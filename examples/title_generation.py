#!/usr/bin/env python

#*********************************** TITLE GENERATION ******************************/
#
#  This example shows how to auto generate a title for a large text using Gurunudi AI
#
#*********************************** TITLE GENERATION ******************************/


from gurunudi import AI,api,lang

#First setup your API key. This needs to be done only once at the beginning in an application. 
#Visit https://gurulaghu.com to get an API key
api.key="<YOUR_GURUNUDI_API_KEY>" 

#AI is a class with simple yet intelligent attributes. Create an AI object by passing your document text as the argument to the constructor.
ai = AI("capital of India?")

#The AI attribute "title" returns a title suggestion for the given text
print(ai.title)

#If there was any error during the attribute call, then ai.latest_error will contain the error string, else it will be None
#if ai.title returns None i.e. if title API fails, then check this value for the corresponding error message
assert(ai.latest_error==None)

#By default the text is assumed to be in English language. If the text is in a different language, you can pass the corresponding language code. See example below for French text.
ai = AI("Emmanuel Macron est le président de la France.",lang.FRENCH)

#For the latest updated list of languages supported by Gurunudi for title visit https://gurulaghu.com/languages/
