#!/bin/evn/python3

#import request module
import requests


#create a variable to hold the URL
ISS_URL =" http://api.open-notify.org/iss-now.json"

def main():
    resp = requests.get(ISS_URL).json()

#print resp to see results
    print(resp)

    print("CURRENT LOCATION OF THE ISS:")

    lon = resp["iss_position"]["longitude"]
    print(f"Lon: {lon}")

    lat = resp["iss_position"]["latitude"]
    print(f"Lat: {lat}")




if __name__ ==  "__main__":
    main()




