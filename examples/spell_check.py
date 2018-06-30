#!/usr/bin/env python

#***************************** SPELL CHECK ******************************/
#
#  This example shows how to fix spelling errors in a text using Gurunudi AI
#  For example, "whois cming tmrrow" will be fixed as "who is coming tomorrow"
#
#***************************** SPELL CHECK ******************************/


from gurunudi import AI,api,lang

#First setup your API key. This needs to be done only once at the beginning in an application. 
#Visit https://gurulaghu.com to get an API key
api.key="<YOUR_GURUNUDI_API_KEY>" 

#AI is a class with simple yet intelligent attributes. Create an AI object by passing your document text as the argument to the constructor.
ai = AI("whois cming")

#The AI attribute "spell_check" prints the corrected text
print(ai.spell_checked_text)

#The AI attribute "spell_check" returns a list of spelling suggestions for the given text
print(ai.spell_check)

#If there was any error during the attribute call, then ai.latest_error will contain the error string, else it will be None
#if ai.spell_check returns None i.e. if spell check API fails, then check this value for the corresponding error message
assert(ai.latest_error==None)

#By default the text is assumed to be in English language. If the text is in a different language, you can pass the corresponding language code. See example below for French text.
ai = AI("Emmanuel Macron est le président de la France.",lang.FRENCH)

#For the latest updated list of languages supported by Gurunudi for spell check visit https://gurulaghu.com/languages/
