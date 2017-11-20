from selenium import webdriver
import time

#selenium test
def seleniumTest(i):
    print(i)

    browser = webdriver.Firefox()

    browser.get('youtube/site/you/want/to/inflate/')
    #time is in seconds, change it to suit your internet connection and video size.
    time.sleep(180)
    browser.quit()
    

for i in range(100):
    
    seleniumTest(i)
    
print("DONE")
