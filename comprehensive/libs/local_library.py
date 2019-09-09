'''local_library.py

This is a local library file that lives with the testscript. Local libraries
contains functions, classes & methods local to a testscript only. Because they
are local and are not shared with other scripts/modules, the use of them should
be minimized (not used if possible). Common code/libraries should be shared with
the testing community in repositories such as xbu_shared.

'''

#
# import statements
#
import logging

#
# create a logger for this module
#
logger = logging.getLogger(__name__)

#**********************************
#* Function & Class Definitions
#*
def function_supporting_step(step):
    '''function_supporting_step

    This function demonstrate the use of steps within function APIs. This
    enables smaller breakdown of functions into smaller steps, and thus provides
    finer granularity in your testscript logs.

    Arguments
    ---------
        steps   (obj): the step object to be passed in from the testscript

    '''

    with step.start('function step one'):
        # do some meaningful testing
        pass

    with step.start('function step two'): 
        # do some meaningful testing
        pass
        
    with step.start('function step three'): 
        # do some meaningful testing
        pass
        
    return