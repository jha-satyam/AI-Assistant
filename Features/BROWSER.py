import webbrowser
import pywhatkit
import pyautogui

def play_on_youtube(query):
    pywhatkit.playonyt(query)
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter') 
    return True  

def sites(data):
    webbrowser.open(f'www.{data}.com')
    return True

def google_search(query):
    pywhatkit.search(query)
    return True
