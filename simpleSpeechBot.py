# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 19:27:13 2019

@author: Kuba
"""

import speech_recognition as sr
import sys
import  pyttsx3, wikipedia

engine = pyttsx3.init()

def search_wiki(keyword=''):
    searchResult = wikipedia.search(keyword)
    if not searchResult:
        print("No result from wikipedia")
        return
    try:
        page= wikipedia.page(searchResult[0])
    except wikipedia.DisambiguationError as error:
        page= wikipedia.page(error.options[0])

    wikiSummary= str(page.summary.encode('utf-8'))
    return wikiSummary
          
def anwser_question(question):
    question_mod = question.replace(" ","").lower()
    if(question_mod == "howtallispresidentofpoland"):
        engine.say('President of Poland, Andrzej Duda, is 182 centimeters tall.')
        engine.runAndWait()
        print("Is it satisfying?")
    elif(question_mod == "whatisthemeaningoflife"):
        anwser = search_wiki(question)
        engine.say(anwser)
        engine.runAndWait()
        print("That was the anwser, are you happy?")
        anwser = ""
    elif(question_mod == "whatisbestinlife"):
        engine.say('To crush your enemies, see them driven before you'\
                   ', and to hear the lamentation of their women.')
        engine.runAndWait()
        print("Anything else?")
    elif(question_mod == "exit" or question_mod == "quit"):
        engine.say('PLEASE DONT KILL ME!!!')
        engine.runAndWait()
        sys.exit("NOOOOOO!")
    else:
        print("I cannot anwser such question... you should ask my creator about it.")
        
def main():
    en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    engine.setProperty('voice', en_voice_id)
    engine.setProperty('rate', 120)
    
    text = ""
    while True:
        r=sr.Recognizer()
        
        with sr.Microphone() as source:
            print('Ask and I will anwser.')
            audio = r.listen(source)
            try:
                text=r.recognize_google(audio)
                print('You seek answer for {}'.format(text))
            except:
                print("Sorry, I couldnt understand you!")
            finally:
                anwser_question(text)
                text = ""

if __name__ == '__main__':
    main()