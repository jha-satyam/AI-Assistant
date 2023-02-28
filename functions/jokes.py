import talkback
import pyjokes
def jokes():
    joke=pyjokes.get_joke(language='en',category='neutral')
    talkback.talkback(joke)
    return joke

if"name"=="main":
    jokes()