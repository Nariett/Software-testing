import unittest
import calc_test

calcTestSuite=unittest.TestSuite()
calcTestSuite.addTest(unittest.makeSuite(calc_test.CalcTest))
calcTestSuite.addTest(unittest.makeSuite(calc_test.CalcExTests))
print("Количество тестов: "+str(calcTestSuite.countTestCases())+"\n")
runner=unittest.TextTestRunner(verbosity=2)
runner.run(calcTestSuite)