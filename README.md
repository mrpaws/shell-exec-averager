shell-exec-averager
===================

runs a specified number via a shell spawned from python's subprocess module to perform timing simulations on a dictionary of the form 'testname => shell command"


>> from sh_exec_avgr import Test
>> cmds = {"detailed_listing" : "ls -l", "hidden_listing" : "ls -a" }
>> x = Test(cmds)
>> x.test(5)

{'detailed_listing': 0.0022, 'hidden_listing': 0.002}


