import os
from selenium import webdriver

chrome_path = r"D:\python\web_automation\chromedriver.exe"
url = "http://www.amazon.com/"   
browser = webdriver.Chrome(chrome_path)
browser.get(url)
# resultsCol

cnt = 0

try:
    input_form = browser.find_element_by_css_selector("input#twotabsearchtextbox.nav-input")
    input_form.send_keys("Asus laptop")

    submit_btn = browser.find_element_by_css_selector("input.nav-input")
    submit_btn.click()
    
    for j in range(30):
        results = browser.find_elements_by_css_selector("h2.a-size-medium.s-inline.s-access-title.a-text-normal")
        prices = browser.find_elements_by_css_selector("span.a-color-base.sx-zero-spacing")        

        for result, price in zip(results, prices):
            cnt += 1
            print(str(cnt) + " : " + result.text[0:10] + \
                  ", " + price.get_attribute("aria-label"))
            
        next_link = browser.find_element_by_css_selector("a#pagnNextLink.pagnNext")
        next_url = next_link.get_attribute("href")
        browser.get(next_url)

except Exception as e:
    browser.quit()
    print(e)
