shell-exec-averager
===================

Runs specified number of timing simulations on various shell commands specified by a python dict. A shell is spawned by python's subprocess module which times the executon of the given shell commands, aggregates the data and obtains averages. Dict is of the form {'testname' => 'shell command'}. Useful for relative testing of any code types (as the shell can easily expand files, etc.).

Example:

from sh_exec_avgr import Test
cmds = {"detailed_listing" : "ls -l", "hidden_listing" : "ls -a" }
x = Test(cmds)
x.test(5)

{'detailed_listing': 0.0022, 'hidden_listing': 0.002}


