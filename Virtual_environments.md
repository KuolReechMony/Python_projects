# Virtual environments - venv

Both: cd ./Project_folder

Win: CMD
LInux: Terminal

# Create a new virtual environment
Win: python3 -m venv Environment_name
Linux: python3 -m venv Environment_name

# Activate environment
Win: .\Environment_name\Scripts\activate.bat
Linux: source Environment_name/bin/activate

# Deactivate
Both: deactivate

# Share environment
pip freeze > requirements.txt
pip install -r requirements.txt