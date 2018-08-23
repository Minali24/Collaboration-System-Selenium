__author__= 'Minali and Urmi'
import unittest
from decouple import config
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class create_env(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Remote(command_executor='http://'+config('DOCKER_IP')+':'+config('DOCKER_PORT')+'/wd/hub',desired_capabilities=DesiredCapabilities.FIREFOX)#,browser_profile=profile)
		#self.driver = webdriver.Firefox()


	def test_create_community(self):
		driver = self.driver
		# Logging in by admin
		driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT')+"/login")
		print (driver.current_url)
		elem = driver.find_element_by_id("id_username")
		user = config('NOTIFICATION_USER').split(',')
		elem.send_keys(user[3])
		elem = driver.find_element_by_id("id_password")
		elem.send_keys(config('NOTIFICATION_PASSWORD'))
		driver.find_element_by_class_name('btn-block').click()
		# Creating community
		driver.get("http://" + config('IP_ADDRESS') + ":" + config('NOTIFICATION_PORT')+"/create_community")
		print (driver.current_url)
		name ="Test Community abc ABCXYZA"  #community name should not contain numbers
		tag_line= "only meant for testing"
		description= "only meant for testing"
		category= "testing"
		username= "admin"
		elem = driver.find_element_by_id("name")
		elem.send_keys(name)
		elem = driver.find_element_by_id("tag_line")
		elem.send_keys(tag_line)
		elem = driver.find_element_by_id("comm_text_box")
		elem.send_keys(description)
		elem = driver.find_element_by_id("category")
		elem.send_keys(category)
		elem = driver.find_element_by_id("username")
		elem.send_keys(username)
		#element = driver.find_element_by_id("community_image")
		#element.send_keys("/home/anjali/community.jpg")
		element =driver.find_element_by_id("create")
		element.click()
		print (driver.current_url)
		# Extracting the community id
		var = driver.current_url
		community_id = var.split("/")[-2]
		f = open(".env","a")
		f.write("\nNOTIFICATION_COMMUNITY_ID="+community_id)
		f.close()
		
		

	def tearDown(self):
		self.driver.quit()


if __name__ == '__main__':
	unittest.main()

