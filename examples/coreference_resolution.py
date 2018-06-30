#!/usr/bin/env python

#************************************* CO-REFERENCE RESOLUTION ************************************/
#  
#  This example shows how to resolve co-references in a text using Gurunudi AI
#  For example: In the text "Delhi is in India. It is a big city.", the pronoun "It" refers to "Delhi"
#  So after resolving co-referneces, the text would become "Delhi is in India. Delhi is a big city."
#  
#************************************* CO-REFERENCE RESOLUTION ************************************/


from gurunudi import AI,api,lang

#First setup your API key. This needs to be done only once at the beginning in an application. 
#Visit https://gurulaghu.com to get an API key
api.key="<YOUR_GURUNUDI_API_KEY>" 

#AI is a class with simple yet intelligent attributes. Create an AI object by passing your document text as the argument to the constructor.
ai = AI("The women stopped taking pills because they were pregnant.")

#The AI attribute "coreferenced_text" returns coreference resolved version of the original text
assert(ai.coreferenced_text=="The women stopped taking pills because the women were pregnant.")

#If there was any error during the attribute call, then ai.latest_error will contain the error string, else it will be None
#if ai.coreferenced_text returns None i.e. if coreference resolution API fails, then check this value for the corresponding error message
assert(ai.latest_error==None)

#By default the text is assumed to be in English language. If the text is in a different language, you can pass the corresponding language code. See example below for Italian text.
ai = AI("L'India, ufficialmente Repubblica dell'India, è uno Stato federale dell'Asia meridionale, con capitale Nuova Delhi.",lang.ITALIAN)

#For the latest updated list of languages supported by Gurunudi for co-reference resolution visit https://gurulaghu.com/languages/
