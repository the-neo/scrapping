from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import getpass

	driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
	detail_link = []

def login_and_search():	                                         

	linkedin_id = input("Enter Linkedin ID: ")
	passkey = getpass.getpass("Password: ")
	print('Logging in Linkedin...')

	driver.get('https://www.linkedin.com/uas/login?_l=en')

	driver.maximize_window()

	email = driver.find_element_by_xpath('//*[@id="session_key-login"]')  
	email.send_keys(linkedin_id)

	time.sleep(3)

	password = driver.find_element_by_xpath('//*[@id="session_password-login"]') 
	password.send_keys(passkey)

	time.sleep(3)

	login = driver.find_element_by_xpath('//*[@id="btn-primary"]')  
	login.click()

	time.sleep(5)

	info = input("Enter text to be searched: ")

	search = driver.find_element_by_xpath('//*[@id="ember997"]/input') 
	search.send_keys(info)

	time.sleep(3)
	search.sendKeys(Keys.ENTER);
	# button = driver.find_element_by_xpath('/html/body/nav/div/form/div/div/div/artdeco-typeahead-deprecated/artdeco-typeahead-deprecated-input/input')
	# button.click()  

	time.sleep(3)

	people = driver.find_element_by_xpath('//*[@id="ember5026"]/ul/li[1]/button') 
	people.click() 

	time.sleep(10)

	return driver



def get_detail_link(driver):

	soup = BeautifulSoup(driver.page_source, 'lxml')	
	i=1

	for a in soup.find_all('a', class_ = 'result-image'):
		print (str(i) + ')  https://www.linkedin.com' + a['href'])
		detail_list.append('https://www.linkedin.com' + a['href'])
		i+=1
	

def get_public_profile_information():


	i = input("Enter corresonding # for details: ")
	url=detail_link[i-1]
	driver.get(url)

	soup = BeautifulSoup(driver.page_source,'lxml')

	# print soup.text
	print soup.find('h1', class_='pv-top-card-section__name Sans-26px-black-85%').text
	print soup.find('h2', class_='pv-top-card-section__headline mt1 Sans-19px-black-85%').text
	edu = soup.find('img', class_='pv-top-card-v2-section__entity-logo-img EntityPhoto-square-5')
	print edu['alt']
	
	info = driver.find_element_by_xpath('//*[@id="ember1586"]/span[2]') 
	info.click() 
	print soup.find_element_by_xpath(//*[@id="ember2513"]/div/section[2]/div/a).text

	

	print '\n'

########################################### MAIN ###################################



get_detail_link(login_and_search())
get_public_profile_information()


driver.quit()

####################################################################################