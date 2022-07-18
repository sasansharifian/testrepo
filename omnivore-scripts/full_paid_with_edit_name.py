from asyncore import loop
#from http.client import ACCEPTED
import webbrowser
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.alert import Alert
import pytest

def test_qr():
    global driver
    driver = webdriver.Chrome('/home/sasan/Documents/Python/chromedriver')
    #Run Test With One Participant [Full Paid with Tip]
    location = ('https://app-staging.qlub.cloud/qr/ae/omnivore-sasan/17/_/_/1a184b2835')
    driver.get(location)
    sleep(15)


def test_fetch_order(): 
    #Fetch Order
    driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div/div[3]/div').click()
    sleep(15)


def test_split():    
    #Open Split Section
    driver.find_element(By.XPATH, '//*[@id="split-bill"]').click()
    sleep(4)


def test_edit_name():    
    #Edit Name
    driver.find_element(By.XPATH, '//*[@id="name"]').send_keys('Sasan Sharifian')
    sleep(4)


def test_tip(): 
    driver.find_element(By.CLASS_NAME, "Tips_tipLabel__FJ_Dg").click()    
    sleep(5)
    #Enter Visa Card Number


def test_checkout():    
    driver.switch_to.frame("cardNumber")
    driver.find_element(By.XPATH, '//*[@id="checkout-frames-card-number"]').send_keys('4242424242424242')
    driver.switch_to.default_content()
    sleep(2)
    #Enter ExirayDate
    driver.switch_to.frame("expiryDate")
    driver.find_element(By.XPATH, '//*[@id="checkout-frames-expiry-date"]').send_keys('1030')
    driver.switch_to.default_content()
    sleep(1)
    #Enter Cvv
    driver.switch_to.frame("cvv")
    driver.find_element(By.XPATH, '//*[@id="checkout-frames-cvv"]').send_keys('100')
    driver.switch_to.default_content()
    sleep(3)


def test_pay():    
    #Click On Pay Now
    driver.find_element(By.XPATH, '//*[@id="checkout-action-btn"]').click()
    sleep(15)



def test_email():    
    driver.find_element(By.NAME, "email").send_keys("sasan@qlub.io")
    sleep(2)
    #Click On Send
    driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div/div[2]/form/div/div[2]/div/div/div/button').click()
    sleep(2)

    
def test_finish():
    driver.quit()
    print('Successful Test')