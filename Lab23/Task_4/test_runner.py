import unittest
import calc_test

testLoad=unittest.TestLoader()
suites=testLoad.loadTestsFromName("Тест для калькулятора")
print("Количество тестов: "+str(suites.countTestCases())+"\n")
runner=unittest.TextTestRunner(verbosity=2)
runner.run(suites)