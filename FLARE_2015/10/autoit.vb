Global $standard_rights_required = 983040
Global $sc_manager_connect = 1
Global $sc_manager_create_service = 2
Global $sc_manager_enumerate_service = 4
Global $sc_manager_lock = 8
Global $sc_manager_query_lock_status = 16
Global $sc_manager_modify_boot_config = 32
Global $sc_manager_all_access = BitOR($standard_rights_required, $sc_manager_connect, $sc_manager_create_service, $sc_manager_enumerate_service, $sc_manager_lock, $sc_manager_query_lock_status, $sc_manager_modify_boot_config)
Global $service_query_config = 1
Global $service_change_config = 2
Global $service_query_status = 4
Global $service_enumerate_dependents = 8
Global $service_start = 16
Global $service_stop = 32
Global $service_pause_continue = 64
Global $service_interrogate = 128
Global $service_user_defined_control = 256
Global $service_all_access = BitOR($standard_rights_required, $service_query_config, $service_change_config, $service_query_status, $service_enumerate_dependents, $service_start, $service_stop, $service_pause_continue, $service_interrogate, $service_user_defined_control)
Global $service_control_stop = 1
Global $service_control_pause = 2
Global $service_control_continue = 3
Global $service_control_interrogate = 4
Global $service_control_shutdown = 5
Global $service_control_paramchange = 6
Global $service_control_netbindadd = 7
Global $service_control_netbindremove = 8
Global $service_control_netbindenable = 9
Global $service_control_netbinddisable = 10
Global $service_control_deviceevent = 11
Global $service_control_hardwareprofilechange = 12
Global $service_control_powerevent = 13
Global $service_control_sessionchange = 14
Global $service_kernel_driver = 1
Global $service_file_system_driver = 2
Global $service_adapter = 4
Global $service_recognizer_driver = 8
Global $service_driver = BitOR($service_kernel_driver, $service_file_system_driver, $service_recognizer_driver)
Global $service_win32_own_process = 16
Global $service_win32_share_process = 32
Global $service_win32 = BitOR($service_win32_own_process, $service_win32_share_process)
Global $service_interactive_process = 256
Global $service_type_all = BitOR($service_win32, $service_adapter, $service_driver, $service_interactive_process)
Global $service_boot_start = 0
Global $service_system_start = 1
Global $service_auto_start = 2
Global $service_demand_start = 3
Global $service_disabled = 4
Global $service_error_ignore = 0
Global $service_error_normal = 1
Global $service_error_severe = 2
Global $service_error_critical = 3

Func _startservice($scomputername, $sservicename)
	Local $hadvapi32
	Local $hkernel32
	Local $arret
	Local $hsc
	Local $hservice
	Local $lerror = -1
	$hadvapi32 = DllOpen("advapi32.dll")
	If $hadvapi32 = -1 Then Return 0
	$hkernel32 = DllOpen("kernel32.dll")
	If $hkernel32 = -1 Then Return 0
	$arret = DllCall($hadvapi32, "long", "OpenSCManager", "str", $scomputername, "str", "ServicesActive", "long", $sc_manager_connect)
	If $arret[0] = 0 Then
		$arret = DllCall($hkernel32, "long", "GetLastError")
		$lerror = $arret[0]
	Else
		$hsc = $arret[0]
		$arret = DllCall($hadvapi32, "long", "OpenService", "long", $hsc, "str", $sservicename, "long", $service_start)
		If $arret[0] = 0 Then
			$arret = DllCall($hkernel32, "long", "GetLastError")
			$lerror = $arret[0]
		Else
			$hservice = $arret[0]
			$arret = DllCall($hadvapi32, "int", "StartService", "long", $hservice, "long", 0, "str", "")
			If $arret[0] = 0 Then
				$arret = DllCall($hkernel32, "long", "GetLastError")
				$lerror = $arret[0]
			EndIf
			DllCall($hadvapi32, "int", "CloseServiceHandle", "long", $hservice)
		EndIf
		DllCall($hadvapi32, "int", "CloseServiceHandle", "long", $hsc)
	EndIf
	DllClose($hadvapi32)
	DllClose($hkernel32)
	If $lerror <> -1 Then
		SetError($lerror)
		Return 0
	EndIf
	Return 1
