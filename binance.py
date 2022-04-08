from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os, time
import random
from selenium.webdriver.chrome.options import Options
from multiprocessing import Pool
  
cwd = os.getcwd()
mobile_emulation = {
    "deviceMetrics": { "width": 360, "height": 650, "pixelRatio": 3.4 },
    }


firefox_options = webdriver.ChromeOptions()
firefox_options.add_argument('--no-sandbox')
 
firefox_options.headless = True
firefox_options.add_argument('--disable-setuid-sandbox')
firefox_options.add_argument('disable-infobars')
firefox_options.add_argument('--ignore-certifcate-errors')
firefox_options.add_argument('--ignore-certifcate-errors-spki-list')

firefox_options.add_argument("--incognito")
firefox_options.add_argument('--no-first-run')
firefox_options.add_argument('--disable-dev-shm-usage')
firefox_options.add_argument("--disable-infobars")
firefox_options.add_argument("--disable-extensions")
firefox_options.add_argument("--disable-popup-blocking")
firefox_options.add_argument('--log-level=3') 
firefox_options.add_argument("--window-size=500,1600")
firefox_options.add_argument('--disable-blink-features=AutomationControlled')
firefox_options.add_experimental_option("useAutomationExtension", False)
firefox_options.add_experimental_option("excludeSwitches",["enable-automation"])
firefox_options.add_experimental_option('excludeSwitches', ['enable-logging'])
firefox_options.add_argument('--disable-notifications')
firefox_options.add_experimental_option("mobileEmulation", mobile_emulation)
random_angka = random.randint(100,999)
random_angka_dua = random.randint(10,99)
def xpath_ex(el):
    element_all = wait(browser,15).until(EC.presence_of_element_located((By.XPATH, el)))
    #browser.execute_script("arguments[0].scrollIntoView();", element_all)
    element_all.click()
    #return browser.execute_script("arguments[0].click();", element_all)

def xpath_long(el):
    element_all = wait(browser,30).until(EC.presence_of_element_located((By.XPATH, el)))
    #browser.execute_script("arguments[0].scrollIntoView();", element_all)
    #return browser.execute_script("arguments[0].click();", element_all) 

def xpath_type(el,word):
    return wait(browser,30).until(EC.presence_of_element_located((By.XPATH, el))).send_keys(word)
def xpath_id(el,word):
    return wait(browser,30).until(EC.presence_of_element_located((By.XPATH, f'//input[@{el}]'))).send_keys(word)
 
  
 
def action(k):
 
    get_url = r"https://testnet.binance.org/faucet-smart"
    
    global browser
    browser = webdriver.Chrome(options=firefox_options, executable_path=f"{cwd}\\chromedriver.exe")
    browser.get(get_url)
   
    xpath_id('class="form-control"',k)
 
    xpath_ex('/html/body/div[1]/div/div[2]/div/div[1]/span[1]/button')
     
  
    xpath_ex('//*[text()="1 BNB"]')  
    sleep(2)
    notify = wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(),"accept") or contains(text(),"until")]'))).text 
    sleep(2)
    print(f"[{k} => {notify}")  
   
if __name__ == '__main__':
    print("[*] Registration Faucet")
 
    jumlah = input("[*] Multiprocessing: ")
    
    file_list_akun = "loop.txt"
    myfile_akun = open(f"{cwd}/{file_list_akun}","r")
    akun = myfile_akun.read()
    list_accountsplit = akun.split()
    k = list_accountsplit
    start = time.time()
    with Pool(int(jumlah)) as p:  
        p.map(action, k)
    