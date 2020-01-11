# Comprehensive Example

This is a comprehensive example written to showcase pyATS AEtest features. 
This example is typically automatically copied into your pyATS instance as part
of the installation process.

The goal of this example is to demonstrate the following basics:

    - how AEtest works: features & flow
    - writing a straighforward, basic testscript:
        - script components and structure
        - various script features
    - script inheritance & variance
    - driving testscript with data/parameters
    - passing arguments from jobfile/commandline into the testscript.
    - importing local libraries & etc.

and is written to be self-explanatory. It is intended to act as a semi-guide,
walking users through important features and explaining them using live
examples, supplementing the full user guide at:
    https://developer.cisco.com/site/pyats/docs/

This example is executable both under standalone execution, and through 
pyATS command line `pyats run job`. You can modify parts of this code to see 
how it changes execution behaviors.

```
    Folder Structure
    ----------------
        pyats-sample-scripts/comprehensive/
        |-- README.md
        |-- base_example.py
        |-- variant_example.py
        |-- job
        |   `-- example_job.py
        |-- etc
        |   `-- example_testbed.yaml
        |-- testcases
        |   |-- __init__.py
        |   `-- comprehensive_testcases.py
        `-- libs
            |-- __init__.py
            `-- local_library.py
```

Each file listed above contains appropriate headers describing their usages.


## Usages

```bash
$ cd pyats-sample-scripts/comprehensive/

# standalone execution
# --------------------
$ python base_example.py --testbed etc/example_testbed.yaml
$ python variant_example.py --testbed etc/example_testbed.yaml

# pyats job execution
# -------------------
$ pyats run job job/example_job.py --testbed-file etc/example_testbed.yaml
```