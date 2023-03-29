#importing required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Indeed Canada homepage
driver.get("https://ca.indeed.com/")
time.sleep(3)
driver.maximize_window()


#verify that Find Jobs button is displayed
find_job_option=driver.find_element("id","FindJobs")
find_job_option.is_displayed()
#
find_company_reviews=driver.find_element("id","CompanyReviews")
find_company_reviews.is_displayed()


# Finding the search bar and entering search text
search_bar = driver.find_element("id","text-input-what")
search_bar.send_keys("part time")

# Clicking the Find Jobs button
find_button=driver.find_element("xpath","//button[.='Find jobs']")
find_button.click()


# Waiting for the search results page to load
time.sleep(5)

# Verifying that the search results page has loaded,
assert "Part Time Jobs in Kitchener, ON (with Salaries) 2023 | Indeed.com Canada" in driver.title
time.sleep(3)

#Clicking the first job listed in the search result
first_item= driver.find_element("xpath","//td[@class='resultContent']//a")
first_item.click()
time.sleep(5)

#click on apply button
apply_link=driver.find_element("xpath","//a[contains(text(),'Apply')]")
apply_link.click()
time.sleep(20)

# Closing the webdriver
driver.close()
driver.quit()