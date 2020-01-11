'''
Basic Example Script
--------------------

A very simple test script example which include:
    common_setup
    testcases
    common_cleanup

The purpose of this sample test script is to demonstrate
"hello world" in aetest.

You can run this script directly as:
    $ python basic_example_script.py
'''

import logging

from pyats import aetest

# get your logger for your script
log = logging.getLogger(__name__)

class common_setup(aetest.CommonSetup):
    '''Common Setup Section

    Each script may only have a single common setup section. 
    Common setup section is always run as the first section in a test script,
    and serves to perform all the "common" setups required for your script.

    Define a common setup section by subclassing aetest.CommonSetup class. 
    It's a good convention to name it 'common_setup', as this section's
    reporting ID is always 'common_setup'.

    Each common setup may have 1+ subsections. Consider a subsection as a 
    setup 'milestone/step'. A subsection is defined using @aetest.subsection
    decorator on a method.
    '''

    @aetest.subsection
    def subsection_1(self):
        '''example subsection one'''
        log.info('hello world!')
        

    @aetest.subsection
    def subsection_2(self, section):
        '''
        if the special 'section' keyword argument is defined in the subsection
        method, the current running subsection will be passed in.
        '''
        log.info("inside %s" % (section))


class Testcase_One(aetest.Testcase):
    '''Testcases

    Testcases are the bread and butter of test automation. Each testcase should
    be a self-contained individual unit of testing, and are independent from
    other testcases (eg, testcases should be runnable out-of-order).

    Define a testcase by subclassing from aetest.Testcase and provide a 
    meaningful class name - this will be used as the testcase's reporting ID.

    Each testcase may contain:
        - 1 x setup section
        - n x tests section
        - 1 x cleanup section
    
    Within each testcase, the class instance is perserved and reused for each
    section execution. Eg: self points to the same instance while this testcase
    runs. This is an important property of AEtest testcases.
    '''

    @aetest.setup
    def setup(self, section):
        '''setup section

        create a setup section by defining a method and decorating it with
        @aetest.setup decorator. The method should be named 'setup' as good
        convention.

        setup sections are optional within a testcase, and is always runs first.
        '''
        log.info("%s testcase setup/preparation" % self.uid)

        # set some variables
        self.a = 1
        self.b = 2

    @aetest.test
    def test_1(self, section):
        '''test section

        create a test section by defining a method and decorating it with
        @aetest.test decorator. The name of the method becomes the unique id
        labelling this test. There may be arbitrary number of tests within a 
        testcase.

        test sections run in the order they appear within a testcase body.
        '''
        log.info("test section: %s in testcase %s" % (section.uid, self.uid))

        # testcase instance is preserved, eg
        assert self.a == 1

    @aetest.test
    def test_2(self, section):
        '''
        you can also provide explicit results, reason and data using result API.
        These information will be captured in the result summary.
        '''
        log.info("test section: %s in testcase %s" % (section.uid, self.uid))

        if self.b == 2:
            self.passed('variable b contains the expected value',
                        data = {'b': self.b})
        else:
            self.failed('variable b did not contains the expected value',
                        data = {'b': self.b})
            
    @aetest.cleanup
    def cleanup(self):
        '''cleanup section

        create a cleanup section by defining a method a decorating it with
        @aetest.cleanup decorator. This method should be named 'cleanup' as good
        convention.

        cleanup sections are optional within a testcase, and is always run last.
        '''
        log.info("%s testcase cleanup/teardown" % self.uid)

class common_cleanup(aetest.CommonCleanup):
    '''Common Cleanup Section

    Each script may only have a single common cleanup section. 
    Common cleanup section is always run as the last section in a test script,
    and serves to perform all the "common" cleanups required for your script.

    In addition, common-cleanup section should act as the safety net: in case
    of dramatic testcase failures, common cleanup section should be able to
    cleanup the lingering mess left behind in the testbed/devices under test.

    Define a common cleanup section by subclassing aetest.CommonCleanup class. 
    It's a good convention to name it 'common_cleanup', as this section's
    reporting ID is always 'common_cleanup'.

    Similar to its counterpart, common cleanup may have 1+ subsections. 
    Consider a subsection as a cleanup 'milestone/step'. A subsection is defined
    using @aetest.subsection decorator on a method.
    '''

    # CommonCleanup follow exactly the same rule as CommonSetup regarding
    # subsection 
    # You can have 1 to as many subsection as wanted
    # here is an example of 1 subsections

    @aetest.subsection
    def clean_everything(self):
        '''one subsection for simplicity'''

        log.info('goodbye world')

if __name__ == '__main__':
    # standard boilerplate entrypoint if the script is run standalone
    # as python basic_example_script.py

    # perform any necessary setup here, eg, parse args.
    # ...

    # finally, call aetest.main() to start script execution
    aetest.main()
