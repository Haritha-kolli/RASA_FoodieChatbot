from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

tier_1_2_locations = ['ahmedabad',"bengaluru","chennai","delhi","hyderabad","kolkata", "mumbai","pune","agra", "ajmer", "aligarh", "amravati", "amritsar",
					  "asansol", "aurangabad", "bareilly", "belgaum", "bhavnagar", "bhiwandi",
					  "bhopal", "bhubaneswar", "bikaner", "bilaspur", "bokaro steel city", "chandigarh", "coimbatore", "cuttack", "dehradun",
					  "dhanbad", "bhilai", "durgapur", "dindigul", "erode", "faridabad", "firozabad", "ghaziabad", "gorakhpur", "gulbarga", "guntur",
					  "gwalior", "gurgaon", "guwahati", "hamirpur", "hubli–dharwad", "indore", "jabalpur", "jaipur", "jalandhar", "jammu", "jamnagar",
				      "jamshedpur", "jhansi", "jodhpur", "kakinada", "kannur", "kanpur", "karnal", "kochi", "kolhapur", "kollam", "kozhikode", "kurnool",
				      "ludhiana", "lucknow", "madurai", "malappuram", "mathura", "mangalore", "meerut", "moradabad", "mysore", "nagpur", "nanded", "nashik",
				      "nellore", "noida", "patna", "pondicherry", "purulia", "prayagraj", "raipur", "rajkot", "rajahmundry", "ranchi", "rourkela", "salem", "sangli",
					  "shimla", "siliguri", "solapur", "srinagar", "surat", "thanjavur", "thiruvananthapuram", "thrissur", "tiruchirappalli", "tirunelveli",
			          "tiruvannamalai","ujjain", "bijapur", "vadodara", "varanasi", "vasai-virar city", "vijayawada", "visakhapatnam", "vellore","warangal"]

class ActionSearchRestaurants(Action):

	
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"8a8605e444ad3c03ad97c043689003c9"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		price_min = 0
		price_max = 9999

		#location check
		if loc.lower() not in tier_1_2_locations:
			return dispatcher.utter_message("we don't operate in that area yet.")

		else:
			location_detail=zomato.get_location(loc, 1)
			d1 = json.loads(location_detail)
			lat=d1["location_suggestions"][0]["latitude"]
			lon=d1["location_suggestions"][0]["longitude"]
			cuisines_dict={'american':1,'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'mexican':73,'north indian':50,'south indian':85}
			#trying to fetch 100 results if available
			results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 100)
			d = json.loads(results)
			count = 0
			#'response' is to display the top 5 restaurants to the user in the chat
			response=""
			#'emailbody' - we are going to include top 10 restaurants if available
			email_response=""
			if d['results_found'] == 0:
				response= "no results"
			else:
				#extracting restaurants
				restaurants = d['restaurants']
				#sorting based on user_rating
				restaurants = sorted(restaurants,key= lambda k:k['restaurant']['user_rating']['aggregate_rating'],reverse=True)
			
				if price in ['low','mid','high']:
					if price == 'low':
						price_min = 0
						price_max = 300
					elif price == 'mid':
						price_min = 300
						price_max = 700
					elif price == 'high':
						price_min = 700
						price_max = 9999
					for restaurant in restaurants:
						if int(restaurant['restaurant']['average_cost_for_two'])>=price_min and int(restaurant['restaurant']['average_cost_for_two'])<price_max:
							if count < 5:
								response = response + " " + restaurant['restaurant']['name'] + " in " + restaurant['restaurant']['location']['address']+ " has been rated "+restaurant['restaurant']['user_rating']['aggregate_rating']+"\n"
							if count < 10:
								email_response = email_response + " " + restaurant['restaurant']['name'] + " in " + restaurant['restaurant']['location']['address']+ " with average budget for two people Rs."+str(restaurant['restaurant']['average_cost_for_two'])+" has been rated "+restaurant['restaurant']['user_rating']['aggregate_rating']+"\n"
							count = count + 1
				else:
					#return dispatcher.utter_ask_price()
					for restaurant in restaurants:
						if count<5:
							response=response + restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+ " has been rated "+restaurant['restaurant']['user_rating']['aggregate_rating']+"\n"
						if count < 10:
							email_response = email_response + " " + restaurant['restaurant']['name'] + " in " + restaurant['restaurant']['location']['address']+ " with average budget for two people Rs."+str(restaurant['restaurant']['average_cost_for_two'])+ " has been rated "+restaurant['restaurant']['user_rating']['aggregate_rating']+"\n"
						count = count + 1

			if response=="":
				response = "No restaurants in that budget range" + " in " + loc
			# if restaurants found - asking the user whether he/she wants them to send on their mail
			elif count<5:
				response = response + "\n\nWe just found "+str(count)+" restaurants with given preferences"+"\n Would you like us to send top 10 restaurant details on your mail?"
			else:
				response = response + "\nWould you like us to send top 10 restaurant details on your mail"
			dispatcher.utter_message("-----\n"+response)
			#setting 'emailbody' slot, to use it in 'action_send_email'
			return [SlotSet('emailbody',email_response)]
			#return [SlotSet('location',loc)]


class ActionSendEmail(Action):

	def name(self):
		return 'action_send_email'

	def run(self,dispatcher,tracker,domain):
		to_user = tracker.get_slot('email')
		if to_user is not None:
			#create your gmail id and paste here
			from_user = 'foodie.searchrestaurant@gmail.com'
			#password set for from_user email
			password = 'HarithaFaiz'
			server = smtplib.SMTP('smtp.gmail.com',587)
			server.starttls()
			server.login(from_user, password)
			subject = 'Foodie Khana - Top Restaurants for you'
			msg = MIMEMultipart()
			msg['From'] = from_user
			msg['TO'] = to_user
			msg['Subject'] = subject
			#appending contents of 'emailbody' to email body
			body = tracker.get_slot('emailbody')
			body_header = '''Hi User, \n \n'''
			body_footer = '''\n\n Thanks & Regards \n Team: Foodie Khana \n For more information reply on same mail. Our Team will connect with you soon.'''
			body = body_header+body+body_footer
			msg.attach(MIMEText(body,'plain'))
			text = msg.as_string()
			server.sendmail(from_user,to_user,text)
			server.close()
			#dispatcher.utter_message("successfully sent the email")

		

