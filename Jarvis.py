import pyaudio,sys
import os
import pyttsx
import webbrowser
import random
import pygame
import speech_recognition as sr
engine = pyttsx.init()

def speak(text):
	engine.say(text)
	engine.runAndWait()
	
def listen():
		r = sr.Recognizer()
		with sr.Microphone() source:
			audio = r.listen(source)
			
		try:
			return r.recognize_google(audio)
		
		except sr.UnknownvalueError:
			print("Could not understand the audio")
		except sr.RequestError as e:
			print("Rcog Error: {0}",format(e))
			
		return ""
		
def internetexplorer():
	speak('got it sir')
	speak('searching for the required application sir')
	speak('configuring all dlls')
	speak('application found')
	speak('starting internet explorer')
	os.system('start iexplore.exe')
	
def firefox():
	speak('i heard you sir')
	speak('finding firefox application sir')
	speak('configuring all required dlls')
	speak('application found')
	speak('starting mozilla firefox')
	os.system('start firefox.exe')
	
def notepad():
	speak('ok sir')
	speak('you have requested for text editor sir')
	speak('Searching for notepad application in windows')
	speak('application found')
	speak('starting notepad')
	os.system('start notepad.exe')
	
def wordpad():
	speak('ok sir')
	speak('you have requested for wordpad sir')
	speak('Searching for wordpad application in windows')
	speak('application found')
	speak('starting wordepad')
	os.system('start wordepad.exe')
	
def greeting():
	k = random.choice(['you are welcome','welcome sir','you are welcome sir'])
	speak(k)

def excel():
	os.system("start excel.exe")
	
def python():
	os.system('start python.exe')
	
def internet():
	os.system("start chrome.exe")
	speak('what do i search for you sir')
	webbrowser.open_new_tab('http://google.com/?q=%s'%listen())
	speak('okay searching....')
	
def media():
	speak('good choice sir')
	speak('connecting to player')
	speak('connected to player')
	speak('starting requested application')
	os.system('start KMPlayer.exe')
	speak('what do i play for you sir')
	os.startfile('F:\Songs\Sundari' +listen()+ '.mp3')
	speak('ok sir playing'+ listen() + 'for you')
	
def shutdown():
	speak('got it sir')
	speak('asking for permission from operating system')
	speak('permission granted')
	speak('connecting to command prompt')
	speak('connected to command prompt')
	speak('shutting down the aplication sir')
	os.system('shutdown -s')
	
def restart():
	speak('understood sir')
	speak('asking for permission from operating system')
	speak('permission granted')
	speak('accessing files from system')
	speak('accessed all files')
	speak('eshtablishing connection to command prompt')
	speak('connection eshtablished')
	speak('ok sir computer is restarting  wait a moment')
	os.system('shutdown -r')

def logoff():
	speak('I heard you sir')
	speak('asking for permission from operating system')
	speak('permission granted')
	speak('signing you out')
	speak('eshtablishing connection to command prompt')
	speak('connection eshtablished')
	speak('ok sir i am logging off your computer as you said  wait a moment')
	os.system('shutdown -I')
	
def stop_shutdown():
	speak('ok sir connecting')
	speak('ok sir i am cancelling the shutdown command as you said  wait a moment')
	os.system('shutdown -a')
	
def getonline():
	speak('ok sir')
	width = 1280
	height = 786
	img = pygame.image.load('C:\Users\Dell\Pictures\jarvis.jpg')
	display = pygame.display.set_mode((width,height))
	crashed = True
	while crashed:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				crashed = False
				pygame.quit()
					sys.exit(0)
					quit()
		disply.blit(img,(0.0))
		pygame.display.update()
		speak('connecting to remote service')
		speak('establishing secure connection')
		speak('starting all systems')
		speak('downloading and initialising all required services')
		speak('just a second sir')
		speak('')
		speak('')
		speak('secure connection established')
		speak('all system have started')
		speak('all drivers are securedly installed in your private server')
		speak('please wait for a second sir')
		speak('ok sir')
		speak('now i am online sir')
		loop()

def gooffline():
	speak('as you wish sir')
	speak('dissconnecting from server')
	speak('shutting down all services and systems')
	speak('prepairing to go offline')
	speak('all systems are down')
	speak('i hope you liked my services')
	speak('goodbye sir')
	quit()
	
def mainfunction(source):
	r = sr.Recognizer()
	audio = r.listen(source)
	user = r.recognize_sphinx(source)
	print(user)
	if user == "Open python":
		python()
	elif user == "explorer":
		internetexplorer()
	elif user == "down":
		gooffline()
	elif user == "start firefox":
		firefox()
	elif user == "note":
		notepad()
	elif user == "word":
		wordpad()
	elif user == "Excel":
		excel()
	elif user == "find":
		internet()
	elif user == "song":
		media()
	elif user == "Jarvis":
		getonline()
	elif user in ["thnks you","thanks","thank you Jarvis","thanks Jarvis"]:
		greeting()
	elif user in ["hi","hey","hello","whatsup","good morning"]:
		a = random.choice(["hi","hey","hello","whatsup","good morning"])
		speak(a)
	elif user in ["good afternoon","noon"]:
		b = random.choice(["good afternoon to you sir"])
		speak(b)
	elif user in ["goog night","night"]:
		c = random.choice(["good night sir"])
		speak(c)
		gooffline()
		
def loop():

	if _name_ "" "_main_":
		r = sr.Recognizer()
		with sr.Microphone() as source:
			while 1:
				manifunction(source)

loop()