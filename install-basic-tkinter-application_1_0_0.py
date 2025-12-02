## 1) Import Libraries

import configparser
import io
import os
import requests
import shutil
import subprocess
import zipfile

## 2) Initialize Variables

config = configparser.ConfigParser()
config.read("config.ini")

app_path = "C:/Program Files (Python)"
app_name = "Basic Python Tkinter Application"
source_code_url = "https://github.com/tylerrichman-erg/Python-Tkinter-Application-Installer/archive/refs/heads/main.zip"
app_version = "1.0.0"

repository_name = "{0}-{1}".format(
    source_code_url.split("/")[4],
    source_code_url.split("/")[-1].replace(".zip", "")
)

workspace_path = os.path.join(app_path, app_name)
python_env_path = os.path.join(workspace_path, "python-env")
repository_path = os.path.join(workspace_path, repository_name)
main_exe_folder_location = os.path.join(workspace_path, "exe")

activate_venv_command = os.path.join(python_env_path, "Scripts/activate.bat")
python_exe_location = os.path.join(python_env_path, "Scripts/python.exe")
pip_exe_location = os.path.join(python_env_path, "Scripts/pip.exe")
pyinstaller_exe_location = os.path.join(python_env_path, "Scripts/pyinstaller.exe")

requirements_txt_path = os.path.join(repository_path, "requirements.txt")
main_py_location = os.path.join(repository_path, "dev/main.py")
icon_location = os.path.join(repository_path, "img/icon.png")

output_exe_location = os.path.join(workspace_path, "exe/dist/main.exe")
final_exe_location = os.path.join(workspace_path, f"{app_name}.exe")

## 3) Download Repository to Workspace

print(f"INSTALLATION FILE MESSAGE: Downloading application code from {source_code_url}.")

response = requests.get(source_code_url)
response.raise_for_status()

with zipfile.ZipFile(io.BytesIO(response.content)) as z:
    os.makedirs(workspace_path, exist_ok=True)
    z.extractall(workspace_path)

## 4) Create Python Virtual Environment

print(f"INSTALLATION FILE MESSAGE: Creating Python Virtual Environment.")

if os.path.exists(python_env_path):
    shutil.rmtree(python_env_path)

subprocess.run(['python', '-m', 'venv', python_env_path], check=True)

with open(requirements_txt_path, "r") as f:
    for line in f:
        line = line.strip()   # remove newline
        subprocess.run([activate_venv_command, "&&", python_exe_location, pip_exe_location, "install", line], check=True)

## 5) Create Enviroment for Application

print(f"INSTALLATION FILE MESSAGE: Creating Application Environment.")

if os.path.exists(main_exe_folder_location):
    shutil.rmtree(main_exe_folder_location)

if not os.path.exists(main_exe_folder_location):
    os.makedirs(main_exe_folder_location)

items = os.listdir(repository_path)
filtered_items = [x for x in items if x not in [".git", ".gitattributes", "README.md"]]

for filtered_item in filtered_items:
    print(filtered_item)
    if os.path.isdir(filtered_item):
        print("Folder")
        shutil.copytree(
            os.path.join(repository_path, filtered_item),
            os.path.join(main_exe_folder_location, filtered_item)
        )
    else:
        print("File")
        shutil.copy(
            os.path.join(repository_path, filtered_item),
            os.path.join(main_exe_folder_location, filtered_item)
        )

## 6) Create Executable of Application

print(f"INSTALLATION FILE MESSAGE: Creating Application File.")

try:
    command = (
        f'"{activate_venv_command}" && '
        f'cd "{main_exe_folder_location}" && '
        f'"{pyinstaller_exe_location}" --onefile --noconsole '
        f'--icon="{icon_location}" '
        f'--add-data=dev;dev '
        f'--add-data=img;img '
        #f'--add-data=txt;txt '
        f'--add-data=install-basic-tkinter-application_0_1_0.py;. '
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

print(f"INSTALLATION FILE MESSAGE: Installation Complete! Application located at: {final_exe_location}.")

#NOTES
#1) Repository needs to be public for this to work.
#2) Requests may need to be installed via pip if not already available in the Python environment.