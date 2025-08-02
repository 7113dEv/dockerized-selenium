from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("Test Execution Started")
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=options
)

driver.maximize_window()
time.sleep(5)

driver.get("https://www.browserstack.com/")
time.sleep(5)

driver.find_element(By.LINK_TEXT, "Get started free").click()
time.sleep(5)

driver.close()
driver.quit()
print("Test Execution Successfully Completed!")
