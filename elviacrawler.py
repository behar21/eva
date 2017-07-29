import webbrowser
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys


try:
	chrome=webdriver.PhantomJS()
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
    	
	wait = WebDriverWait(chrome,10)
	element = wait.until(EC.element_to_be_clickable((By.ID,'1730')))
 	table_buttons = chrome.find_elements_by_xpath("//*[@id='1730']")
    	
	
	prit = WebDriverWait(chrome,10)
	try:
        
		element = prit.until(EC.element_to_be_clickable((By.ID,'1730')))
		chrome.find_element_by_xpath("//*[@id='1730']").click()
		print("1st Page Finished")

		#-------Go to 2nd Page -------------
        
		element = prit.until(EC.element_to_be_clickable((By.ID,'id8214')))
		chrome.find_element_by_xpath("//*[@id='id8214']/option[text()='AG']").click()
	
		kontrollschild = chrome.find_element_by_xpath("//*[@id='id9108']")
		kontrollschild.clear()
		kontrollschild.send_keys("123456")
		
		inverkehrestzung = chrome.find_element_by_xpath("//*[@id='id9116']")
		inverkehrestzung.clear()
		inverkehrestzung.send_keys("28.07.2017")

		chrome.find_element_by_xpath("//*[@id='id2640']/option[text()='kein Leasing']").click()
		print("2nd Page Finished")
        
		#------- Got  to 3rd Page ------------
		chrome.find_element_by_xpath("//*[@id='1730']").click()


		element = prit.until(EC.element_to_be_clickable((By.ID,'id10558')))
        	fuhrerausweis = chrome.find_element_by_xpath("//*[@id='id10558']")
        	fuhrerausweis.clear()
        	fuhrerausweis.send_keys("02.02.2017")
            
        	plz = chrome.find_element_by_xpath("//*[@id='id1001001']")
        	plz.clear()
        	plz.send_keys("4016")
		chrome.find_element_by_xpath("//*[@id='id10558']").click()

		element = prit.until(EC.element_to_be_clickable((By.ID,'id1744')))
        	jahr = chrome.find_element_by_xpath("//*[@id='id1744']")
       		jahr.clear()
		jahr.send_keys("5") 
                
        	birthdate = chrome.find_element_by_xpath("//*[@id='8120']")
            	birthdate.clear()
            	birthdate.send_keys("28.01.1993")
		chrome.find_element_by_xpath("//*[@id='id10558']").click()
		
		#element = prit.until(EC.element_to_be_clickable((By.ID,'id3348')))
		#chrome.find_element_by_xpath("//*[@id='id3348']/option[text()='B (Aufenthalt)']").click()
				
		print("3rd Page Finished!!!")		
		chrome.find_element_by_xpath("//*[@id='1730']").click()
		
		element = prit.until(EC.element_to_be_clickable((By.ID,'1730')))
		chrome.find_element_by_xpath("//*[@id='1730']").click()

		element = prit.until(EC.element_to_be_clickable((By.ID,'id100071')))
		total = chrome.find_element_by_xpath("//*[@id='id100071']")
		print("Total : "+total.text +" CHF")
	except TimeoutException:
		print("Ahh damn it!!!")
		

except TimeoutException:
	print "Loading took too much time!"

