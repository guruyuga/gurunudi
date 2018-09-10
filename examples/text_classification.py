#!/usr/bin/env python

from __future__ import division, print_function, absolute_import

#***************************** TEXT CLASSIFICATION ************************************/
#  
#  This example shows how to query Gurunudi to identify language of a text
#  
#***************************** TEXT CLASSIFICATION ************************************/

from gurunudi import AI,lang

#AI is the wrapper class to call Gurunudi AI API
ai = AI()

response = ai.classify("John ate an apple.","tense")
print(response)

response = ai.classify("Where are you going?.","mood")
print(response)

response = ai.classify("Einstein discovered relativity.","mood")
print(response)

response = ai.classify("You have won 1 million dollars","email")
print(response)

response = ai.classify("India wins the ICC world cup","news")
print(response)
 
response = ai.classify("that movie was really bad","sentiment")
print(response)


#For the latest updated list of languages supported by Gurunudi for text classification visit https://gurulaghu.com/languages/




 
