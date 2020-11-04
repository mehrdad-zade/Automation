'''
advertizing on Twitter

1. find entities I follow
2. find the latest post on their wall
3. comment under it
4. do this for all

#########
https://www.softwaretestinghelp.com/selenium-webdriver-commands-selenium-tutorial-17/
'''
advertisement = 'Wednesday - Stock Market Brief | Dip Buying :  https://market-brief.blogspot.com/2020/09/wednesday-dip-buying.html'

WSJ = 'https://twitter.com/WSJ'
import time

def openChrome():
    from selenium import webdriver
    driver = webdriver.Chrome()        
    return driver

def findFollowings(driver, myAccount_url):
    following = []
    driver.get(myAccount_url+'/following')
    
    return following
    
def login2Twitter(driver):
    driver.get('https://twitter.com')
    userName = driver.find_element_by_xpath("//*[contains(text(), 'Password')]")
    #userName.click()
    userName.send_keys(Keys.NUMPAD4168247576)
    credentials[1].send_keys('Elearn@6485')    
    driver.find_element_by_xpath("//*[contains(text(), 'Log in')]").click()
    

def comment(driver):
    driver.get(WSJ)
    #time.sleep(10)
    
    svg = driver.find_elements_by_tag_name('svg')
    svg[14].click()
   

def run ():
    myAccount_url = 'https://twitter.com/Mehr6a6'
    from selenium import webdriver
        
    driver = openChrome()
    login2Twitter(driver)
    comment(driver)

run()



