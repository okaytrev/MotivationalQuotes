import requests
import json
from random import randint
from twilio.rest import Client 
 
def random_quote():
    api_response = requests.get("https://type.fit/api/quotes") #api into variable
    data = api_response.text  #store api response
    parse_json = json.loads(data) #parse the json file
    random_index = randint(0, len(parse_json)-1) #generates a random number that's between index 0 and the lenght of Json
    info = parse_json [random_index]['text'] #pulls the random quote
    return ("Inspirational quote of the day: " + info)


account_sid = 'ACf4990cb06cc8d26bb53480f12a81ed33' 
auth_token = 'dfcef6c2079c3b160d06fe2f78520b34' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(messaging_service_sid='MG9bb4c52f16884d4a1981702ba479dcb2', body= random_quote(), to='+13035185767' ) 
 
print(message.sid)
