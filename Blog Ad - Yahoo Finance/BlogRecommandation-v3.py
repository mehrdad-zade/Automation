'''
#install selenium
pip install selenium

#install homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

#install chrome driver
brew cask install chromedriver

#update chrome driver
brew uninstall chromedriver
brew cask install chromedriver
ctr + click + open + open the newly download app then run this program


#find chromedriver in finder and cd to the dir, to make it executable on mac
xattr -d com.apple.quarantine chromedriver 

#test
chromedriver --version


##################

from requests import get
from bs4 import BeautifulSoup
response = get(yahooConversations_DOW)
#print(response.text[:500])
soup = BeautifulSoup(response.text, 'html.parser')
#print(soup.prettify())
print(soup.get_text('share your reaction'))



#extract all urls
for link in soup.find_all('a'):
    print(link.get('href'))
'''    


import time
import sys

def loadData():    
    tickerConversations = []
    
    TEN = 'https://ca.finance.yahoo.com/quote/%5ETNX/community?p=%5ETNX'
    DOW = 'https://ca.finance.yahoo.com/quote/%5EDJI/community?p=%5EDJI'
    NASDAQ = 'https://ca.finance.yahoo.com/quote/%5EIXIC/community?p=%5EIXIC'
    SandP = 'https://ca.finance.yahoo.com/quote/CAD%3DX/community?p=CAD%3DX'
    BTC_CAD = 'https://ca.finance.yahoo.com/quote/BTC-CAD/community?p=BTC-CAD'
    BTC_USD = 'https://ca.finance.yahoo.com/quote/BTC-USD/community?p=BTC-USD'
    RY = 'https://ca.finance.yahoo.com/quote/RY.TO/community?p=RY.TO'
    V = 'https://ca.finance.yahoo.com/quote/V/community?p=V'
    PYPL = 'https://ca.finance.yahoo.com/quote/PYPL/community?p=PYPL'
    GLD = 'https://ca.finance.yahoo.com/quote/GLD/community?p=GLD'
    K = 'https://ca.finance.yahoo.com/quote/K.TO/community?p=K.TO'
    KL = 'https://ca.finance.yahoo.com/quote/KL.TO/community?p=KL.TO'
    CVE = 'https://ca.finance.yahoo.com/quote/CVE.TO/community?p=CVE.TO'
    MSFT = 'https://ca.finance.yahoo.com/quote/MSFT/community?p=MSFT'
    AAPL = 'https://ca.finance.yahoo.com/quote/AAPL/community?p=AAPL'
    GOOG = 'https://ca.finance.yahoo.com/quote/GOOG/community?p=GOOG'
    AMZN = 'https://ca.finance.yahoo.com/quote/AMZN/community?p=AMZN'
    FB = 'https://ca.finance.yahoo.com/quote/FB/community?p=FB'
    SHOP = 'https://ca.finance.yahoo.com/quote/SHOP.TO/community?p=SHOP.TO'
    UBER = 'https://ca.finance.yahoo.com/quote/UBER/community?p=UBER'
    SNOW = 'https://ca.finance.yahoo.com/quote/SNOW/community?p=SNOW'
    U = 'https://ca.finance.yahoo.com/quote/U/community?p=U'
    NVDA = 'https://ca.finance.yahoo.com/quote/NVDA/community?p=NVDA'
    ZM = 'https://ca.finance.yahoo.com/quote/ZM/community?p=ZM'
    WORK = 'https://ca.finance.yahoo.com/quote/WORK/community?p=WORK'
    CSU = 'https://ca.finance.yahoo.com/quote/CSU.TO/community?p=CSU.TO'
    CGX = 'https://ca.finance.yahoo.com/quote/CGX.TO/community?p=CGX.TO'
    TRI = 'https://ca.finance.yahoo.com/quote/TRI.TO/community?p=TRI.TO'
    TSLA = 'https://ca.finance.yahoo.com/quote/TSLA/community?p=TSLA'
    DOL = 'https://ca.finance.yahoo.com/quote/DOL.TO/community?p=DOL.TO'
    GOOS = 'https://ca.finance.yahoo.com/quote/GOOS.TO/community?p=GOOS.TO'
    PLTH = 'https://ca.finance.yahoo.com/quote/PLTH.CN/community?p=PLTH.CN'
    ACB = 'https://ca.finance.yahoo.com/quote/ACB.TO/community?p=ACB.TO'
    APHA = 'https://ca.finance.yahoo.com/quote/APHA.TO/community?p=APHA.TO'
    AAL = 'https://ca.finance.yahoo.com/quote/AAL/community?p=AAL'
    EXPE = 'https://ca.finance.yahoo.com/quote/EXPE/community?p=EXPE'
    BKNG = 'https://ca.finance.yahoo.com/quote/BKNG/community?p=BKNG'
    GRPN = 'https://ca.finance.yahoo.com/quote/GRPN/community?p=GRPN'
    AMD = 'https://ca.finance.yahoo.com/quote/AMD/community?p=AMD'
    SBUX = 'https://ca.finance.yahoo.com/quote/SBUX/community?p=SBUX'
    PINS = 'https://ca.finance.yahoo.com/quote/PINS/community?p=PINS'
    FVRR = 'https://ca.finance.yahoo.com/quote/FVRR/community?p=FVRR'
    SQ = 'https://ca.finance.yahoo.com/quote/SQ/community?p=SQ'
    WIX = 'https://ca.finance.yahoo.com/quote/WIX/community?p=WIX'
    ASML = 'https://ca.finance.yahoo.com/quote/ASML/community?p=ASML'
    BAND = 'https://ca.finance.yahoo.com/quote/BAND/community?p=BAND'
    AC = 'https://ca.finance.yahoo.com/quote/AC.TO/community?p=AC.TO'
    ZNGA = 'https://ca.finance.yahoo.com/quote/ZNGA/community?p=ZNGA'
    NFLX = 'https://ca.finance.yahoo.com/quote/NFLX/community?p=NFLX'
    ADSK = 'https://ca.finance.yahoo.com/quote/ADSK/community?p=ADSK'
    ZM = 'https://ca.finance.yahoo.com/quote/ZM/community?p=ZM'
    TTD = 'https://ca.finance.yahoo.com/quote/TTD/community?p=TTD'
    APPN = 'https://ca.finance.yahoo.com/quote/APPN/community?p=APPN'
    SQQQ = 'https://ca.finance.yahoo.com/quote/SQQQ/community?p=SQQQ'
    ##############high volumes
    GPS = 'https://finance.yahoo.com/quote/GPS/community?p=GPS'
    RKT = 'https://finance.yahoo.com/quote/RKT/community?p=RKT'
    HPQ = 'https://finance.yahoo.com/quote/HPQ/community?p=HPQ'
    HL = 'https://finance.yahoo.com/quote/HL/community?p=HL'
    HST = 'https://finance.yahoo.com/quote/HST/community?p=HST'
    ABEV = 'https://finance.yahoo.com/quote/ABEV/community?p=ABEV'
    CTL = 'https://finance.yahoo.com/quote/CTL/community?p=CTL'
    SPCE = 'https://finance.yahoo.com/quote/SPCE/community?p=SPCE'
    JBLU = 'https://finance.yahoo.com/quote/JBLU/community?p=JBLU'
    JD = 'https://finance.yahoo.com/quote/JD/community?p=JD'
    FSLY = 'https://finance.yahoo.com/quote/FSLY/community?p=FSLY'
    OPK = 'https://finance.yahoo.com/quote/OPK/community?p=OPK'
    HMY = 'https://finance.yahoo.com/quote/HMY/community?p=HMY'
    MRNA = 'https://finance.yahoo.com/quote/MRNA/community?p=MRNA'
    HTHT = 'https://finance.yahoo.com/quote/HTHT/community?p=HTHT'
    APA = 'https://finance.yahoo.com/quote/APA/community?p=APA'
    IMMU = 'https://finance.yahoo.com/quote/IMMU/community?p=IMMU'
    CAG = 'https://finance.yahoo.com/quote/CAG/community?p=CAG'
    VEON = 'https://finance.yahoo.com/quote/VEON/community?p=VEON' 
    ACI = 'https://finance.yahoo.com/quote/ACI/community?p=ACI'
    DOCU = 'https://finance.yahoo.com/quote/DOCU/community?p=DOCU'
    KHC = 'https://finance.yahoo.com/quote/KHC/community?p=KHC'
    IBN = 'https://finance.yahoo.com/quote/IBN/community?p=IBN'
    LB = 'https://finance.yahoo.com/quote/LB/community?p=LB'
    KDP = 'https://finance.yahoo.com/quote/KDP/community?p=KDP'
    AGNC = 'https://finance.yahoo.com/quote/AGNC/community?p=AGNC'
    DHI = 'https://finance.yahoo.com/quote/DHI/community?p=DHI'
    DVN = 'https://finance.yahoo.com/quote/DVN/community?p=DVN'
    SYF = 'https://finance.yahoo.com/quote/SYF/community?p=SYF'
    MYL = 'https://finance.yahoo.com/quote/MYL/community?p=MYL'
    AM = 'https://finance.yahoo.com/quote/AM/community?p=AM'
    ABBV = 'https://finance.yahoo.com/quote/ABBV/community?p=ABBV'
    JNJ = 'https://finance.yahoo.com/quote/JNJ/community?p=JNJ'
    BRK = 'https://finance.yahoo.com/quote/BRK-B/community?p=BRK-B'
    PEAK = 'https://finance.yahoo.com/quote/PEAK/community?p=PEAK'
    NLOK = 'https://finance.yahoo.com/quote/NLOK/community?p=NLOK'
    UA = 'https://finance.yahoo.com/quote/UA/community?p=UA'
    RCL = 'https://finance.yahoo.com/quote/RCL/community?p=RCL'
    
    tickerConversations.append(TEN)
    tickerConversations.append(DOW)
    tickerConversations.append(NASDAQ)
    tickerConversations.append(SandP)
    tickerConversations.append(BTC_CAD)
    tickerConversations.append(BTC_USD)
    tickerConversations.append(RY)
    tickerConversations.append(V)
    tickerConversations.append(PYPL)
    tickerConversations.append(GLD)
    tickerConversations.append(K)
    tickerConversations.append(KL)
    tickerConversations.append(CVE)
    tickerConversations.append(MSFT)
    tickerConversations.append(AAPL)
    tickerConversations.append(GOOG)
    tickerConversations.append(AMZN)
    tickerConversations.append(FB)
    tickerConversations.append(SHOP)
    tickerConversations.append(UBER)
    tickerConversations.append(SNOW)
    tickerConversations.append(U)
    tickerConversations.append(NVDA)
    tickerConversations.append(ZM)
    tickerConversations.append(WORK)
    tickerConversations.append(CSU)
    tickerConversations.append(CGX)
    tickerConversations.append(TRI)
    tickerConversations.append(TSLA)
    tickerConversations.append(DOL)
    tickerConversations.append(GOOS)
    tickerConversations.append(PLTH)
    tickerConversations.append(ACB)
    tickerConversations.append(APHA)
    tickerConversations.append(AAL)
    tickerConversations.append(EXPE)
    tickerConversations.append(BKNG)
    tickerConversations.append(GRPN)
    tickerConversations.append(AMD)
    tickerConversations.append(SBUX)    
    tickerConversations.append(PINS)
    tickerConversations.append(FVRR)
    tickerConversations.append(SQ)
    tickerConversations.append(WIX)
    tickerConversations.append(ASML)
    tickerConversations.append(BAND)
    tickerConversations.append(AC)       
    tickerConversations.append(ZNGA)
    tickerConversations.append(NFLX)
    tickerConversations.append(ADSK)
    tickerConversations.append(ZM)
    tickerConversations.append(TTD)   
    tickerConversations.append(APPN)
    tickerConversations.append(SQQQ)    
    ########high volume ticker adding to the arr
    tickerConversations.append(GPS)
    tickerConversations.append(RKT)
    tickerConversations.append(HPQ)
    tickerConversations.append(HL)
    tickerConversations.append(HST)
    tickerConversations.append(ABEV)
    tickerConversations.append(CTL)
    tickerConversations.append(SPCE)
    tickerConversations.append(JBLU)
    tickerConversations.append(JD)
    tickerConversations.append(FSLY)
    tickerConversations.append(OPK)
    tickerConversations.append(HMY)
    tickerConversations.append(MRNA)
    tickerConversations.append(HTHT)
    tickerConversations.append(APA)
    tickerConversations.append(IMMU)
    tickerConversations.append(CAG)
    tickerConversations.append(VEON)
    tickerConversations.append(ACI)
    tickerConversations.append(DOCU)
    tickerConversations.append(KHC)
    tickerConversations.append(IBN)
    tickerConversations.append(LB)
    tickerConversations.append(KDP)
    tickerConversations.append(AGNC)
    tickerConversations.append(DHI)
    tickerConversations.append(DVN)
    tickerConversations.append(SYF)
    tickerConversations.append(MYL)
    tickerConversations.append(AM)
    tickerConversations.append(ABBV)
    tickerConversations.append(JNJ)
    tickerConversations.append(BRK)
    tickerConversations.append(PEAK)
    tickerConversations.append(NLOK)
    tickerConversations.append(UA)
    tickerConversations.append(RCL)
    return tickerConversations

