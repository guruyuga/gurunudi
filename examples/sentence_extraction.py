#!/usr/bin/env python

#***************************** SENTENCE EXTRACTION ******************************/
#  
#  This example shows how to extract individual sentences in a text using Gurunudi AI
#  For example, "Mr. India was a great movie. It was directed by Shekhar Kapur."
#  contains the sentences ["Mr. India was a great movie.", "It was directed by Shekhar Kapur."]
#  
#***************************** SENTENCE EXTRACTION ******************************/


from gurunudi import AI,api,lang

#First setup your API key. This needs to be done only once at the beginning in an application. 
#Visit https://gurulaghu.com to get an API key
api.key="<YOUR_GURUNUDI_API_KEY>" 

#AI is a class with simple yet intelligent attributes. Create an AI object by passing your document text as the argument to the constructor.
ai = AI("India is a country in South Asia. It shares land borders with Pakistan to the west. China, Nepal, and Bhutan are to the northeast; and Myanmar (Burma) and Bangladesh to the east.")

#The AI attribute "sentences" returns a list of sentences extracted by Gurunudi AI API from the given text
print(ai.sentences)

#If there was any error during the attribute call, then ai.latest_error will contain the error string, else it will be None
#if ai.sentences returns None i.e. if sentences extraction API fails, then check this value for the corresponding error message
assert(ai.latest_error==None)

#By default the text is assumed to be in English language. If the text is in a different language, you can pass the corresponding language code. See example below for Italian text.
ai = AI("L'India, ufficialmente Repubblica dell'India, è uno Stato federale dell'Asia meridionale, con capitale Nuova Delhi.",lang.ITALIAN)

#For the latest updated list of languages supported by Gurunudi for sentence extraction visit https://gurulaghu.com/languages/
