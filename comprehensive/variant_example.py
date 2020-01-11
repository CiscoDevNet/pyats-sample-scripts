#!/bin/env python

'''variant_example.py

This is a comprehensive example variant script. It extends the base_example
script by leveraging a few of its sections & testcases, and adding a few of its
own.

This is called the 'variant' script: it provides varianting (eg, extends, adds 
more to) to the base script. What we're trying to demonstrate here is the use
of inheritances and re-useability of test script codes, etc.

All basic AEtest features are demonstrated in the base script. This variant
script is written assuming the user has a good understanding of how testscript
flows, how various features work, etc. 

Arguments:
    This script requires two script arguments (argument_A and argument_B) to be 
    passed in from the job file for demonstration purposes.

    argument_A: an argument
    argument_B: another argument

Examples:
    # to run under standalone execution
    bash$ python variant_example.py

    # to run under pyats job engine
    bash$ pyats run job job/example_job.py

References:
   For the complete and up-to-date user guide on pyATS, visit:
    https://developer.cisco.com/site/pyats/docs/
'''

#
# optional author information
# 
__author__ = 'Siming Yuan <siyuan@cisco.com>'
__copyright__ = 'Copyright 2017, Cisco Systems'
__email__ = 'pyats-support-ext@cisco.com'
__date__= 'Nov 14, 2017'


#
# import statements
#
import logging
import argparse

from pyats import aetest
from pyats.log.utils import banner

#**********************************
#* Import From Base Script
#*
#*  because this testscript inherits from the base example, it needs to import
#*  testcases/sections from it.
#*  Note that the act of importing testcases and common sections from another
#*  script doesn't actually run it. They need to be locally defined (inherited)
#*  in order for them to take effect.
#*
#*  here, we'll reuse parts of the base_example. so let's import it
import base_example

#**********************************
#* Import From Testcases
#*
#*  importing testcases from the testcase library (under testcases/ folder). 
#*
#*  up to this point we've been focusing on defining testcases directly within
#*  testscripts. This was more intuitive from a training perspective, to teach
#*  content in a linear perspective, building up as we go.
#*
#*  However, whilst this is fine for small-scale scripts for demo purpose, the 
#*  resulting scripts often have have a mix-up of data hard-coding & such, 
#*  leading to testscripts that are difficult to be re-used & extended.
#*
#*  the use of a dedicated testcase library promotes good development habits:
#*  consolidating testcases into a central module, and inheriting whichever 
#*  one you need in your scripts, provide the data & go.
#*
#*  see more @ testcases/__init__.py for details
#*
#*  Note:
#*      the usage of testcase files is entirely optional. 
#*
#*      It is not an AEtest script infrastructure requirement, but rather, a 
#*      recommended standard to follow in order to produce clearly defined, 
#*      re-useable & maintainable testscripts.
from testcases import comprehensive_testcases


#
# create a logger for this module
#
logger = logging.getLogger(__name__)

#**********************************
#* Testscript Parameters
#* 
#*  we can reuse part of, or the entire of the base_example's parameters
#*
#*  for example, let's take a copy of the base_example's testscript parameters,
#*  and extend on top of it.

#
# testscript parameters
#
parameters = base_example.parameters.copy()
parameters.update(variant_parameter_A = 'variant A',
                  variant_parameter_B = 'variant B')


#*******************************************************************************
#* COMMON SETUP SECTION
#* 
#*  instead of defining a whole new CommonSetup section, here we can inherit
#*  the base script's common_setup section, and add/overwrite subsections.
class CommonSetup(base_example.CommonSetup):
    '''Common Setup Section

    This CommonSetup inherits from the base_example.CommonSetup, and adds more
    local subsections to it.

    '''

    @aetest.subsection
    def using_parameters(self, **kwargs):
        '''demonstrating parameter overwriting

        base_example's CommonSetup also has the same 'using_parameters' section.
        This will overwrite it with our own, do extra stuff, then call the
        original one (class inheritance technique).
        '''

        # kwargs contains all parameters
        logger.info('Variant Parameter A: %s' % kwargs['variant_parameter_A'])
        logger.info('Variant Parameter B: %s' % kwargs['variant_parameter_B'])

        # objects are great: call the parent subsection that we defined
        # it's just a method - call it with the proper arguments it requires.
        super().using_parameters(testbed = kwargs['testbed'],
                                 parameter_A = kwargs['parameter_A'],
                                 parameter_B = kwargs['parameter_B'], )

    @aetest.subsection
    def new_subsection_in_variant(self):
        '''New Subsection

        demonstrating that after inheriting the previous CommonSetup, we can add
        more sections to it.
        '''
        logger.info(banner('new subsection is now called'))

