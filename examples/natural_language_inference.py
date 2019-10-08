#!/usr/bin/env python

from __future__ import division, print_function, absolute_import

#***************************** NATURAL LANGUAGE INFERENCE - NLI ************************************/
#  
#  This example shows how to query Gurunudi to infer or extract additional information from a text
#  
#***************************** NATURAL LANGUAGE INFERENCE - NLI ************************************/

from gurunudi import AI,lang

#AI is the wrapper class to call Gurunudi AI API
ai = AI()

response = ai.inferences("Larry Page was doing his Phd at Stanford University in 1996.")
print(response)
 
response = ai.inferences("Emmanuel Macron est le président de la France.",lang.FRENCH)
print(response)

#For the latest updated list of languages supported by Gurunudi for named entities recognition visit https://guruyuga.com/languages/

