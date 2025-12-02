# Python Tkinter Application Installer

## Overview
This repository provides a method to automatically install Python Tkinter applications through an installation file and can be used as a template to build larger applications.

## Instructions

### Setup
<ol>
  <li>Download the app installation python script (install-basic-tkinter-application_1_0_0.py).</li>
  <li>Install the prequisite Python libaries:</li>
  <ul>
    <li>configparser *</li>
    <li>io *</li>
    <li>os *</li>
    <li>requests</li>
    <li>shutil *</li>
    <li>subprocess *</li>
    <li>zipfile *</li>
  </ul>
  <li>Run the app installation python script.</li>
  <li>Copy the application file to your desktop for quick access.</li>
</ol>

'* Inlcuded with Python installation.

### Customize

#### Functionality
The <a href="https://github.com/tylerrichman-erg/Python-Tkinter-Application-Installer/blob/main/dev/main.py">dev/main.py</a> Python script contains code for the basic application of the template. This can be altered and expanded upon to include functionality for your application's needs. All code should be contained within the <a href="https://github.com/tylerrichman-erg/Python-Tkinter-Application-Installer/blob/main/dev">dev</a> folder.

#### Configuration
The <a href="https://github.com/tylerrichman-erg/Python-Tkinter-Application-Installer/blob/main/config.ini">config.ini</a> enables developers to set their own configuration parameters for their application. This basic application enables the developers to set the application installation path, application name, source code url of the repository, and application version. This can be expanded to include other configuration parameters.

The source code url parameter must be changed once you create a repository for your own application, otherwise you will install this application. The application installation path will be created if it does not exist, it's not required to create it beforehand.

#### Libraries
All Python libraries utilized within the code needs to be listed within the <a href="https://github.com/tylerrichman-erg/Python-Tkinter-Application-Installer/blob/main/requirements.txt">requirements.txt</a> file. Follow the format of the existing libraries where the library name is listed along with the version that is seperated by "==" (e.g. pillow==11.3.0).

#### Installation File Name
It's recomended to update the installation python script file name from install-basic-tkinter-application_1_0_0.py to a name that fits your application.

### Contact
Email: richmantyler73@gmail.com
