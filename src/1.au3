#include <StringConstants.au3>

;~ MsgBox(0,"LogonDNSDomain",@LogonDNSDomain)

HttpSetUserAgent ( "gfTicket" )

Local $dData = InetRead("http://192.168.1.235:8000/SSO/api/getTadminPassword/" & @LogonDNSDomain, 3)
Local $sData = BinaryToString($dData)
;~ MsgBox(0, "", $sData)
Local $aArray = StringSplit($sData, @CRLF )
Local $sDomainUser = $aArray[1]
Local $sDomainPassword = $aArray[2]

Func _RunAsWait($sCommand)
   RunAsWait ( $sDomainUser, @LogonDomain, $sDomainPassword, 1, $sCommand , @ScriptDir )
EndFunc

_RunAsWait("notepad.exe")