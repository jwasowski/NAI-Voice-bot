# NAI - AI tools classes - Text to speech
The script is a simple speech to speech bot implementation. Bot's purpose is to anwser three questions. <br />
What is the meaning of life? How tall is president of Poland? What is best in life? <br />
'What is the meaning of life?' question is anwsered based on Wikipedia article. Other questions have hardcoded anwsers. <br />
You can interact with bot by using you microphone.  <br />


### Requirements
```
Anaconda (Python 3.7) or Python 3.7
Python IDE (for development)
Microphone
Dependencies:
speech_recognition package
sys package
pyttsx3 package 
wikipedia package

```

### Questions and commands
Bot recognizes three questions:

| Questions |
| ------------- | 
| `What is the meaning of life?`  |
| `How tall is president of Poland?`  | 
| `What is best in life?`  | 

and there are two keywords (commands) to shutdown script:

| Keyword |
| ------------- | 
| `Exit`  |
| `Quit`  |

### Running Application

To run script use following syntax in Python console <br />

```
In Spyder IDE (Anaconda):
runfile('disk:\path\to\script\simpleSpeechBot.py', wdir='disk:\path\to\script\')

Example usage:
runfile('D:/Informatyka/NAI/lab5/simpleSpeechBot.py', wdir='D:/Informatyka/NAI/lab5')

In Anaconda terminal (use it inside folder containing script):
python simpleSpeechBot.py

In PyCharm IDE (Python):
simpleSpeechBot.py

In Python terminal (not tested, but it should work):
python simpleSpeechBot.py

```


## Authors

* **Jakub Wąsowski** - [JWasowski](https://github.com/jwasowski) 