<#
  .SYNOPSIS
  Unlocks Office Macro Password Protection.
  .DESCRIPTION
  Unlocks Word/Excel/PowerPoint/etc 2003-2013 format files password protections.

  To access macros in Shared Excel Workbooks click Review -> Share Workbook and untick 

'Allow changes by more than one user'

  An unlocked document will throw error 

    ---------------------------
    Microsoft Visual Basic for Applications
    ---------------------------
    The project file 'C:\support\somefile.docm' contains invalid key 'DPx'.--Continue 

Loading Project?
    ---------------------------
    Yes   No   Help   
    ---------------------------

  Click 'Yes' to continue, macro code will be accessible.
  To remove this warning, set a password on the macro, then remove it, then resave 

document.

  Common issues:

    - This is relying on Shell for ZIP/UNZIP if working on Office 2007+ format files
      This method is not very robust and will not be surprised if it breaks.
      
      If you get pop-up errors can't read file/etc then increase delay in line 

        Start-Sleep -Seconds 3

    - This script does not have huge amount of error checking. 

  .EXAMPLE
  Unlock-OfficeMacro ProtectedWord.doc UnprotectedWord.doc
  .EXAMPLE
  Unlock-OfficeMacro C:\support\ProtectedWord.docm UnprotectedWord.docm
  .EXAMPLE
  Unlock-OfficeMacro -InputFile C:\support\ProtectedExcel.xlsm -OutputFile 

UnProtected.xlsm
  .PARAMETER InputFile
  The password protected office document.
  .PARAMETER OutputFile
  The output file with password protection removed. Should have same extension as 

inputfile.
  .NOTES
  By Malcolm McCaffery
  http://chentiangemalc.wordpress.com
  #>


[CmdletBinding()]
Param(
  [Parameter(Mandatory=$True,Position=1)]
   [string]$InputFile,
    
   [Parameter(Mandatory=$True,Position=2)]
   [string]$OutputFile
)

 
# Binary "IndexOf"
# too lazy (or busy…) to write this code in PowerShell, couldn’t find any good 

PowerShell example
# And this is fast. From http://stackoverflow.com/users/649008/foubar
# at http://stackoverflow.com/questions/283456/byte-array-pattern-search
$compilerParameters = New-Object System.CodeDom.Compiler.CompilerParameters
$compilerParameters.CompilerOptions="/unsafe"
Add-Type -PassThru -CompilerParameters $compilerParameters -TypeDefinition @"
using System;
using System.Collections.Generic;
 
public static class FastByte
{
    public static unsafe long IndexOf(byte[] Haystack, byte[] Needle)
    {
        fixed (byte* H = Haystack) fixed (byte* N = Needle)
        {
            long i = 0;
            for (byte* hNext = H, hEnd = H + Haystack.LongLength; hNext < hEnd; i++, 

hNext++)
            {
                bool Found = true;
                for (byte* hInc = hNext, nInc = N, nEnd = N + Needle.LongLength; Found 

&& nInc < nEnd; Found = *nInc == *hInc, nInc++, hInc++);
                if (Found) return i;
            }
            return -1;
        }
    }
}
"@

# check if file locked
Function Test-FileLocked
{
    param(
        [string]$Filename)

    $HRFileLocked = 0x80070020;
    $HRPortionOfFileLocked = 0x80070021;
  
    "Test $Filename is locked"
    try
    {
        $fs = [System.IO.File]::Open($filename,
                [System.IO.FileMode]::OpenOrCreate,
                [System.IO.FileAccess]::ReadWrite,
                [System.IO.Fileshare]::Write)
       
        $fs.Close()

        # file is not locked
        return $false
    }
    catch [System.IO.IOException]
    { 
        "Error accessing $filename : $_"
        $errorCode = [System.Runtime.InteropServices.Marshal]::GetHRForException

($_.Exception)
        if ($errorCode -eq $HRFileLocked -or $errorCode -eq $HRPortionOfFileLocked)
        {
            # file is locked!
            return $true
        }
        else
        {
            # failures to open file, besides file is locked
            throw
        }
    }
}

# wait for file to become unlocked
Function Wait-File
{
    param(
        [string]$FileName,
        [System.TimeSpan]$Timeout=(New-TimeSpan -Seconds 60))


    $StopWatch = [Diagnostics.StopWatch]::StartNew()
    while ($StopWatch.Elapsed -lt $Timeout)
    {
        if ((Test-FileLocked -FileName $FileName) -eq $true)
        {
        
            "$FileName is locked, retrying"
        }
        else
        {
            "$FileName is NOT locked"
            return
        }
 
        Start-Sleep -Milliseconds 500
    }

}

