@ECHO OFF
pip install -r requirements.txt
pyinstaller --onefile --icon=assets/logo.ico paper.py
pyinstaller --onefile --uac-admin --icon=assets/logo.ico pen.py