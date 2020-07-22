# pyATS Sample Scripts

The best method to master pyATS test framework is to learn-by-example. This 
repository contains various scripts that showcases the many features and
packages of pyATS.

## General Information

- Website: https://developer.cisco.com/site/pyats/
- Bug Tracker: https://github.com/CiscoTestAutomation/pyats/issues
- Documentation: https://developer.cisco.com/site/pyats/docs/

## Requirements
pyATS & its examples supports Python 3.4+ on Linux & Mac systems. Windows is not yet supported.

## Getting Started

The examples included in this repository expects you to have a Python environment with pyATS packages installed. Alternatively, you can always setup a new virtual environment as sandbox.

```
$ python3 -m venv pyats_sandbox
$ cd pyats_sandbox
$ source bin/activate
$ pip install pyats

$ git clone https://github.com/CiscoDevNet/pyats-sample-scripts.git
```

## Sample Script Usage

There are two ways to run a typical pyATS script:

1. through `pyats run job`, which generates log and archives
2. as standalone, and prints results to screen

```bash
$ cd pyats-sample-scripts/basic

$ pyats run job basic_example_job.py

$ python basic_example_script.py
```

Refer to each job file's docstring on details of command-line arguments.

