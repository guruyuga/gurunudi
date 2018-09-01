#!/usr/bin/env python

from __future__ import division, print_function, absolute_import

#***************************** CONTEXT QA ************************************/
#  
#  This example shows how to query Gurunudi with a Context
#  
#***************************** CONTEXT QA ************************************/

from gurunudi import AI,lang

#AI is the wrapper class to call Gurunudi AI API

ai = AI()

#default language is English. First argument is the context text and second argument is the question within the given context.
answer = ai.contextqa('GuruLaghu Technologies is a technology company specializing in the field of Artificial Intelligence. It is based out of Bengaluru, India. Its motto is, "AI to the last man". Gurudev Rao is the founder and CEO of GuruLaghu. He is also the developer of Gurunudi.',"who is the developer of Gurunudi")
print(answer)

#if language other than English, then specify
answer = ai.contextqa("GuruLaghu Technologies est une technologie spécialisée dans le domaine de l'intelligence artificielle. Il est basé à Bangalore, en Inde. Sa devise est \"AI au dernier homme\". Gurudev Rao est le fondateur et PDG de GuruLaghu. Il est également le développeur de Gurunudi.","qui est le développeur de Gurunudi",lang.FRENCH)
print(answer)

#For the latest updated list of languages supported by Gurunudi for Context QA visit https://gurulaghu.com/languages/
