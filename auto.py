from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json


API_response_dict = {}

def login(browser):
	global API_response_dict
	API_response_dict = {}
	login_link = 'https://go.appen.com/users/sign_in'
	my_email = 'kalaborative94@gmail.com'
	my_pw = 'Comput3ch'

	print("[DEV] Logging in...")
	browser.get(login_link)
	# WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, "user-email")))

	browser.find_element_by_id('user_email').send_keys(my_email)
	browser.find_element_by_id('user_password').send_keys(my_pw)
	browser.find_element_by_xpath('//input[@type="submit"]').click()

	WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.ID, "left-navbar-group")))

def go_to_work_page(browser):
	print("[DEV] Going to work page...")
	browser.get('https://gnx.appen.com/#/tasks/3001480/work')

def wait_for_authentication(browser):
	print("[DEV] Waiting for authentication...")
	WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))

def retrieve_major_data(browser):
	print("[DEV] Retrieving major data...")
	browser.get('https://gnx.appen.com/api/1.0/tasks/3001480/work/')
	response = browser.find_element_by_tag_name('pre').text
	response_JSON = json.loads(response)

	print("[DEV] Compiling...")
	transcription_batches = response_JSON["queues"][0]
	maj_tr_hasBatch = transcription_batches['hasBatchAvailable']
	maj_tr_numBatch = transcription_batches['subTask']['numBatches']

	QA_batches = response_JSON["queues"][1]
	maj_qa_hasBatch = QA_batches['hasBatchAvailable']
	maj_qa_numBatch = QA_batches['subTask']['numBatches']

	API_response_dict = {}
	API_response_dict['maj_tr_hasBatch'] = maj_tr_hasBatch
	API_response_dict['maj_tr_numBatch'] = maj_tr_numBatch

	API_response_dict['maj_qa_hasBatch'] = maj_qa_hasBatch
	API_response_dict['maj_qa_numBatch'] = maj_qa_numBatch
	return API_response_dict

def retrieve_minor_data(browser):
	print("[DEV] Done - Retrieving minor data...")
	browser.get('https://gnx.appen.com/api/1.0/tasks/3001490/work/')
	response = browser.find_element_by_tag_name('pre').text
	response_JSON = json.loads(response)



	print("[DEV] Compiling...")
	transcription_batches = response_JSON["queues"][0]
	min_tr_hasBatch = transcription_batches['hasBatchAvailable']
	min_tr_numBatch = transcription_batches['subTask']['numBatches']

	QA_batches = response_JSON["queues"][1]
	min_qa_hasBatch = QA_batches['hasBatchAvailable']
	min_qa_numBatch = QA_batches['subTask']['numBatches']

	API_response_dict['min_tr_hasBatch'] = min_tr_hasBatch
	API_response_dict['min_tr_numBatch'] = min_tr_numBatch

	API_response_dict['min_qa_hasBatch'] = min_qa_hasBatch
	API_response_dict['min_qa_numBatch'] = min_qa_numBatch
	return API_response_dict

def close_browser(browser):
	print("[DEV] Closing browser...")
	browser.quit()

	print("[DEV] Completed")
