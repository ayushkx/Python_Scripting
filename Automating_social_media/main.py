#importing selenium module to handle browser activity , getpass to get secure password and time module to delay
from getpass import getpass
from selenium import webdriver
from time import sleep
import webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

#taking user credentials
user = input("email")
pwd = input("password")

#using options function for headless automation and fast process
chrome_options = Options()

chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

#initiate the chrome driver and open the url
driver = webdriver.Chrome(ChromeDriverManager().install() , options=chrome_options)
driver.get('www.instagram.com')
print("opened insta")
sleep(1)

#find the user email box using find_element_by_id function and provinding user email by send_keys
username_box = driver.find_element_by_id('email')
username_box.send_keys(user)
print("Email entered")

#find the user password box using find_element_by_id function and provinding user password by send_keys
password_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd)
print("passwaord entered")

#clicking on the login button
login_box = driver.find_element_by_id('login')
login_box.click()
print("Login successfully..")

#exit the session using quit()
exitSession = input("Enter q to quit session: ")

while(exitSession != 'q'):
    exitSession = input("please enter q to quit: ")

if exitSession == "q" :
    driver.quit()
    print("session over 😊")
