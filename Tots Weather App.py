"""
Tots Weather App
API Weather
Datetime Module
Weather education application for toddlers.
The App will ask for an input from the toddler to request what city they are based.


"""

import requests
import calendar
import datetime

# Ask for user's full name
full_name = input('Please enter your full name ')

# Split the First and Last Names into 2 items
name_split = full_name.split(" ")
# Access string via index
first_name =(name_split[0])
last_name = (name_split[1])
# Use slice to get the first character of the first name and concatenate with last name
user_name = (first_name[0] + last_name)
# Display a personalised welcome message print('Hi {}.format(first_name), Welcome to Tots Weather App")
print("Your username is {}".format(user_name))

# Get current date and day-name via datetime module
today_date = datetime.datetime.now()
print('Today is {}'.format(today_date.strftime("%A")))

# Request city name from user
city = input('Please enter your city name ')

# Get data from open weather
api_key = 'de2824e6d185bfe60cc6f3bb19444a96'
url_openweather = 'https://api.openweathermap.org/data/2.5/weather'
payload = {
    'q': city,
        'appid': api_key
}

response = requests.get(url_openweather, params = payload)
if response.status_code == 200:
    data = response.json()


temp_k = data['main']['temp']
desc = data['weather'][0]['description']
print(f'Description: {desc}')

# function to calculate Celsius from Fahrenheit
def find_celsius(temp_k):
    converted_temp = float(temp_k)
    result = (converted_temp - 273.15)
    return result

# call function
temp_c = find_celsius(temp_k)
print('The current temperature is {}'.format(temp_c))

# If statement to advise user that its either hot, cold or warm depending on the temperature
if temp_c <= 15:
    print("It's cold")
elif temp_c < 25:
    print("It's warm today")
else:
    print("It's hot today")

# Collect the main weather forecost for the day
weather_code = data['weather'][0]['main']
# Dictionary of clothing based on weather forecast
clothing_dict = {'Thunderstorm': ['Socks', 'Wellies', 'Boots', 'Coat', 'Cardigan', 'umbrella'],
                 'Drizzle': ['Socks', 'Wellies', 'Boots', 'Rain Coat', 'Trousers', 'Umbrella'],
                 'Rain': ['Socks', 'Wellies', 'Boots', 'Coat','Cardigan', 'umbrella'],
                 'Snow': ['Socks', 'Hat', 'Snow Boots', 'Ear Muffs', 'Coat', 'Gloves', 'Scarf'],
                 'Clear': ['Shorts', 'Swimming', 'Costumes', 'Tshirt','Flip-flops', 'Sun hat', 'Sandals', 'Sunglasses',
                           'Vest'],
                 'Clouds': ['Jacket', 'Socks', 'Boots', 'Cardigan']
                  }

# Pull clothing list based the weather code and iterate over the list
clothing_list = (clothing_dict[weather_code])
if weather_code!='str':
    print('Here is a list of clothes you might choose to wear today ')
    for i in clothing_list:
        print(i)
else:
  print("Please check with your grown up what you can wear ")

# Write to a file the user input
user_choice = input("List the clothes you picked ")
user_list = list(user_choice)
with open('tots_app1.txt', 'a+') as file:
    file.write(user_choice + "\n")



