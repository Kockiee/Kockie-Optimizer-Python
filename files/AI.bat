@echo off
cls
echo Isso pode demorar alguns minutos !
echo Isso pode demorar alguns minutos !
echo Isso pode demorar alguns minutos !
echo Isso pode demorar alguns minutos !
::Launchers
winget install Valve.Steam -h
winget install EpicGames.EpicGamesLauncher -h
winget install Ubisoft.Connect -h

::Frameworks
winget install Microsoft.dotnetRuntime.3-x64 -h
winget install Microsoft.dotnetRuntime.5-x64 -h

::Drivers
REM cinst intel-chipset-device-software -y
REM cinst nvidia-display-driver -y
REM cinst intel-graphics-driver -y
REM cinst intel-rst-driver -y
winget install AMD.RyzenMaster -h


::Uteís
winget install BraveSoftware.BraveBrowser -h
winget install RARLab.WinRAR
winget install CPUID.CPU-Z -h
winget install Microsoft.Office -h
winget install Notepad++.Notepad++ -h
cinst msiafterburner -y

TIMEOUT /T 5
taskkill /f /im explorer.exe
start explorer.exe

