import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):
	def setUp(self):
		self.driver=webdriver.Chrome()

	def test_search_in_python_org(self):
		driver=self.driver
		driver.get("https://www.python.org")
		self.assertIn("Python", driver.title)
		time.sleep(5)
		elem=driver.find_element_by_name("q")
		time.sleep(5)
		elem.send_keys("Колледж бизнеса и права")
		time.sleep(5)
		elem.send_keys(Keys.RETURN)
		time.sleep(5)
		self.assertIn("No results found.",driver.page_source)
		time.sleep(5)
		elem=driver.find_element_by_name("q")
		elem.clear()
		time.sleep(5)
		elem.send_keys("pycon")
		time.sleep(5)
		elem.send_keys(Keys.RETURN)
		time.sleep(5)
		self.assertNotIn("No results found.", driver.page_source)

	def test_about_breadcrumbs(self):
		driver=self.driver
		driver.get("https://www.python.org")
		elems=driver.find_elements_by_css_selector('#about ul li a')
		href_list=[]
		name_list=[]
		for e in elems:
			href_list.append(e.get_attribute("href"))
			name_list.append(e.get_attribute('innerHTML'))

		for i in range(len(href_list)-1):
			driver.get(href_list[i])
			elem=driver.find_elements_by_css_selector('.breadcrumbs')
			for e in elems:
				self.assertIn("About",e.get_attribute('innerHTML'))
				self.assertIn(name_list[i],e.get_attribute('innerHTML'))
				time.sleep(3)

	def tearDown(self):
		self.driver.close()

if __name__=='__main__':
	unittest.main()