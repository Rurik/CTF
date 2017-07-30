import base64
#Need:
#Caption1
HelpContextId = 44
ScrollHeight = 2310 #??
Label1Caption = "UserForm1"
ScrollWidth = 1#??
Zoom      = 1#??
Tag = "BZb+NKtmD9XQ6uQAgJsuvvudb7tZgoD/RCJX"

"""
U8pblvDZuAh8GY.HelpContextId = 44
U8pblvDZuAh8GY.ScrollHeight = 2310 #??
U8pblvDZuAh8GY.Label1.Caption = "UserForm1"
U8pblvDZuAh8GY.ScrollWidth = 1#??
U8pblvDZuAh8GY.Zoom      = 1#??
U8pblvDZuAh8GY.Tag = "BZb+NKtmD9XQ6uQAgJsuvvudb7tZgoD/RCJX"
"""
"""
VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} U8pblvDZuAh8GY
   Caption         =   "UserForm1"
   ClientHeight    =   2310
   ClientLeft      =   120
   ClientTop       =   1095
   ClientWidth     =   1740
   HelpContextID   =   44
   Tag             =   "BZb+NKtmD9XQ6uQAgJsuvvudb7tZgoD/RCJX"
   TypeInfoVer     =   3
End
"""


def Process1(Data_Caption1, Data_NoProc):
    fjGeMmP8Z = base64.b64decode(Data_Caption1)
    Process2(fjGeMmP8Z, Data_NoProc)


def DecodeData_Comp_Label1Caption(dd):
    DecodeData_Comp_Label1Caption = False
    A4xcPiKtrr = base64.b64decode(dd)
    DecodeData_Comp_Label1Caption = XOR_Data_Cmp_Label1Caption(A4xcPiKtrr)

    
def FindProc_Matches_Label1Caption():
    while l < gjvhSFe.CountOfLines:
        za29rx = gjvhSFe.ProcOfLine(l, 0)
        if za29rx != "":
            if DecodeData_Comp_Label1Caption(za29rx):
                return za29rx
            l = l + gjvhSFe.ProcCountLines(za29rx, 0)
        else:
            l = l + 1
    return False

    
def DocumentMain():
    sN2l0P = FindProc_Matches_Label1Caption()
    if sN2l0P:
        for LIndexC in ActiveDocument.VBProject.VBComponents:
            if LIndexC.Type == 1:
                Index = 1
                cm = LIndexC.CodeModule
                while Index < cm.CountOfLines:
                    pn = cm.ProcOfLine(Index, 0)
                    if pn:
                        Process1(pn, sN2l0P)
                        Index = Index + cm.ProcCountLines(pn, 0)
                    else:
                        Index = Index + 1


def XOR_Data_Key(Data, Key):
    result = ''
    for cz9vzhBR in range(0, len(Data)):
        result += chr(ord(Data(cz9vzhBR)) ^ ord(Key))
    return result


def XOR_Key_Data(u48G, G6NK):
    return XOR_Data_Key(G6NK, u48G)


def StringCompare(Rfn10hWpA, XPbV8Rj5Q):
    result = False
    if len(Rfn10hWpA) == len(XPbV8Rj5Q):
        result = True
        for z5PQAfu9 in range(0, len(Rfn10hWpA)):
            if (Rfn10hWpA(z5PQAfu9) != XPbV8Rj5Q(z5PQAfu9)):
                StringCompare = False
                z5PQAfu9 = len(Rfn10hWpA)
    else:
        result = False


def XOR_Data_String(Data, Data2):
    result = ''
    for pos in range(0, len(Data)):
        result += chr( ord(Data[pos]) ^ ord(Data2[pos]) )
    return result

def XOR_Data_Cmp_Label1Caption(Data):
    result = False
    yTV2li = XOR_Data_Key(Data, U8pblvDZuAh8GY.HelpContextId)# ' 44
    VGmMTyf = XOR_Key_Data(Int(U8pblvDZuAh8GY.ScrollHeight), yTV2li)# ' 2310
    if StringCompare(VGmMTyf, base64.b64decode(U8pblvDZuAh8GY.Label1.Caption)):
        result = True
    return result


def Process2(Data, Data2_B64):
    ang8rjzwn = XOR_Data_Key(Data, U8pblvDZuAh8GY.ScrollWidth)
    upnFZMT9P = XOR_Key_Data(U8pblvDZuAh8GY.Zoom, ang8rjzwn)
    s06 = XOR_Data_String(upnFZMT9P, base64.b64decode(Data2_B64))
    if StringCompare(s06, base64.b64decode(StrReverse(U8pblvDZuAh8GY.Tag))):
        print(Data)






"""
Function base64.b64decode(qqZUlc9)
'http://thydzik.com/vb6vba-functions-to-convert-binary-string-to-base64-string/
    Set vW3zM = CreateObject("MSXML2.DOMDocument")
    Set ugBi6C = vW3zM.createElement("b64")
    ugBi6C.dataType = "bin.base" + CStr(vbUnicode)
    ugBi6C.Text = Trim(qqZUlc9)
    base64.b64decode = ugBi6C.nodeTypedValue
    Set ugBi6C = Nothing
    Set vW3zM = Nothing
End Function

Function StrToUnicode(sHZF70G) As String
    TPjEpV = ""
    For cz9vzhBR = 1 To len(sHZF70G)
        TPjEpV = TPjEpV & StrConv(sHZF70G(cz9vzhBR), 64)
    Next
    StrToUnicode = StrConv(sHZF70G, 64)
End Function
"""
if __name__ == "__main__":
    DocumentMain()