def getChrome():
    from selenium import webdriver
    driver = webdriver.Chrome()        
    return driver

def postInYahooConversation(driver, advertisement, url):
    retry = 0
    try:
        text_area = driver.find_element_by_tag_name('textarea')
        text_area.send_keys(advertisement)
        submit_button = driver.find_element_by_class_name("comment-submit")
        submit_button.click()
    except:
        print("\nRetry..\n")
        retry += 1
        time.sleep(10)        
        driver.get(url)
        
        text_area = driver.find_element_by_tag_name('textarea')
        text_area.send_keys(advertisement)
        submit_button = driver.find_element_by_class_name("comment-submit")
        submit_button.click()     
    return retry


def run(advertisement):
    #clear the console
    import os
    clear = lambda: os.system('clear') #on Linux System
    clear()
    
    retryCount = 0
    
    tickerConversations = loadData()
    driver = getChrome()   
    t0 = 30
    i = 1
    for url in tickerConversations:   
        driver.get(url)   
        time.sleep(t0) # a gap to login manually 
        print(i, url.split('?p=')[1])#show the ticker name part of the url
        retryCount += postInYahooConversation(driver, advertisement, url)

        t0 = 5
        i += 1
        
    time.sleep(10)
    driver.close()
    
    print('\n', retryCount, " retried URLs : ")#print number of retried URLs



ad = sys.argv[1]
run(ad)
    
    
    
    
    
    

    
    
    
    