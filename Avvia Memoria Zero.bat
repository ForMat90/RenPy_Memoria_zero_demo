@echo off
setlocal
cd /d "%~dp0."
if not exist "%~dp0renpy-sdk\renpy.exe" (
  echo.
  echo Questo file deve restare dentro la cartella Memoria_zero_demo,
  echo insieme alle cartelle game e renpy-sdk.
  echo.
  echo Non spostarlo fuori dalla cartella. Se lo vuoi sul Desktop:
  echo tasto destro su questo file, Invia a, Desktop ^(crea collegamento^).
  echo.
  pause
  exit /b 1
)
"%~dp0renpy-sdk\renpy.exe" "%~dp0."
if errorlevel 1 pause
