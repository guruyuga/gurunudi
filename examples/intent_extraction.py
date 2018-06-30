#!/usr/bin/env python

#***************************** INTENT **********************************/
#  
#  This example shows how to find intent of a text using Gurunudi AI 
#  For example, "get me some coffee" is a command while "hi" is a greeting
#  
#***************************** INTENT **********************************/


from gurunudi import AI,api,lang

#First setup your API key. This needs to be done only once at the beginning in an application. 
#Visit https://gurulaghu.com to get an API key
api.key="<YOUR_GURUNUDI_API_KEY>" 

#AI is a class with simple yet intelligent attributes. Create an AI object by passing your document text as the argument to the constructor.
ai = AI("Larry Page was doing his Phd at Stanford University in 1996.")

#The AI attribute "intent" returns a list of intents extracted from the given text
print(ai.intents)

#If there was any error during the attribute call, then ai.latest_error will contain the error string, else it will be None
#if ai.intents returns None i.e. if intent extraction API fails, then check this value for the corresponding error message
assert(ai.latest_error==None)

#By default the text is assumed to be in English language. If the text is in a different language, you can pass the corresponding language code. See example below for French text.
ai = AI("Emmanuel Macron est le président de la France.",lang.FRENCH)

#For the latest updated list of languages supported by Gurunudi for intent extraction visit https://gurulaghu.com/languages/
