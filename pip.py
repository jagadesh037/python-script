#Deploy vpn pod
#Verify the state of pod
#Modify the vpn pod
#Delete the vpn pod
#verify the vpn pod deleted properly

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()

#Enter into webpage
driver.get("https://connect.netsurion.com/login")
