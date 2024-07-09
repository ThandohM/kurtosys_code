from telnetlib import EC
from tkinter.tix import Select
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the web driver
driver = webdriver.Chrome()  # Make sure ChromeDriver is in your PATH

try:
    # SGo to the URL
    driver.get("https://www.kurtosys.com/")
    driver.maximize_window()
    time.sleep(2)  # Wait for the page to load

    # Navigate to "RESOURCES"
    resources_menu = driver.find_element(By.XPATH, '//*[@id="kurtosys-menu-item-75710"]/a/div/div/span')
    resources_menu.click()
    time.sleep(1)  # Wait for the drop-down to appear

    # Click on "White Papers & eBooks"
    white_papers_link = driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div/div/section[2]/div/div/div/div/div/section[1]/div/div/div[3]/div/div/div[2]/div/h4/a')
    white_papers_link.click()
    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[1])
    
    # Navigate to the desired URL in the new tab
    driver.get("https://www.kurtosys.com/white-papers/")
    time.sleep(5)
    #time.sleep(2)  # Wait for the page to load

    # Verify Title reads "White Papers"
    assert "White Papers" in driver.title, "Title does not read 'White Papers'"

   
    white_paper_tile = driver.find_element(By.XPATH, '/html/body/div[2]/div/section[2]/div/div/div/div/div/div/div/div[1]/article[1]/div/div[1]/p/a')  
    white_paper_tile.click()
    time.sleep(5)  # Wait for the page to load

   
    first_name_field = driver.find_element(By.ID, 'form-field-firstname')
    first_name_field.send_keys("John")
    time.sleep(5)
   
    last_name_field = driver.find_element(By.ID, 'form-field-lastname')
    last_name_field.send_keys("Doe")
    time.sleep(5)

  # Fill in "Email"
    Email_field = driver.find_element(By.ID, 'form-field-email')
    Email_field.send_keys("")
    time.sleep(5)

    # Fill in "Company"
    company_field = driver.find_element(By.ID, 'form-field-company')
    company_field.send_keys("VJ Digital")
    time.sleep(5)
    
    # Fill in "Job Title"
    industry_field = driver.find_element(By.ID, 'form-field-jobtitle')
    industry_field.send_keys("Software Tester")
    time.sleep(5)

     # Fill in "Industry"
    select_element = WebDriverWait(driver, 10).until
    EC.presence_of_element_located((By.XPATH, '//*[@id="form-field-industry"]'))
    time.sleep(3)

    select = Select(select_element)
    select.select_by_visible_text("Asset and Investment Management")
    time.sleep(5)
   
    # Step 11: Click "Send me a copy"
    send_copy_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/section/div/div/div/div/div/div/div/div/div/div/section[2]/div/div/div/div/div/section/div/div/div[3]/div/div/div[2]/div/form/div/div[8]/button')
    send_copy_button.click()
    time.sleep(5)  #Wait for the error messages to appear

    
    driver.save_screenshot('error_messages.png')

    # Validate all error messages
    error_messages = driver.find_elements(By.CLASS_NAME, 'error-message') 
    for error in error_messages:
        print(error.text)

finally:
    # Close the browser
    driver.quit()
