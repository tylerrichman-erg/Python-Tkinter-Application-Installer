## 1) Import Libraries

import io
import os
import requests
import shutil
import subprocess
import zipfile

## 2) Initialize Variables

app_path = "C:/Program Files (Python)"
app_name = "Basic Python Tkinter Application"
code_zip_url = "https://github.com/tylerrichman-erg/Python-Tkinter-Application-Installer/archive/refs/heads/main.zip"

workspace_path = os.path.join(app_path, app_name)

repository_name = "{0}-{1}".format(
    code_zip_url.split("/")[4],
    code_zip_url.split("/")[-1].replace(".zip", "")
)
repository_path = os.path.join(workspace_path, repository_name)

requirements_txt_path = os.path.join(repository_path, "requirements.txt")
activate_venv_command = os.path.join(workspace_path, "python-env/Scripts/activate.bat")
python_exe_location = os.path.join(workspace_path, "python-env/Scripts/python.exe")
pip_exe_location = os.path.join(workspace_path, "python-env/Scripts/pip.exe")

main_py_location = os.path.join(repository_path, "dev/main.py")
main_exe_folder_location = os.path.join(workspace_path, "exe")
pyinstaller_exe_location = os.path.join(workspace_path, "python-env/Scripts/pyinstaller.exe")
icon_location = os.path.join(repository_path, "img/icon/main.png")

output_exe_location = os.path.join(workspace_path, "exe/dist/main.exe")
final_exe_location = os.path.join(workspace_path, "Basic-Tkinter-Application_0_1_0.exe")

## 3) Download Repository to Workspace

response = requests.get(code_zip_url)
response.raise_for_status()

with zipfile.ZipFile(io.BytesIO(response.content)) as z:
    os.makedirs(workspace_path, exist_ok=True)
    z.extractall(workspace_path)

## 4) Create Python Virtual Environment

if os.path.exists(os.path.join(workspace_path, "python-env")):
    shutil.rmtree(os.path.join(workspace_path, "python-env"))

subprocess.run(['python', '-m', 'venv', os.path.join(workspace_path, "python-env")], check=True)

with open(requirements_txt_path, "r") as f:
    for line in f:
        line = line.strip()   # remove newline
        subprocess.run([activate_venv_command, "&&", python_exe_location, pip_exe_location, "install", line], check=True)

## 5) Create Enviroment for Application

if os.path.exists(main_exe_folder_location):
    shutil.rmtree(main_exe_folder_location)

if not os.path.exists(main_exe_folder_location):
    os.makedirs(main_exe_folder_location)

## 6) Install Application

try:
    command = (
        f'"{activate_venv_command}" && '
        f'cd "{main_exe_folder_location}" && '
        f'"{pyinstaller_exe_location}" --onefile --noconsole '
        f'--icon="{icon_location}" '
        f'--add-data=dev;dev '
        f'--add-data=img;img '
        #f'--add-data=txt;txt '
        f'--add-data=default_installation_file.py;. '
        f'--add-data=config.ini;. '
        f'"{main_py_location}"'
    )
    subprocess.run(command, shell=True, check=True)

except:
    proc = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(proc.stdout)
    print(proc.stderr)

shutil.copy(
    output_exe_location,
    final_exe_location
    )

#NOTES
#1) Repository needs to be public for this to work.
#2) Requests may need to be installed via pip if not already available in the Python environment.