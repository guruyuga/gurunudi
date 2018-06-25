#!/usr/bin/env python

from gurunudi import AI,api

#First setup your API key. This needs to be done only once at the beginning in an application. 
#Visit https://gurulaghu.com to get an API key
api.key="<YOUR_GURUNUDI_API_KEY>" 

#AI is a class with simple yet intelligent attributes. Create an AI object by passing your document text as the argument to the constructor.
ai = AI("I really did not like that movie")

#The AI attribute "sentiment" returns sentiment or mood detected by Gurunudi AI API for the given text
print(ai.sentiment)
assert(ai.sentiment=="negative")

#If there was any error during the attribute call, then ai.latest_error will contain the error string, else it will be None
#if ai.sentiment returns None i.e. if sentiment analysis API fails, then check this value for the corresponding error message
assert(ai.latest_error==None)

#By default the text is assumed to be in English language. If the text is in a different language, you can pass the corresponding language code. See example below for German text.
ai = AI("Aller Anfang ist schwer",gurunudi.GERMAN)

#Other sentiment examples for English
ai = AI("she is very beautiful")
assert(ai.sentiment=="positive")

ai = AI("The ambience was good, but the food was bad")
assert(ai.sentiment=="mixed")

ai = AI("roses are red, violets are blue")
assert(ai.sentiment=="neutral")

#For the latest updated list of languages supported by Gurunudi for sentiment analysis visit https://gurulaghu.com/languages/
