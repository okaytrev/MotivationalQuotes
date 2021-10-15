from math import inf
import requests
import json
from random import randint

def random_quote():
    api_response = requests.get("https://type.fit/api/quotes") #api into variable
    data = api_response.text  #store api response
    parse_json = json.loads(data) #parse the json file
    random_index = randint(0, len(parse_json)-1) #generates a random number that's between index 0 and the lenght of Json
    info = parse_json [random_index]['text'] #pulls the random quote
    return ("Inspirational quote of the day: " + info)

print(random_quote())
