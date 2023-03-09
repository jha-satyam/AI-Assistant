import pyjokes
def jokes():
    joke=pyjokes.get_joke(language='en',category='neutral')
    return joke

if __name__=="_main_":
    jokes()