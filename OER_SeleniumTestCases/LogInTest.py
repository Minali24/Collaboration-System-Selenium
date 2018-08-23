#!/usr/bin/env python
import unittest
from decouple import config
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class LoginCorrect(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(command_executor='http://'+config('DOCKER_IP')+':'+config('DOCKER_PORT')+'/wd/hub',desired_capabilities=DesiredCapabilities.FIREFOX)#,browser_profile=profile)

    def test_LoginCorrect(self):
        driver = self.driver
        user ="admin"
        pwd= "root1234"
        driver.get("http://"+config('IP_ADDRESS')+":"+config('CONTENT_TOOLS_PORT')+"/login")
        print (driver.current_url)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        driver.find_element_by_class_name('btn-block').click()


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
        unittest.main()
