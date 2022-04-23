#excercise 9---Akhbaar padhke sunao


import requests
import json

def speak(str):
     from win32com.client import Dispatch
     speak=Dispatch("SAPI.SpVoice")
     speak.Speak(str)

if __name__=='__main__':
     speak('News for today are:')
     url="https://newsapi.org/v2/everything?domains=techcrunch.com,thenextweb.com&apiKey=00315c7a8f784914966c1f94e8673053"
     news=requests.get(url).text
     news_dict=json.loads(news)
     print(news_dict['articles'])

     arts=news_dict['articles']

     for article in arts:
          print(article['title'])
          speak(article['title'])

          speak("Next news coming up")

     speak("Thanks for listning.  Have a good day!!!")


