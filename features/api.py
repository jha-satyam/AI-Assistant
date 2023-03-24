import wolframalpha
import requests
import wikipedia
import pyjokes

#To get a programming jokes
def jokes():
    joke=pyjokes.get_joke(language='en',category='neutral')
    return joke

#To perform mathematical calculation
def computation(query):
    client=wolframalpha.Client('VTY239-55Y8AXJEW4')
    res=client.query(query)
    result=next(res.results).text
    return result


#To fetch weather forecast of particular city
def weather(location):
    Base_Url="http://api.openweathermap.org/data/2.5/weather?"
    API_KEY="e0fdd235cc32f3a8e4530658254850a6"
    url=Base_Url+"appid="+API_KEY+"&q="+location
    response=requests.get(url).json()
    
    if(response['cod']=='404'):
        city=f"{location} not found."
        return city
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
        return temp,wind,humid,weather

#To retrive information from the wikipedia
def search_wiki(query):
    result=wikipedia.summary(query)
    return result
    
if __name__=="_main_":
    computation(query)
    weather(location)
    search_wiki(query)


