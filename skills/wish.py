import datetime
import talkback
def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=5 and hour<=12:
        greet="Good Morning"
        talkback.talkback(greet)
    elif hour>12 and hour<=16:
        greet="Good Afternoon"
        talkback.talkback(greet)
    elif hour>16 and hour<22:
        greet="Good Evening"
        talkback.talkback(greet)
    else:
        greet="Good Night"
        talkback.talkback(greet)
    return greet
wish()
if __name__=="_main_":
    
    wish()