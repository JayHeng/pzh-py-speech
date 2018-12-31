pyinstaller.exe pyinstaller_pack_fw.spec
copy .\dist\Jays-PySPEECH.exe ..\bin
rd /q /s .\build
rd /q /s .\dist