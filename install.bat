@echo off
echo Installing Python
start python-3.7.0-amd64-webinstall.exe
set /p Var1="Press Enter when Python Installation is complete"
cls
pip install easyimap
