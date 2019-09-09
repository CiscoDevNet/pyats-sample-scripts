'''
Basic Example Job
-----------------

This example shows the basic functionality of pyats with few passing tests.

To run:
    
    cd pyats-sample-scripts/basic
    easypy job/basic_example_job.py

'''

import os
from pyats.easypy import run

def main():
    '''
    main() function is the default easypy job file entry point.
    '''

    # find the location of the script in relation to the job file
    script_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    testscript = os.path.join(script_path, 'basic_example_script.py')

    # execute the testscript
    run(testscript=testscript)
