import webbrowser
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time


try:
	chrome=webdriver.Chrome()
	chrome.get("https://tarif.elvia.ch/direct/start.do?calc=mfz&variante=pw&lang=de")			
    	dp1=chrome.find_element_by_xpath("//*[@id='id6731']/option[text()='2016']").click()
	
	wait = WebDriverWait(chrome, 10)
    	element = wait.until(EC.element_to_be_clickable((By.ID, '8393')))
	dp2=chrome.find_element_by_xpath("//*[@id='8393']/option[text()='BMW']").click()

	wait = WebDriverWait(chrome, 10)
    	element = wait.until(EC.element_to_be_clickable((By.ID, '8440')))
	dp3=chrome.find_element_by_xpath("//*[@id='8440']/option[text()='2er Serie F46 BENZIN Gran Tourer']").click()
	
	wait = WebDriverWait(chrome, 10)
	element = wait.until(EC.element_to_be_clickable((By.ID, 'id6815')))
	dp4=chrome.find_element_by_xpath("//*[@id='id6815']/option[text()='216i Gran Tourer']").click()

    	print "Page is ready!"
except TimeoutException:
	print "Loading took too much time!"

