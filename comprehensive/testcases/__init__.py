'''testcases/__init__.py

Defines the package 'testcases' under comprehensive examples folder. This folder
is intended for storing "testcase files": a library of testcases available for
import & usage in actual testscripts.

The goal of the testcases/ folder is to maintain a library of testcase classes &
definitions. This allows testscripts to import and inherit from a common source
as opposed to add-hoc definition of testcases in various scripts, leading to 
potential circular imports.

Testcase files are not intended to be run directly. Rather, they should always
be inherited and provided with & data/parameters before execution. Any libraries
and procedure/functions it references should be imported, from other libraries,
rather than being contained here directly.

Note:
    the usage of testcase files is entirely optional. 

    It is not an AEtest script infrastructure requirement, but rather, a 
    recommended standard to follow in order to produce clearly defined, 
    re-useable & maintainable testscripts.
'''