@echo off
echo Starting YouTube Video Downloader...
echo.

:: Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH.
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

:: Run the application
python youtube_downloader.py

if errorlevel 1 (
    echo.
    echo Error running the application. Make sure dependencies are installed.
    echo Run setup.bat first if you haven't already.
    pause
)

echo.
echo Application closed.
pause