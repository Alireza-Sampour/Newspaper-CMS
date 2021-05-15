# pages/test_automation.py
from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

class PlayerFormTest(LiveServerTestCase):

  username='test_user'
  password='12345678'
  email='test_user@test.com'

  def setUp(self):
    User.objects.create_user(self.username, self.email, self.password)
    
  def test_login(self):
    selenium = webdriver.Firefox()
    selenium.get(self.live_server_url+'/login/')
    # login_button = selenium.find_element_by_link_text('Log In')
    # sleep(0.7)
    # login_button.click()
    WebDriverWait(selenium, 15).until(ec.visibility_of_element_located((By.NAME, 'username')))
    # sleep(0.7)
    username = selenium.find_element_by_name('username')
    password = selenium.find_element_by_name('password')
    login_button = selenium.find_element_by_class_name('btn')
    username.send_keys(self.username)
    # # sleep(0.2)
    password.send_keys(self.password)
    # # sleep(0.4)
    password.send_keys(Keys.ENTER)
    sleep(50)


