from tkinter import *
import speech_recognition as sr
import os, csv
import detectlanguage
from googletrans import Translator
from nltk.tokenize import sent_tokenize, word_tokenize
import difflib
import goslate


detectlanguage.configuration.api_key = "4a757fef0e4e952fd4296813c7f581ee"
''' uncommented '''
def speak_():
	r = sr.Recognizer()                                                                                   
	with sr.Microphone() as source:
		print("Speak:")
		audio = r.listen(source) 
	a1=r.recognize_google(audio); 


def gui():

	test = e1.get()

	testy = word_tokenize(test)



	sent = []

	lan = []

	hin = []



	translator= Translator()
	gs = goslate.Goslate()


	with open('/home/charul/recent_projects/code_switching/normalisation_dataset.csv', 'r') as file:

		reader = csv.reader(file, delimiter='	')

		for row in reader:

			sent.append(row[0])   # stores the first column of all the rows

			lan.append(row[1])    # stores the 2nd column of all the rows

			hin.append(row[2])    # storesthe 3rd column of all the rows



	result= ''

	con_hin = ''



	for words in testy:

		maxi=0.90

		match=''  

		for i in range (0, 15966):

			if(difflib.SequenceMatcher(None, sent[i], words).ratio() > maxi):  # so that we get the word having highest ratio

				maxi=difflib.SequenceMatcher(None, sent[i], words).ratio() 

				match = hin[i]



		if(match ==''):   # if the typed word is not present in dataset then the typed word is sent as output

			#match = words
			if(detectlanguage.simple_detect(words) != 'en'):
				match=words

			else:	
				x = translator.translate(words, dest='hi')

				con_hin = x.text

				match = con_hin

		result = result + match + " "

	

	print(result)









	# code for translating the language

	
	y= gs.translate(result,'en')

	#x=translator.translate(result, dest='en')

	#y=  x.text    # for extracting only converted text and omitting the other output parameters

	print(y)

	text1.insert(INSERT, y+"\n")  # for displaying the result in the text box in GUI

	print()



	#Code for speech recognition
	
	speak_('Speech recog')



	#POS tagging

   

	output_file=open('hindi.input.txt', 'w')

	output_file.write(result)

	output_file.close()	



	os.chdir('/home/charul/recent_projects/code_switching/Hindi_POS')

	os.system('make tag')

	

# code for GUI

master = Tk()



Label(master, text="Your search",font=("Helvetica", 16), fg="red", bg="#000000", padx=100, pady=40).grid(row=3, column=1, sticky=W)

e1 = Entry(master)

e1.grid(row=3, column=1, padx=300)



Button(master, text='Convert', command=gui, bg="#0D47A1", fg="white",activebackground="black", activeforeground="white", bd=4).grid(row=15, column=1, pady=10)
#Button(master, text='Speak', command=speak_, bg="#0D47A1", fg="white",activebackground="black", activeforeground="white", bd=4).grid(row=15, column=2, pady=10,sticky=W)



text1 = Text(master,height=10, bg="black", fg="#3498db",font=("Helvetica", 10))

text1.grid(row = 18,column=1, pady=100)

text1.insert(INSERT, "                                                                Result\n\n")

master.configure(background='#000000') 

mainloop( )
