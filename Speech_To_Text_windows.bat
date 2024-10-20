@echo off
:: Change to the directory where the application is located
:: Asagiya yazilan yol, uygulamanin bulundugu dizine gore degistirilmelidir.
cd /d "%UserProfile%\Desktop\Speech_to_text_app"

:: Run the Python script using python3
python app.py
