import json
#Importing json module
import http.client
#This is a client that can send a request and get a response from the server in http format.Very useful in json


pokemon_list = []
#Sets a frame that I can use to add in the info for pokemon

try:
    conn = http.client.HTTPSConnection("pokeapi.co")
    #putting the info from the pokemonapi website into a variable
    conn.request("GET", "/api/v2/pokemon?limit=10")
    #Getting the info
    
    response = conn.getresponse()
    #Code is getting a response from the conn variable and saving it for later
    
    data_storage = response.read().decode('utf-8')
    #It reads the response and decodes it to make sure its understanderble
    #8-bit values are used in the encoding.- unicode transformation format
    api_response = json.loads(data_storage)
    #Loads the response held
    

    for i in range(10):
        pokemon_name = api_response['results'][i]['name']
        #Loads 10 names form the database and saves the results
        pokemon_list.insert(i, pokemon_name)
        #Inserts the pokemon names into the pokemon list

    print(pokemon_list)
    #Prints the list which holds all the names

except http.client.HTTPException as e:
    print("HTTP Exception:", e)
#it checks for the internet connection and prints the error if there is
    

finally:
    conn.close()
    #Finally stops the connection
