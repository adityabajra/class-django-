from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5500/index.html")
    driver.find_element(By.NAME, "username").send_keys("Bidur")
    driver.find_element(By.NAME, "password").send_keys("pass123")
    driver.find_element(By.ID, "login-button").click()
   
   
    message = driver.find_element(By.ID, "welcome").text
    assert 'Welcome test user' in message 
    
    driver.quit()

