import webbrowser
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import openpyxl


#--------------- Start Excel -----------------#
wb = openpyxl.Workbook()
wb = openpyxl.load_workbook(filename='policies.xlsm')
sheets = wb.sheetnames
ws = wb[sheets[0]]
#--------------- End Excel -------------------#
try:
	#----------------- Read Excel -----------------#
	for row in ws.iter_rows('S{}:S{}'.format(2,100)):
        	#--------------- Start Web Driver ------------#
       		chrome=webdriver.PhantomJS()
        	chrome.get("https://tarif.elvia.ch/direct/start.do?calc=mfz&variante=pw&lang=de")
        	#--------------- End Web Driver --------------#
        	#--------------- Start WaitDrive -------------#
        	prit = WebDriverWait(chrome,10)
        	#--------------- End WaitDrive ---------------#
		for cell in row:
        		
			print(cell.value)
			cell_S = cell.value	
  			
			#dp1=chrome.find_element_by_xpath("//*[@id='id6731']/option[text()='2016']").click()
			#element = prit.until(EC.element_to_be_clickable((By.ID, '8393')))
			#dp2=chrome.find_element_by_xpath("//*[@id='8393']/option[text()='BMW']").click()
			#element = prit.until(EC.element_to_be_clickable((By.ID, '8440')))
			#dp3=chrome.find_element_by_xpath("//*[@id='8440']/option[text()='2er Serie F46 BENZIN Gran Tourer']").click()
			#element = prit.until(EC.element_to_be_clickable((By.ID, 'id6815')))
			#dp4=chrome.find_element_by_xpath("//*[@id='id6815']/option[text()='216i Gran Tourer']").click()
	    		#element = prit.until(EC.element_to_be_clickable((By.ID,'1730')))
	    		#chrome.find_element_by_xpath("//*[@id='1730']").click()
		
			element = prit.until(EC.element_to_be_clickable((By.ID,'8535')))
			search = chrome.find_element_by_xpath("//*[@id='8535']")
			search.clear()
			search.send_keys(cell_S)
		
			chrome.find_element_by_xpath("//*[@id='8572']").click()
    		
			element = prit.until(EC.element_to_be_clickable((By.ID,'10406')))
			if element.text == "0Treffer":
				print "No Data"
				print ("-------------------------->")
			else:
				chrome.find_element_by_xpath("//*[@id='1730']").click()
                		#print("1st Page Finished")			

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
                  		#print("2nd Page Finished")

				
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

                    		#print("3rd Page Finished!!!")
                    		chrome.find_element_by_xpath("//*[@id='1730']").click()

                		element = prit.until(EC.element_to_be_clickable((By.ID,'1730')))
                    		chrome.find_element_by_xpath("//*[@id='1730']").click()

                    		element = prit.until(EC.element_to_be_clickable((By.ID,'id4861')))
                    		haft = chrome.find_element_by_xpath("//*[@id='id4861']")

                    		teil = chrome.find_element_by_xpath("(//*[@id='id4861'])[2]")
                    		print("Haftpflicht : "+haft.text +" CHF")
                		print("Teilkasko :"+teil.text +" CHF")

                		chrome.find_element_by_name("I9.checked").click()        
                    		element = prit.until(EC.element_to_be_clickable((By.ID,'id4861')))
                    		vol = chrome.find_element_by_xpath("(//*[@id='id4861'])[2]")
                		print("Vollkasko :"+ vol.text +" CHF")
                		print("-------------------------")
		chrome.close()
	print "Done"
except TimeoutException:
	print "Loading took too much time!"

