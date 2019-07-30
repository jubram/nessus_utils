# Nessus Utils

This project aims to be a collection of scripts to manipulate the Nessus results files (.nessus).

For some people, it would be useful to run some transformations on Nessus files, in order to perform tests and some tasks; as well to facilitate it analysis.

Right now, it has two manipulation scripts:
* Nessus Transform: it removes random ReportHosts and/or ReportItems from your Nessus files an save into a new file.
* Nessus Split: it splits a big Nessus file into smaller ones. For now, it does this by creating files with at most 50 ReportHosts each.

# How to Use

The scripts are built with Python 3.6. It is recommended to start a new virtual environment and to install the dependencies (```pip install -r requirements.txt```).

After that, you just need to run ```python3.6 nessus_<function>.py```.