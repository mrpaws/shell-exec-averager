shell-exec-averager
===================

Runs specified number of timing simulations on various shell commands specified by a python dict. A shell is spawned by python's subprocess module which times the executon of the given shell commands, aggregates the data and obtains averages. Dict is of the form {'testname' => 'shell command'}. Useful for relative testing of any code types (as the shell can easily expand files, etc.).  

Beware of the default dictionary.

Example:

> from sh_exec_avgr import Test

> cmds = {"detailed_listing" : "ls -l", "hidden_listing" : "ls -a" }

> x = Test(cmds)

> x.test(5)

{'detailed_listing': 0.0022, 'hidden_listing': 0.002}


Example (no arg):
> from sh_exec_avgr import Test

> y = Test()

> y.test(100)


{'python': 0.0583, 'ruby': 0.0593, 'java': 0.1137, 'bash': 0.0459, 'perl': 0.0477}



