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


# Finding the search bar and entering search text
search_bar = driver.find_element("id","text-input-what")
search_bar.send_keys("part time")

# Clicking the Find Jobs button
find_button=driver.find_element("xpath","//button[.='Find jobs']")
find_button.click()

# Waiting for the search results page to load
time.sleep(3)

# Verifying that the search results page has loaded,
assert "Part Time Jobs in Kitchener, ON (with Salaries) 2023 | Indeed.com Canada" in driver.title


#Clicking the first job listed in the search result
first_item= driver.find_element("xpath","//td[@class='resultContent']//a")
first_item.click()
time.sleep(2)

#verify apply button is displayed
apply_link=driver.find_element("xpath","//a[contains(text(),'Apply')]")
apply_link.is_displayed()
print("1.Apply button is displayed")
#time.sleep(10)


#verify that company reviews page is displayed
find_company_reviews=driver.find_element("xpath","//a[@id='CompanyReviews']")
find_company_reviews.is_displayed()
find_company_reviews.click()
assert "Find The Best Companies to Work For | Indeed.com" in driver.title
print("2.Company review tab is displayed")

#verify Find great places to work title is displayed in company review page
great_place=driver.find_element("xpath","//h1[.='Find great places to work']")
great_place.is_displayed()
print("3.Find great places to work title is displayed")

#verify salary guide tab
find_salary_guide=driver.find_element("xpath","//a[@id='FindSalaries']")
find_salary_guide.is_displayed()
find_salary_guide.click()
time.sleep(5)
assert "Salaries | Indeed" in driver.title
print("4.Salary guide page is displayed")
time.sleep(3)

#verify browse top-paying jobs title
top_paying_title= driver.find_element("xpath","//h2[.='Browse top-paying jobs']")
top_paying_title.is_displayed()
time.sleep(5)
print("5.Browse top-paying jobs title is displayed")

#verify sign in button is displayed
sign_in=driver.find_element("xpath","//a[.='Sign in']")
sign_in.is_displayed()
print("6.Sign in button is displayed")

#click on sign in button and verify sign in page is displayed
sign_in.click()
time.sleep(3)
assert "Sign In | Indeed Accounts" in driver.title
driver.back()

#verify upload resume option is displayed
upload_resume=driver.find_element("xpath","//a[@id='UploadYourResume']")
upload_resume.is_displayed()
print("7.Upload resume option is displayed")

#verify post job option is displayed
post_job= driver.find_element("xpath","//a[@id='EmployersPostJob']")
post_job.is_displayed()

#verify post job page is loaded on clicking post job option
post_job.click()
time.sleep(3)
assert "Post a job | Indeed for Employers" in driver.title
driver.back()
print("8.Post job page is loaded")

time.sleep(5)
# Closing the webdriver
driver.close()
driver.quit()