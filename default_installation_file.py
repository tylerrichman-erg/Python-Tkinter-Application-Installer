import os
#import shutil
import subprocess

app_path = "C:\Program Files (Python)"
app_name = "Basic Python Tkinter Application"
repo_url = "https://github.com/tylerrichman-erg/Python-Tkinter-Application-Installer.git"

workspace_path = os.path.join(app_path, app_name)

os.makedirs(workspace_path, exist_ok=True)

subprocess.run(
        ["git", "clone", repo_url, workspace_path],
        check=True
    )