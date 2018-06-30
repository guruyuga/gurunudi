#!/usr/bin/env python

#***************************** LANGUAGE DETECTION ******************************/
#  
#  This example shows how to detect the language of a text using Gurunudi AI
#  For example, "get me some coffee" is ENGLISH, while "Lorem Ipsum" is LATIN
#  
#***************************** LANGUAGE DETECTION ******************************/


from gurunudi import AI,api

#First setup your API key. This needs to be done only once at the beginning in an application. 
#Visit https://gurulaghu.com to get an API key
api.key="<YOUR_GURUNUDI_API_KEY>" 

#AI is a class with simple yet intelligent attributes. Create an AI object by passing your document text as the argument to the constructor.
ai = AI("lorem ipsum")

#The AI attribute "language" returns the name of the language detected by Gurunudi AI API for the given text
assert(ai.language=="Latin")

#If there was any error during the attribute call, then ai.latest_error will contain the error string, else it will be None
#if ai.language returns None i.e. if language detection API fails, then check this value for the corresponding error message
assert(ai.latest_error==None)

ai = AI("matter tells space how to curve and space tells matter how to move").language
assert(ai.language=="English")

ai = AI("ನನ್ನ ಹೆಸರು ಗುರು")
assert(ai.language=="Kannada")

#For the latest updated list of languages supported by Gurunudi for language detection visit https://gurulaghu.com/languages/
