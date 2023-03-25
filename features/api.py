import wolframalpha
import requests
import wikipedia
import pyjokes
import json

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

#To fetch latest news of India
def news():
    api_dict={"business":"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=759eabe66a3949e79df242f6a6f37f9a",
    "entertainment":"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=759eabe66a3949e79df242f6a6f37f9a",
    "health":"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=759eabe66a3949e79df242f6a6f37f9a",
    "science":"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=759eabe66a3949e79df242f6a6f37f9a",
    "sports":"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=759eabe66a3949e79df242f6a6f37f9a",
    "technology":"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=759eabe66a3949e79df242f6a6f37f9a"}

    content=None
    url=None
    print("which field news do you want,[business],[sports],[health],[technology],[entertainment],[science]")
    field=input("Type field news that you want:")
    for key,value in api_dict.items():
        if key.lower() in field.lower():
            url=value
            print(url)
            print("url was found")
            break
        else:
            url=True
            if url is True:
                print("url not found")
    news=requests.get(url).text
    news=json.loads(news)
    print("here is the first news")
    arts=news["articles"]
    for articles in arts:
        article=articles["title"]
        print(article)
        news_url=articles["url"]
        print(f"for more info visit:{news_url}")

        a=input("[press c for continue] or [press s to stop]")
        if str(a)=="c":
            pass
        elif str(a)=="s":
            break
    print("thats all")


if __name__=="_main_":
    computation(query)
    weather(location)
    search_wiki(query)
    news()

