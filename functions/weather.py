import datetime as dt
import requests
import talkback
user_input="Mumbai"
def weather(location):
    Base_Url="http://api.openweathermap.org/data/2.5/weather?"
    API_KEY="e0fdd235cc32f3a8e4530658254850a6"
    url=Base_Url+"appid="+API_KEY+"&q="+location
    response=requests.get(url).json()
    print(response)
    
    if(response['cod']=='404'):
        city=f"{location} not found."
        print(city)
        talkback.talkback(city)
    else:    
        temp_kelvin=response['main']['temp']
        temp_celsius=temp_kelvin-273.15
        wind_speed=response['wind']['speed']
        humidity=response['main']['humidity']
        description=response['weather'][0]['description']
        temp=f"Temperature in {location} : {temp_celsius:.2f}℃ degree celcius"
        wind=f"Wind Speed : {wind_speed} meters per second"
        humid=f"Humidity : {humidity}%"
        weather=f"General Weather in {location} : {description}"
        print(temp)
        print(wind)
        print(humid)
        print(weather)
        talkback.talkback(temp)
        talkback.talkback(wind)
        talkback.talkback(humid)
        talkback.talkback(weather)
        return temp,wind,humid,weather
weather(user_input)
        

if __name__=="_main_":
        
    weather(user_input)
