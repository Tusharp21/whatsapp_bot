from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="S:\my tutorial\selenium\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://web.whatsapp.com/")


def msg():
    name = input('\n enter group/user name: ')
    message = input("enter your message to group/user: ")
    # Count = int(input("enter the message count: "))

    # Find whom to message
    user = driver.find_element(By.XPATH,  '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
    user.send_keys(name)
    user.send_keys(Keys.ENTER)

    text_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p' )#"/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]")
    text_box.send_keys(message)
    text_box.send_keys(Keys.ENTER)

driver.implicitly_wait(20)
msg()
