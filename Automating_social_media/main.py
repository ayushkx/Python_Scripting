from getpass import getpass
from selenium import webdriver
from time import sleep
import webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import options

user = input("email")
pwd = input("password")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('www.instagram.com')
print("opened insta")
sleep(1)

username_box = driver.find_element_by_id('email')
username_box.send_keys(user)
print("Email entered")

password_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd)
print("passwaord entered")

login_box = driver.find_element_by_id('login')
login_box.click()
print("Login successfully..")

exitSession = input("Enter q to quit session: ")

while(exitSession != 'q'):
    exitSession = input("please enter q to quit: ")

if exitSession == "q" :
    driver.quit()
    print("session over 😊")
