####Script that sends random quotes over email and SMS
####Written by Trevar Hupf

#Imports
from logging import info
import requests
import json
from random import randint
from twilio.rest import Client 
import yagmail
import os

#Env variables containing sensitive data
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
email_pw = os.environ['okaytrevaremail']

#Function returns a random quote from https://type.fit/api/quotes  
def random_quote():
    api_response = requests.get("https://type.fit/api/quotes") #api response into variable
    data = api_response.text  #store api response into text
    parse_json = json.loads(data) #parse the json file from text
    random_index = randint(0, len(parse_json)-1) #generates a random number that's between index 0 and the lenght of Json
    quote = parse_json [random_index]['text'] #stores the quote in variable
    author = parse_json [random_index]['author'] #stores the author in variable
    return ("Inspirational quote of the day:\n\n" + quote + "\n\n" + "By: " + author) #returns a string with quote and author

#Function to send email using yagmail, accepts 
def sendemail(email):
    yag = yagmail.SMTP('okaytrevar@gmail.com',email_pw)
    return(yag.send(email, 'Your daily inspiration', random_quote()))

#Twilio function accepts a phone number and sends randomquote() function to that number using Twilio api
def twiliotext(number):
    client = Client(account_sid, auth_token) 
    return (client.messages.create(messaging_service_sid='MG9bb4c52f16884d4a1981702ba479dcb2', body= random_quote(), to=number))

#Function calls
sendemail("trevabooo@gmail.com")
twiliotext("13035185767")