Function Send-ZipFile
{
    param(
    [string]$zipFilename,
    [string]$filename) 
 
    $zipHeader=[char]80 + [char]75 + [char]5 + [char]6 + [char]0 + [char]0 + [char]0 + 

[char]0 + [char]0 + [char]0 + [char]0 + [char]0 + [char]0 + [char]0 + [char]0 + [char]0 

+ [char]0 + [char]0 + [char]0 + [char]0 + [char]0 + [char]0 
 
    # Check to see if the Zip file exists, if not create a blank one 
    If ( (Test-Path $zipfilename) -eq $FALSE )
    { 
        Add-Content $zipfilename -value $zipHeader 
    } 
 
    # Create an instance to Windows Explorer's Shell comObject 
    $ExplorerShell=New-Object -ComObject Shell.Application

    # Send whatever file / Folder is specified in $filename to the Zipped folder 

$zipfilename 
    $SendToZip=$ExplorerShell.Namespace($zipFilename.tostring()).CopyHere

($filename.ToString(),0)
     
    # sleep long enough for "Copy here to at least start..."
    # this is a bit ugly but necessary if relying on shell 
    # to put multiple files in the ZIP file
    Start-Sleep -Seconds 3

    # wait for any writing to be completed on ZIP file
    Wait-File $ZipFilename
  
}

Function Expand-ZIPFile
{
    Param(
        [String]$ZipFilename,
        [String]$DestinationPath)

     $shell = New-Object -ComObject Shell.Application
     $zip = $shell.NameSpace($ZipFileName)
     "Expand to $destination"
     $shell.Namespace($DestinationPath).CopyHere($zip.Items())
}

$O2k7Format = $false

# We’ll work on the copy—just in case we mess up the original
Copy-Item $InputFile $OutputFile
 
# Load our target file all at once
# Not scalable … &c but works to test the concept
Write-Host "Loading $OutputFile"
$data=Get-Content -Encoding Byte $OutputFile

$tempFolder=""

# check if we are using Office 2007 or later file format
# by looking for PK header (ZIP file)...
if ($data[0] -eq 80 -and $data[1] -eq 75)
{
    $O2k7Format = $true

    "Office 2007+ format, unzipping contents"
    # yes ... must unzip file first
    $tempFolder = [System.IO.Path]::Combine(
            [System.IO.Path]::GetTempPath(),
            [System.IO.Path]::GetRandomFileName())

    # Rename output file to ZIP so we can use Shell 'unzip'
    $ZipFileName = $OutputFile + ".zip"

    Move-Item -Path $OutputFile -Destination $ZipFileName -Force
    New-Item -ItemType Directory -Path $tempFolder
    
    "Expanding files to $tempFolder"
    Expand-ZIPFile -ZipFileName $ZipFileName -DestinationPath $tempFolder
    
    # we don't need the ZIP file anymore, delete it
    Remove-Item $ZipFileName

    # get vbaProject.bin filename
    $vbaFileName = (Get-ChildItem -Path $tempFolder -Filter vbaProject.bin -Recurse)

#[0].FullName
    
    # use vbaProject.bin as our data stream
    $data=Get-Content -Encoding Byte $vbaFileName

}
 
Write-Host "Searching file contents"
# The string we need to replace ( DPB= )
[Byte[]] $searchBytes = 0x44,0x50,0x42,0x3D,0x22

# This is the string we will use to break the macro protection ( DPx= )
[Byte[]] $replaceBytes = 0x44,0x50,0x78,0x3D,0x22
 
$index=[FastByte]::IndexOf($data,$searchBytes)

Write-Host "Key found at $index"
 
# update file
if ($o2k7format)
{
    [System.IO.Stream]$stream = [System.IO.File]::Open($vbaFileName,

[System.IO.FileMode]::Open)
}
else
{
    [System.IO.Stream]$stream = [System.IO.File]::Open($OutputFile,

[System.IO.FileMode]::Open)
}

# write our replacement key
$stream.Position=$index
$stream.Write($replaceBytes,0,$replaceBytes.Length)
$stream.Dispose()
 
 # if office 2007+ format, we need to rezip contents
if ($o2k7format)
{
    "Building ZIP file at $($OutputFile).zip"

    # delete ZIP if it already exists
    if (Test-Path $ZipFilename)
    { 
        Remove-Item $ZipFilename
    }

    # rebuild Office "ZIP" file 
    ForEach ($file in Get-ChildItem $tempFolder)
    {
        "Adding $($file.FullName) to $ZipFilename"
        Send-ZipFile -ZipFileName $ZipFilename -filename $file.FullName
    }

    "Moving $ZipFilename to $OutputFile"
    Wait-File $ZipFilename
    Move-Item -Path $ZipFilename -Destination $OutputFile -Force
    Remove-Item $tempFolder -Recurse
}

Write-Host "Update Complete! Output file: $OutputFile"
 