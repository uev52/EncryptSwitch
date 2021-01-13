import datetime, time, twint
import pyAesCrypt as crypt

def versleutel(bestandPad, wachtwoord):	
	print("De versleutelmeganisme is geeactiveerd")
	#bit grootte verleuteling
	bufSize = 64 * 1024
	#AES versleuteling van het betand
	crypt.encryptFile(bestandPad, (bestandPad + ".aes"), wachtwoord, bufSize)
	print("De encryptie is begonnen, het proces kan niet meer teruggedraait worden")

def checkAvtivatie(conf, checkTijd, filePad, wachtwoord, Timer):

	try:
		twint.run.Search(conf)
	except ValueError:
		print("Er is iets misggegaan tijdens het configureren, probeer het opnieuw")
		Doel()

	berichten = twint.output.tweets_list

	if not berichten:
		if time.time() >= Timer:
			versleutel(filePad, wachtwoord)
		else:
			print("Er zijn geen tweets gevonden. Heb gedult er moet nog gecheck worden ...")
			time.sleep(checkTijd)
			checkAvtivatie(conf, checkTijd, filePad, wachtwoord, Timer)
	else:
		print("Het versleutelmeganisme is uitgeschakeld - overgeschakeld op exit mode")
		exit()

def Doel():
	conf = twint.Config()
	zoekTijd = input("Wanneer wilt u zoeken naar een target: jjjj - mm - dd: ")

	try:
		datetime.datetime.strptime(zoekTijd, "%Y-%m-%d")
	except ValueError:
		print("Verkeerde invoer, houd de juiste formaat aan.")
		Doel()

	conf.Since = zoekTijd
	conf.Search = input("Geef de sleutel/bericht op waarmee de encryptiemechanisme kan worden gestopt: \n")
	conf.Username = input(" Geef hier de gebruikersnaam van de twitteraccount waarmee de encrptie kan worden gestopt: \n")
	checkTijd = int(input("Geef de tijd in secondes op wanneer er word gecheckt op een tweet: \n"))
	filePad = input(" Geef hier de volledige pad van het bestand die u wilt versleutelen: \n")
	wachtwoord = input("Geef hier het wachtwoord op waarmee u de bestanden wilt versleutellen: \n")
	Timer = (time.time()+(int(input("Hoeveel tijd in minuten wil je de timer instellen om de encryptiemechanisme te activeren: \n"))*60))
	conf.Hide_output = True
	conf.Store_object = True
	checkAvtivatie(conf, checkTijd, filePad, wachtwoord, Timer)

Doel()


