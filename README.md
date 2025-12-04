# Python Tkinter Application Installer

## Overview
This repository provides a framework for the automatic installation of <a href="https://www.python.org/">Python</a> <a href="https://docs.python.org/3/library/tkinter.html">Tkinter</a> applications. This framework utilizes an installation file to download the corresponding repository, create a virtual environment, and generate an executable file for the application. This repository can be used as a template to build larger applications with automatic installation functionality. Refer to the next section for instructions on how to do this.

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

\* Already inlcuded with Python installation.

### Customize

#### Functionality
The <a href="https://github.com/tylerrichman-erg/Python-Tkinter-Application-Installer/blob/main/dev/main.py">dev/main.py</a> Python script contains code for the basic application. This can be altered and expanded upon to include functionality for your application's specific needs. All code associated with the application (except the installation file) should be contained within the <a href="https://github.com/tylerrichman-erg/Python-Tkinter-Application-Installer/blob/main/dev">dev</a> folder.

#### Configuration
The <a href="https://github.com/tylerrichman-erg/Python-Tkinter-Application-Installer/blob/main/config.ini">config.ini</a> file enables developers to set their own configuration parameters for their application. This basic application enables the developers to set the application name, application version, installation path, source code url, and window size. This should be altered and expanded upon to include other configurable parameters within your application.

The source code url parameter must be changed once you create a repository for your own application, otherwise you will install this application. The installation path will be created if it does not exist, it's not required to create it beforehand.

#### Libraries
All external Python libraries required for the application need to be included within the <a href="https://github.com/tylerrichman-erg/Python-Tkinter-Application-Installer/blob/main/requirements.txt">requirements.txt</a> file. Follow the format of the existing libraries where the library name is listed along with the version that is seperated by the "equal to" opperator (e.g. pillow==11.3.0).

#### Installation File Name
It's recomended to update the installation python script file name from install-basic-tkinter-application_1_0_0.py to a name that fits your application.

### Contact
Email: richmantyler73@gmail.com
