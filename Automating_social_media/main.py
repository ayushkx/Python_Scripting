#importing selenium module to handle browser activity , getpass to get secure password and time module to delay
import os

try:
    from getpass import getpass
    from selenium import webdriver
    from time import sleep
    import webdriver_manager
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.options import Options
except ModuleNotFoundError:
    os.system('pip install -r requirements.txt')
    os.system('python -m pip install --upgrade pip')
    print("\n\n\n\nPlease Restart this Software\n\n\n\nThanks for your Co-operation")
    exit()

#taking user credentials
user = input("username")
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
username_box = driver.find_element_by_id('username')
username_box.send_keys(user)
print("username entered")

#find the user password box using find_element_by_id function and provinding user password by send_keys
password_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd)
print("passwaord entered")

#clicking on the login button
login_box = driver.find_element_by_id('login')
login_box.click()
print("Login successfully..")


def uploadToInstagram(Image , description,username):
    browser.find_element(By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div").click()
    time.sleep(5)
    browser.get(f'https://instagram.com/{username}')
    time.sleep(5)
    browser.find_element(By.CSS_SELECTOR, '[aria-label="New post"]').click()
    browser.find_element(By.XPATH, '//*[@id="mount_0_0_AM"]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div/div/div/div/div[2]/div[1]/form/input').send_keys(Image)

    time.sleep(200)

    browser.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[3]/div/button").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[3]/div/button").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/textarea").send_keys(description)
    time.sleep(2)
    browser.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[3]/div/button").click()
    time.sleep(2)
    
    ImageUploaded = False
    while ImageUploaded == False:
        try:
            myElem = browser.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div/div/div[2]/div[1]/div/img").click()
            ImageUploaded = True
        except:
            time.sleep(5)
            ImageUploaded = False
    time.sleep(5)




#exit the session using quit()
exitSession = input("Enter q to quit session: ")

while(exitSession != 'q'):
    exitSession = input("please enter q to quit: ")

if exitSession == "q" :
    driver.quit()
    print("session over 😊")
