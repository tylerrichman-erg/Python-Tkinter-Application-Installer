
## 1) Import Libraries

import io
import os
import requests
#import shutil
import subprocess
import zipfile

## 2) Initialize Variables

app_path = "C:/Program Files (Python)"
app_name = "Basic Python Tkinter Application"
code_zip_url = "https://github.com/tylerrichman-erg/Python-Tkinter-Application-Installer/archive/refs/heads/main.zip"

workspace_path = os.path.join(app_path, app_name)

requirements_txt_path = os.path.join(workspace_path, "requirements.txt")
activate_venv_command = os.path.join(workspace_path, "python-env/Scripts/activate.bat")
python_exe_location = os.path.join(workspace_path, "python-env/Scripts/python.exe")
pip_exe_location = os.path.join(workspace_path, "python-env/Scripts/pip.exe")

## 3) Download Repository to Workspace

response = requests.get(code_zip_url)
response.raise_for_status()

with zipfile.ZipFile(io.BytesIO(response.content)) as z:
    os.makedirs(workspace_path, exist_ok=True)
    z.extractall(workspace_path)

repository_name = "{0}-{1}".format(
    code_zip_url.split("/")[4],
    code_zip_url.split("/")[-1].replace(".zip", "")
)

## 4) Create Python Virtual Environment

if os.path.exists(os.path.join(workspace_path, "python-env")):
    shutil.rmtree(os.path.join(workspace_path, "python-env"))

subprocess.run(['python', '-m', 'venv', os.path.join(workspace_path, "python-env")], check=True)

with open(requirements_txt_path, "r") as f:
    for line in f:
        line = line.strip()   # remove newline
        subprocess.run([activate_venv_command, "&&", python_exe_location, pip_exe_location, "install", line], check=True)

#NOTES
#1) Repository needs to be public for this to work.
#2) Requests may need to be installed via pip if not already available in the Python environment.