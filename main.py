import requests, json, time
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright


global_appointment_cache = []


def filter_data(data: "html") -> "appintment array":

	# Create array for the appointments
	appointment_array = []

	# Start working with the data
	data_split = data.split("AvaialbleAppointmentsResult")[1].split("AvaialbleCalendarResult")[0].replace("\n", "").replace(" ", "").replace("\r", "")
	if "noappointmentisavailableforyoursearch" in data_split.lower():
		return None
	else:
		for appointment in data_split.split("data-date"):

			# Create an object for the indivigual appointment
			appointment_object_ind = {} 

			first_split = appointment.replace(r"\r", " ").replace(r"\n", " ").split("=\\")

			# Set all of the variables equal to none

			start_time, end_time, date, education_center_id, appointment_type, day_of_the_week, appointment_id = None, None, None, None, None, None, None
			for section in first_split:
				section = section.replace("\\", "")
				# Now we filter the indivgual data sets

				if "data-endtime" in section.lower():
					start_time = section.split('"')[1]

				elif "data-position" in section.lower():
					end_time = section.split('"')[1]

				elif "data-blockid" in section.lower():
					date = section.split('"')[1]

				elif "data-pickupec" in section.lower():
					education_center_id = section.split('"')[1]

				elif "data-appointmentec" in section.lower():
					appointment_type = section.split('"')[1]

				elif "data-ecpickup" in section.lower():
					day_of_the_week = section.split(',')[0].replace('"', "")

				elif "data-blocksessionid" in section.lower():
					appointment_id = section.split('"')[1]

			appointment_object_ind['start_time'] = start_time
			appointment_object_ind['end_time'] = end_time
			appointment_object_ind['date'] = date
			appointment_object_ind['education_center_id'] = education_center_id
			appointment_object_ind['appointment_type'] = appointment_type
			appointment_object_ind['day_of_the_week'] = day_of_the_week
			appointment_object_ind['appointment_id'] = appointment_id

			appointment_array.append(appointment_object_ind)

		del appointment_array[0]
		return appointment_array


	
	
	
def validate_session(login_username, login_password):

	# This function creates a valid session
	valid_session_cookie_values = []
	with sync_playwright() as playwright_client:
		browser = playwright_client.chromium.launch(headless=True)
		context = browser.new_context()
		page = context.new_page()
		page.goto("https://www.topdriversignals.com/Student/StudentLogin.aspx")
		page.fill("#txtUserName", login_username)
		page.fill("#txtPassword", login_password)
		page.click("text='Login'")
		time.sleep(3.3)

	# Get the cookies from the context of the browser
		cookies = context.cookies()
		for cookie in cookies:
			if cookie['name'] == "ASP.NET_SessionId":
				valid_session_cookie_values.append(cookie['value'])
	# Return the valid cookie
	return valid_session_cookie_values[1]