EndFunc

Func _stopservice($scomputername, $sservicename)
	Local $hadvapi32
	Local $hkernel32
	Local $arret
	Local $hsc
	Local $hservice
	Local $lerror = -1
	$hadvapi32 = DllOpen("advapi32.dll")
	If $hadvapi32 = -1 Then Return 0
	$hkernel32 = DllOpen("kernel32.dll")
	If $hkernel32 = -1 Then Return 0
	$arret = DllCall($hadvapi32, "long", "OpenSCManager", "str", $scomputername, "str", "ServicesActive", "long", $sc_manager_connect)
	If $arret[0] = 0 Then
		$arret = DllCall($hkernel32, "long", "GetLastError")
		$lerror = $arret[0]
	Else
		$hsc = $arret[0]
		$arret = DllCall($hadvapi32, "long", "OpenService", "long", $hsc, "str", $sservicename, "long", $service_stop)
		If $arret[0] = 0 Then
			$arret = DllCall($hkernel32, "long", "GetLastError")
			$lerror = $arret[0]
		Else
			$hservice = $arret[0]
			$arret = DllCall($hadvapi32, "int", "ControlService", "long", $hservice, "long", $service_control_stop, "str", "")
			If $arret[0] = 0 Then
				$arret = DllCall($hkernel32, "long", "GetLastError")
				$lerror = $arret[0]
			EndIf
			DllCall($hadvapi32, "int", "CloseServiceHandle", "long", $hservice)
		EndIf
		DllCall($hadvapi32, "int", "CloseServiceHandle", "long", $hsc)
	EndIf
	DllClose($hadvapi32)
	DllClose($hkernel32)
	If $lerror <> -1 Then
		SetError($lerror)
		Return 0
	EndIf
	Return 1
EndFunc

Func _serviceexists($scomputername, $sservicename)
	Local $hadvapi32
	Local $arret
	Local $hsc
	Local $bexist = 0
	$hadvapi32 = DllOpen("advapi32.dll")
	If $hadvapi32 = -1 Then Return 0
	$arret = DllCall($hadvapi32, "long", "OpenSCManager", "str", $scomputername, "str", "ServicesActive", "long", $sc_manager_connect)
	If $arret[0] <> 0 Then
		$hsc = $arret[0]
		$arret = DllCall($hadvapi32, "long", "OpenService", "long", $hsc, "str", $sservicename, "long", $service_interrogate)
		If $arret[0] <> 0 Then
			$bexist = 1
			DllCall($hadvapi32, "int", "CloseServiceHandle", "long", $arret[0])
		EndIf
		DllCall($hadvapi32, "int", "CloseServiceHandle", "long", $hsc)
	EndIf
	DllClose($hadvapi32)
	Return $bexist
EndFunc

Func _servicerunning($scomputername, $sservicename)
	Local $hadvapi32
	Local $arret
	Local $hsc
	Local $hservice
	Local $brunning = 0
	$hadvapi32 = DllOpen("advapi32.dll")
	If $hadvapi32 = -1 Then Return 0
	$arret = DllCall($hadvapi32, "long", "OpenSCManager", "str", $scomputername, "str", "ServicesActive", "long", $sc_manager_connect)
	If $arret[0] <> 0 Then
		$hsc = $arret[0]
		$arret = DllCall($hadvapi32, "long", "OpenService", "long", $hsc, "str", $sservicename, "long", $service_interrogate)
		If $arret[0] <> 0 Then
			$hservice = $arret[0]
			$arret = DllCall($hadvapi32, "int", "ControlService", "long", $hservice, "long", $service_control_interrogate, "str", "")
			$brunning = $arret[0]
			DllCall($hadvapi32, "int", "CloseServiceHandle", "long", $hservice)
		EndIf
		DllCall($hadvapi32, "int", "CloseServiceHandle", "long", $hsc)
	EndIf
	DllClose($hadvapi32)
	Return $brunning
