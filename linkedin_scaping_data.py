from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

website = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
path = r"C:\Users\galih agung raharjo\Documents\web_scraping\chromedriver.exe"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"webdriver.chrome.driver={path}")
driver = webdriver.Chrome(options=chrome_options)

driver.get(website)

wait = WebDriverWait(driver, 10)
input_username = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='username']")))
input_password = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password']")))
signin_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "btn__primary--large")))

input_username.send_keys("galihagung3544@gmail.com")
input_password.send_keys("Kepanjen2020")
signin_button.click()

div_profile_contains = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'feed-identity-module__actor-meta') and contains(@class, 'break-words')]")))
a_element = div_profile_contains.find_element(By.XPATH, ".//a")

a_element.click()

div_profile_entities = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@data-view-name='profile-component-entity']")))

div_profile_entity = div_profile_entities[4]

find_spans = div_profile_entity.find_elements(By.XPATH, ".//span[@class='visually-hidden']")
text_content = ' '.join([span.text for span in find_spans])

data = {'Text Content': [text_content]}
df = pd.DataFrame(data)
df.to_csv('galih_agung_raharjo.csv', index=False)

driver.quit()
