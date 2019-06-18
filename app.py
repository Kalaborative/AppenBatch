from flask import Flask, render_template, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from auto import login, go_to_work_page, wait_for_authentication, retrieve_major_data, retrieve_minor_data, close_browser
from os import environ

app = Flask(__name__)
browser = ""
data_dict = {}

@app.route('/')
def index():
	return render_template('index.html')

@app.route("/api-update-1")
def api_update_1():
	global data_dict
	data_dict = {}
	chrome_options = Options()
	chrome_options.binary_location = environ.get('GOOGLE_CHROME_BIN')
	chrome_options.add_argument('--disable-gpu')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("log-level=3")
	global browser
	browser = webdriver
	browser = browser.Chrome(executable_path=str(environ.get('CHROMEDRIVER_PATH')), chrome_options=chrome_options)
	browser.implicitly_wait(10)
	login(browser)
	return jsonify({'progress': 17})

@app.route('/api-update-2')
def api_update_2():
	go_to_work_page(browser)
	return jsonify({'progress': 33})

@app.route('/api-update-3')
def api_update_3():
	wait_for_authentication(browser)
	return jsonify({'progress': 50})

@app.route('/api-update-4')
def api_update_4():
	response = retrieve_major_data(browser)
	data_dict.update(response)
	return jsonify({'progress': 67})

@app.route('/api-update-5')
def api_update_5():
	response = retrieve_minor_data(browser)
	data_dict.update(response)
	return jsonify({'progress': 83})

@app.route('/api-update-6')
def api_update_6():
	close_browser(browser)
	return jsonify(data_dict)

if __name__ == "__main__":
	# convention to run on Heroku
	port = int(environ.get("PORT", 5000))
	# run the app available anywhere on the network, on debug mode
	app.run(host="0.0.0.0", port=port)
	# app.run(debug=True)
