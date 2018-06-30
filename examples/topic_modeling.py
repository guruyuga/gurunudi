#!/usr/bin/env python

#******************************** TOPIC MODELING *********************************/
#  
#  This example shows how to suggest topics for a given text using Gurunudi AI
#  For example, "oil prices on the rise" can be associated wit the topic "BUSINESS"
#  "Kohli scores a century" can be associated wit the topics ["SPORTS","CRICKET"]
#  
#******************************** TOPIC MODELING *********************************/


from gurunudi import AI,api,lang

#First setup your API key. This needs to be done only once at the beginning in an application. 
#Visit https://gurulaghu.com to get an API key
api.key="<YOUR_GURUNUDI_API_KEY>" 

#AI is a class with simple yet intelligent attributes. Create an AI object by passing your document text as the argument to the constructor.
ai = AI("Oil prices fall on expected output rise")

#The AI attribute "topics" returns a list of topics suggested by Gurunudi AI API for the given text
assert(ai.topics==["Business"])

#If there was any error during the attribute call, then ai.latest_error will contain the error string, else it will be None
#if ai.topics returns None i.e. if topic modeling API fails, then check this value for the corresponding error message
assert(ai.latest_error==None)

#By default the text is assumed to be in English language. If the text is in a different language, you can pass the corresponding language code. See example below for Italian text.
ai = AI("L'India, ufficialmente Repubblica dell'India, è uno Stato federale dell'Asia meridionale, con capitale Nuova Delhi.",lang.ITALIAN)

#For the latest updated list of languages supported by Gurunudi for topic modeling visit https://gurulaghu.com/languages/