#*******************************************************************************
#* TESTCASES
#* 
#*  testcases can also be easily inherited. 
#*  in addition, if you inherit a testcase and then apply loop on it, it will
#*  loop as well.
#*  for this example, we'll use loop uids instead of loop parameters, since the
#*  parent testcase doesn't require parameters
@aetest.loop(uids = ['step_testcase_loop_1', 'step_testcase_loop_2'])
class InheritedStepTestcase(base_example.TestcaseWithSteps):
    '''InheritedStepTestcase

    We are inheriting the parent testcase fully and not making any modifications
    to it.
    '''

    #**********************************
    #* Testcase Groups
    #*
    #*  parent groups are automatically inherited when inheriting testcases.
    #*  this can be overwritten.

    groups = ['group_A', 'group_B', 'group_D']

#*******************************************************************************
#* INHERITING FROM TESTCASE LIBRARY
#*
#*  demonstrating inheriting a testcase from testcases/ testcase library
class DynamicLoops(comprehensive_testcases.DynamicLoopDemonstration):
    '''Dynamic Loops

    Leveraging a testcase defined in comprehensive_testcases library and reusing
    it here. Note that testcase data values needed to be defined in order to
    use this testcase.
    '''

    #**********************************
    #* Testcase Data
    #* 
    #*  this testcase requires two data values to be defined in order to run
    loop_value_one = [123, 456, 789]
    loop_value_two = ['abc', 'def', 'ghi']

    #**********************************
    #* Local Cleanup
    #*
    #*  of course, by the rules of inheritance, we can also create local
    #*  sections.
    @aetest.cleanup
    def cleanup(self):
        pass


#*******************************************************************************
#* LOOPING & INHERITANCE
#*
#*  if you inherit a testcase that was originally looping, the new testcase will
#*  also be looping.
#*
#*  however, you can also overwrite its original loop parameters.
@aetest.loop(a = [5, 6])
class VariantLoopedTestcase(base_example.LoopedTestcase):
    pass

#*******************************************************************************
#* PARAMETERS & INHERITANCE
#*
#*  if a testcase is inherited, its parameters & attributes are also inherited.
#*  you can choose to overwrite them.
#*
class VariantExampleTestcase(base_example.ExampleTestcase):

    uid = 'VariantExampleTestcase'    

    # overwriting parameter defaults
    parameters = {
        'local_A': 'variant default A',
        'local_B': 'variant default B', 
    }
    
    # data can be overwritten
    data_A = base_example.ExampleTestcase.data_A * 10
    data_B = base_example.ExampleTestcase.data_B + ' ' + 'ABC'

    @aetest.cleanup
    def cleanup(self):
        '''Adding cleanup

        Let's add a cleanup Section to this variant testcase
        '''
        pass


class VariantNewTestcase(aetest.Testcase):
    '''Variant New Testcase

    Variant new testcase: this testcase is defined entirely new in this variant
    script.
    '''

    @aetest.setup
    def setup(self):
        pass

    @aetest.test
    def test(self):
        pass

    @aetest.cleanup
    def cleanup(self):
        pass

#*******************************************************************************
#* STANDALONE EXECUTION
#*
#*  this is the same as the base_example. If you feel like this is redundant,
#*  you can create a function to do this mundane work, and call it here.
if __name__ == '__main__':

    #
    # local imports 
    #
    import argparse
    from ats import topology

    #
    # set global loglevel
    #
    logging.root.setLevel('INFO')
    logging.root.setLevel('INFO')

    #
    # local standalone parsing
    #
    parser = argparse.ArgumentParser(description = "standalone parser")
    parser.add_argument('--testbed', dest = 'testbed', 
                        help = 'testbed YAML file',
                        type = topology.loader.load, 
                        default = None)

    # do the parsing
    args = parser.parse_known_args()[0]

    #
    # calling aetest.main() to start testscript run
    #
    aetest.main(testbed = args.testbed)
