from selenium import webdriver
import time
driver=webdriver.Chrome("D:\\chromedriver.exe")
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSd3PZLvGWrGgEjGiSfWrnRr4ZW9jqZPbRTj9B2bnlzOOIOZJA/viewform")

# wait for one second, until page gets fully loaded
time.sleep(1)
 
# Data
datas = [
    ['ROhan', 'rohaniuru@gmail.com', '4079025063',
        '2474   bait,Maitland', 'NA'],
    [' Vikas', '        Viaks@gmail.com',
        '3153437575', 'old , NA', 'NA'],
]
 
# Iterate through each data
for data in datas:
    # Initialize count is zero
    count = 0
    textboxes = driver.find_elements_by_class_name(
        "quantumWizTextinputPaperinputInput")
 
    # contain textareas
    textareaboxes = driver.find_elements_by_class_name(
        "quantumWizTextinputPapertextareaInput")
 
    # Iterate through all input boxes
    for value in textboxes:
        # enter value
        value.send_keys(data[count])
        # increment count value
        count += 1
 
    # Iterate through all textareas
    for value in textareaboxes:
        # enter value
        value.send_keys(data[count])
        # increment count value
        count += 1

    # click on submit button
    submit = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    submit.click()
 
    # fill another response
    another_response = driver.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_response.click()

driver.quit()


