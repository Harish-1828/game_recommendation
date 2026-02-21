@echo off
REM Steam Review Prediction - Quick Start Script for Windows

echo ============================================================
echo    STEAM GAME REVIEW RECOMMENDATION PREDICTION
echo ============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/
    pause
    exit /b 1
)

echo [Step 1] Installing dependencies...
echo.
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo ============================================================
echo [Step 2] Training Machine Learning Model...
echo ============================================================
echo.
python train_model.py
if errorlevel 1 (
    echo ERROR: Model training failed
    pause
    exit /b 1
)

echo.
echo ============================================================
echo [Step 3] Starting Flask Web Application...
echo ============================================================
echo.
echo The application will open at: http://127.0.0.1:5000/
echo Press CTRL+C to stop the server
echo.
python app.py

pause
