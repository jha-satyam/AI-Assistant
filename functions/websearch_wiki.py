import wikipedia
import talkback
text="Salman Khan"
def search_wiki(text):
    result=wikipedia.summary(text)
    print(result)
    return result
result=search_wiki(text)
talkback.talkback(result)