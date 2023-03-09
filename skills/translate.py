from googletrans import Translator

def trans(text):
    line=str(text)
    translate=Translator()
    result=translate.translate(line,language='en')
    data=result.text
    print(f"you said:{data}.")
    return data