EndFunc

Func _createservice($scomputername, $sservicename, $sdisplayname, $sbinarypath, $sserviceuser = 0, $spassword = "", $nservicetype = 16, $nstarttype = 2, $nerrortype = 1, $ndesiredaccess = 983551, $sloadordergroup = "")
	Local $hadvapi32
	Local $hkernel32
	Local $arret
	Local $hsc
	Local $lerror = -1
	$hadvapi32 = DllOpen("advapi32.dll")
	If $hadvapi32 = -1 Then Return 0
	$hkernel32 = DllOpen("kernel32.dll")
	If $hkernel32 = -1 Then Return 0
	$arret = DllCall($hadvapi32, "long", "OpenSCManager", "str", $scomputername, "str", "ServicesActive", "long", $sc_manager_all_access)
	If $arret[0] = 0 Then
		$arret = DllCall($hkernel32, "long", "GetLastError")
		$lerror = $arret[0]
	Else
		$hsc = $arret[0]
		$arret = DllCall($hadvapi32, "long", "OpenService", "long", $hsc, "str", $sservicename, "long", $service_interrogate)
		If $arret[0] = 0 Then
			If $sserviceuser = 0 Then
				$arret = DllCall($hadvapi32, "long", "CreateService", "long", $hsc, "str", $sservicename, "str", $sdisplayname, "long", $ndesiredaccess, "long", $nservicetype, "long", $nstarttype, "long", $nerrortype, "str", $sbinarypath, "str", $sloadordergroup, "ptr", 0, "str", "", "ptr", 0, "str", $spassword)
			Else
				$arret = DllCall($hadvapi32, "long", "CreateService", "long", $hsc, "str", $sservicename, "str", $sdisplayname, "long", $ndesiredaccess, "long", $nservicetype, "long", $nstarttype, "long", $nerrortype, "str", $sbinarypath, "str", $sloadordergroup, "ptr", 0, "str", "", "str", $sserviceuser, "str", $spassword)
			EndIf
			If $arret[0] = 0 Then
				$arret = DllCall($hkernel32, "long", "GetLastError")
				$lerror = $arret[0]
			Else
				DllCall($hadvapi32, "int", "CloseServiceHandle", "long", $arret[0])
			EndIf
		Else
			DllCall($hadvapi32, "int", "CloseServiceHandle", "long", $arret[0])
		EndIf
		DllCall($hadvapi32, "int", "CloseServiceHandle", "long", $hsc)
	EndIf
	DllClose($hadvapi32)
	DllClose($hkernel32)
	If $lerror <> -1 Then
		SetError($lerror)
		Return 0
	EndIf
	Return 1
EndFunc

Func _deleteservice($scomputername, $sservicename)
	Local $hadvapi32
	Local $hkernel32
	Local $arret
	Local $hsc
	Local $hservice
	Local $lerror = -1
	$hadvapi32 = DllOpen("advapi32.dll")
	If $hadvapi32 = -1 Then Return 0
	$hkernel32 = DllOpen("kernel32.dll")
	If $hkernel32 = -1 Then Return 0
	$arret = DllCall($hadvapi32, "long", "OpenSCManager", "str", $scomputername, "str", "ServicesActive", "long", $sc_manager_all_access)
	If $arret[0] = 0 Then
		$arret = DllCall($hkernel32, "long", "GetLastError")
		$lerror = $arret[0]
	Else
		$hsc = $arret[0]
		$arret = DllCall($hadvapi32, "long", "OpenService", "long", $hsc, "str", $sservicename, "long", $service_all_access)
		If $arret[0] = 0 Then
			$arret = DllCall($hkernel32, "long", "GetLastError")
			$lerror = $arret[0]
		Else
			$hservice = $arret[0]
			$arret = DllCall($hadvapi32, "int", "DeleteService", "long", $hservice)
			If $arret[0] = 0 Then
				$arret = DllCall($hkernel32, "long", "GetLastError")
				$lerror = $arret[0]
			EndIf
			DllCall($hadvapi32, "int", "CloseServiceHandle", "long", $hservice)
		EndIf
		DllCall($hadvapi32, "int", "CloseServiceHandle", "long", $hsc)
	EndIf
	DllClose($hadvapi32)
	DllClose($hkernel32)
	If $lerror <> -1 Then
		SetError($lerror)
		Return 0
	EndIf
	Return 1
