@echo off
echo YouTube Video Downloader Setup
echo ================================
echo.
echo Installing required dependencies...
echo.

:: Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH.
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

:: Install pip packages
echo Installing Python packages...
pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo Error installing dependencies. Please check your internet connection.
    pause
    exit /b 1
)

echo.
echo Setup completed successfully!
echo.
echo To run the YouTube downloader, execute: python youtube_downloader.py
echo Or simply double-click on run.bat
echo.
pause