#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
#SingleInstance Force

^p::
Send, !{Tab}
Sleep 100
Send, +{F10}
Sleep, 100
Send, !{Tab}
return

^l::
Send, !{Tab}
Sleep 100
Send, ^{F2}
Sleep, 100
Send, !{Tab}
return

^t::
Send, {Enter}
return

^Esc:: ExitApp