EndFunc

If @OSArch <> "X86" Then
	MsgBox(0, "Unsupported architecture", "Must be run on x86 architecture")
	Exit
EndIf
If @OSVersion = "WIN_7" Then
	FileInstall("challenge-7.sys", @SystemDir & "\challenge.sys")
ElseIf @OSVersion = "WIN_XP" Then
	FileInstall("challenge-xp.sys", @SystemDir & "\challenge.sys")
Else
	MsgBox(0, "Unsupported OS", "Must be run on Windows XP or Windows 7")
	Exit
EndIf
FileInstall("ioctl.exe", @SystemDir & "\ioctl.exe")
$nret = dothis("0x96c581bc009905e76931875a583f97a738b764eb67f35c802194bf86123b943d1907619488a31a26cf29ba5f5e57ed5c5a37cb5d67dc2020a7e6d55cadefba32aba3ed77f0e18e41a571e74a8a7614a895d7c8827c46028761994543bf449138c65a6e7b5039792c85be5b4998c9950d2497f73cd88d186a6bffe3634bd250ec59e2", "flarebearstare")
If $nret Then
	If dothis("0x96d587b8139933d17e3598505e729da736bb66aa6cfa5180289fb6845530", "flarebearstare") Then
		dothis("0x9aee96b50da818d16f368556131aecfc69ef21a440f24fcc6bd1f3bd1e76db69574a6c8d81ed53688a7eaa364e53fd0700", "flarebearstare")
	EndIf
EndIf

Func decrypt($data, $key)
	Local $opcode = "0xC81001006A006A005356578B551031C989C84989D7F2AE484829C88945F085C00F84DC000000B90001000088C82C0188840DEFFEFFFFE2F38365F4008365FC00817DFC000100007D478B45FC31D2F775F0920345100FB6008B4DFC0FB68C0DF0FEFFFF01C80345F425FF0000008945F48B75FC8A8435F0FEFFFF8B7DF486843DF0FEFFFF888435F0FEFFFFFF45FCEBB08D9DF0FEFFFF31FF89FA39550C76638B85ECFEFFFF4025FF0000008985ECFEFFFF89D80385ECFEFFFF0FB6000385E8FEFFFF25FF0000008985E8FEFFFF89DE03B5ECFEFFFF8A0689DF03BDE8FEFFFF860788060FB60E0FB60701C181E1FF0000008A840DF0FEFFFF8B750801D6300642EB985F5E5BC9C21000"
	Local $codebuffer = DllStructCreate("byte[" & BinaryLen($opcode) & "]")
	DllStructSetData($codebuffer, 1, $opcode)
	Local $buffer = DllStructCreate("byte[" & BinaryLen($data) & "]")
	DllStructSetData($buffer, 1, $data)
	DllCall("user32.dll", "none", "CallWindowProc", "ptr", DllStructGetPtr($codebuffer), "ptr", DllStructGetPtr($buffer), "int", BinaryLen($data), "str", $key, "int", 0)
	Local $ret = DllStructGetData($buffer, 1)
	$buffer = 0
	$codebuffer = 0
	Return $ret
EndFunc

Func dothis($data, $key)
	$exe = decrypt($data, $key)
	$exe = BinaryToString($exe)
	Return Execute($exe)
EndFunc
