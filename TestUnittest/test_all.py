#encoding=utf-8
import unittest
from TestUnittest.autoproduction_unittest import  *
from TestUnittest.login_unittest import *

if __name__=='__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(unittest.makeSuite(TestLogin))
    testunit.addTest(unittest.makeSuite(TestAutoProduction))
    runner = unittest.TextTestRunner()
    runner.run(testunit)
