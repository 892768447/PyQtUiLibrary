@echo off
set /p name=请输入文件名:
if not defined name (echo 未输入任何内容,按任意键退出&pause>nul&exit)
pyuic5 -x %name%.ui -o %name%.py
pause
