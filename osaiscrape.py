from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

s = Service("/Users/sophiechiang/Downloads/chromedriver")

driver = webdriver.Chrome(service=s)
url = "https://deep.osai.ai/#/tokio2020/581?sign=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJnYW1lX2lkIjo1ODEsImxvY2F0aW9uIjoiaHR0cHM6Ly9kZWVwLm9zYWkuYWkvIy9zaGFyZS81ODEiLCJleHBpcmVzIjoxNjMxMjczMjcyLjgyNjk0NX0.Q2esYy_LChHwzXEg6GjN0pzN9ZIooGfxpZvBlG5VbTc"
url = "https://tokyo2020.osai.ai/"

driver.get(url)
print(driver.page_source)
# driver.find_element_by_class_name("item").click()

"""
try:
    login = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (
                By.CLASS_NAME,
                "text-body-1 text--primary ml-0 v-btn v-btn--block v-btn--is-elevated v-btn--has-bg theme--light elevation-1 v-size--default secondary lighten-1",
            )
        )
    )
    login.click()
    # title = login.find_element_by_class_name("text-h3 mb-5")
    # print(title.text)
    # link = driver.find_element_by_link_text("Sign in")
    # link.click()

except:
    print("not found")
    driver.quit()
"""

# search = driver.find_element_by_id("input-421")
# search.send_keys("schiang@perse.co.uk")
# search.send_keys(Keys.RETURN)
# time.sleep(5)

# driver.quit()
