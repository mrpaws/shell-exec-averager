#!/usr/bin/env python
'''
    sh_exec_avgr.py - Shell Execution Time Averager

       test any set of commands for shell execution times.

       one may override the "tests" attribute with another
       dict of the format:  TestName => shell command
'''
__author__ = 'paws@delimitize.com'

from subprocess import check_output, CalledProcessError
from time import time

class SHTestException(Exception):
    '''general shell execution test exception'''
    pass

class Test:
    def __init__(self, tests={}):
        '''initialize the tests'''
        self.scores = {}
        self.averages = {}
        self.tests = tests
        if not self.tests:
            self.tests = { 
                "bash" : 'echo "Hello World"',
                "perl" : 'perl -e \'print "Hello World\\n";\'',
                "python" : 'python -c \'print "Hello World\\n"\'',
                "java" : 'java hello',
                "ruby" : 'ruby -e \'print "Hello World\\n"\''
            }

    def run(self, test):
        '''run a test'''
        s_time = time()
        try:
            s_time = time()
            check_output(
                test,
                shell=True,
                stdin=None,
                stderr=None,
                universal_newlines=True
            )
            e_time = time()
        except(CalledProcessError):
            print("Warning: Failed a test: {test}.\n".format(test=test))
            raise SHTestException("ERROR: Test failure: {test}".format(test=test))
            return False
        return round((e_time - s_time), 3)

    def sim(self, ntests):
        '''simulate the tests n times, updates the scores dict '''
        for i in range(ntests):
            for x in self.tests:
                res = self.run(self.tests[x])
                if x in self.scores:
                    self.scores[x].append(res)
                else:
                    self.scores[x] = [res]
        return self.scores
            
    def avg(self):
        '''average the scores for each command tested'''
        for x in self.scores:
            its = 0
            sum = 0
            for i in self.scores[x]:
               sum += i
               its += 1
            try:
                self.averages[x] = round((sum / its), 4)
            except(TypeError):
                raise SHExecException("ERROR: Found bad test data while attempting to average.")
                return(False)
        return self.averages

    def test(self, ntests):
       '''high level function to simulate and return averages'''
       raw = self.sim(ntests)
       return self.avg()
        

    ##def __del__(self):
        
