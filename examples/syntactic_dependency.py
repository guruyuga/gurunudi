#!/usr/bin/env python

#***************************** SYNTACTIC DEPENDENCY ******************************/
#  
#  This example shows how to create a dependency parse tree of a text using Gurunudi AI
#  Here, Gurunudi AI tokenizes the text and returns the head token of each token
#  and the dependency relation between the head and the child token
#  
#***************************** SYNTACTIC DEPENDENCY ******************************/


from gurunudi import AI,api,lang

#First setup your API key. This needs to be done only once at the beginning in an application. 
#Visit https://gurulaghu.com to get an API key
api.key="<YOUR_GURUNUDI_API_KEY>" 

#AI is a class with simple yet intelligent attributes. Create an AI object by passing your document text as the argument to the constructor.
ai = AI("Larry Page was doing his Phd at Stanford University in 1996.")

#The AI attribute "syntax_tree" returns a list containing the dependency parse tree for each sentence in the given text
print(ai.syntax_tree)

#If there was any error during the attribute call, then ai.latest_error will contain the error string, else it will be None
#if ai.syntax_tree returns None i.e. if syntactic dependency API fails, then check this value for the corresponding error message
assert(ai.latest_error==None)

#By default the text is assumed to be in English language. If the text is in a different language, you can pass the corresponding language code. See example below for French text.
ai = AI("Emmanuel Macron est le président de la France.",lang.FRENCH)

#For the latest updated list of languages supported by Gurunudi for syntactic dependency visit https://gurulaghu.com/languages/
