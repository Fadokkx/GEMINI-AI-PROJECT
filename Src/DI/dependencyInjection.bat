@echo off
cd /d "%~dp0\..\.."
echo Diretório atual: %CD%

if exist requirements.txt (
    echo Installing dependency injection...
    py -m pip install -r requirements.txt
) else (
    echo ERROR: requirements.txt not found.
    pause
    exit /b 1
)