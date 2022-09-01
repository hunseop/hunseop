@echo off
setlocal
set today=%date:~2,2%%date:~5,2%%date:~8,2%
forfiles /p C:\Users\HUN\Desktop /s /c "cmd /c @echo @file" >> C:\Users\HUN\%today%_delete_files.txt
forfiles /p C:\Users\HUN\Desktop /s /c "cmd /c del /s /q @path"
forfiles /p C:\Users\HUN\Desktop /s /c "cmd /c rmdir /s /q @file"