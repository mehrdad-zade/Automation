#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 21:04:01 2020

@author: mehrdadalemzadeh

Torrent search
"""
import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def torrentSites():    
    TorrentSites_list = []
    
    pirate_org = 'https://thepiratebay.org/index.html'
    pirate_org2 = 'https://tpbpirateproxy.org/en'
    pirate_us_org = 'https://thepiratebay.us.org/en/'
    pirate_3 = 'https://thepiratebays3.com/english/'
    pirate_us = 'https://thepiratebay.us.com/en/'
    kickAss_onl = 'https://kickass.onl/'
    eztv_io = 'https://eztv.io/'
    
    
    TorrentSites_list.append(pirate_org)
    TorrentSites_list.append(pirate_org2)
    TorrentSites_list.append(pirate_us_org)
    TorrentSites_list.append(pirate_3)
    TorrentSites_list.append(pirate_us)
    TorrentSites_list.append(kickAss_onl)
    TorrentSites_list.append(eztv_io)
    
    return TorrentSites_list
    
def getChrome():
    driver = webdriver.Chrome()        
    return driver


def search4Movie(driver, url, movie):
    
    try:
        driver.switch_to.window(driver.window_handles[-1])#move to current tab
        text_area = driver.find_element_by_tag_name('input')
        text_area.send_keys(movie)        
        text_area.send_keys(u'\ue007')#mimics the enter key
    except:
        time.sleep(10)        
        #driver.get(url)
        driver.execute_script("window.open('{0}');".format(url))
        text_area = driver.find_element_by_tag_name('input')
        text_area.send_keys(movie)        
        text_area.send_keys(u'\ue007')#mimics the enter key


def searchTorrent(movie):
    #clear the console
    
    clear = lambda: os.system('clear') #on Linux System
    clear()
    
    TorrentSites_list = torrentSites()
    
    driver = getChrome()   
    for url in TorrentSites_list:
        #driver.get(url)   
        driver.execute_script("window.open('{0}');".format(url))#open in new tab
        search4Movie(driver, url, movie)
        #time.sleep(5)   
        
        
movie = sys.argv[1]    
searchTorrent(movie)
        

