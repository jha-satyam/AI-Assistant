from googletrans import Translator
import talkback
def trans(text):
    line=str(text)
    translate=Translator()
    result=translate.translate(line,language='en')
    data=result.text
    print(f"you said:{data}.")
    return data
    
talkback.talkback(trans("billi aadesh ka upyog kya hai"))
