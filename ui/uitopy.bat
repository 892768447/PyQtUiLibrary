@echo off
set /p name=�������ļ���:
if not defined name (echo δ�����κ�����,��������˳�&pause>nul&exit)
pyuic5 -x %name%.ui -o %name%.py
pause
