@echo off
title Iniciando GeoNova...
echo =======================================
echo   🌎 INICIANDO SERVIDOR GEONOVA
echo =======================================
echo.
cd "%USERPROFILE%\Desktop\GeoNova\backend"
echo Ejecutando servidor FastAPI...
start "" cmd /k "python main.py"
timeout /t 3 >nul
start http://127.0.0.1:8000
exit
