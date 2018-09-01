Gurunudi AI API: Python client
******************************

**Gurunudi** is a Python library by `GuruLaghu Technologies <https://gurulaghu.com/>`_ for accessing the `Gurunudi Artificial Intelligence API <https://www.gurunudi.com/>`_.
Gurunudi (**AI as a Service**) provides a wide range of **Artificial Intelligence based API solutions** (See below). This client library for Gurunudi AI API is commercial open-source software, released under the Apache-2.0 license.

💫 **Version 1.3 out now!**

.. image:: https://img.shields.io/pypi/v/gurunudi.svg?style=flat-square
    :target: https://pypi.python.org/pypi/gurunudi
    :alt: pypi Version

.. image:: https://badges.gitter.im/gurulaghu/gurunudi.svg
    :target: https://gitter.im/gurulaghu/gurunudi
    :alt: Gurunudi on Gitter 

.. image:: https://img.shields.io/twitter/follow/gurunudi.svg?style=social&label=Follow
    :target: https://twitter.com/gurunudi
    :alt: gurunudi on Twitter

📖 Installation
================

==================== ===
**Operating system** macOS / OS X, Linux, Windows
**Python version**   2+
**Package managers** `pip <https://pypi.python.org/pypi/gurunudi>`_
==================== ===

via pip
-------

.. code:: bash

    pip install gurunudi

When using pip it is generally recommended to install packages in a virtual environment to avoid modifying system state:

.. code:: bash

    venv .env
    source .env/bin/activate
    pip install gurunudi

Updating
--------

.. code:: bash

    pip install gurunudi --upgrade

💬 Where to ask questions
==========================

The Gurunudi project is maintained by `@gurudevrao <https://github.com/gurudevrao>`_. Please use the below listed forums for any support requests.

====================== ===
**Bug Reports**        `GitHub Issue Tracker`_
**Usage Questions**    `StackOverflow`_, `Gitter Chat`_
**General Discussion** `Gitter Chat`_
====================== ===

.. _GitHub Issue Tracker: https://github.com/gurulaghu/gurunudi/issues
.. _StackOverflow: http://stackoverflow.com/questions/tagged/gurunudi
.. _Gitter Chat: https://gitter.im/gurulaghu/gurunudi

Features of Gurunudi
====================

* Not just English, support exists for an ever growing list of **100+** `languages <https://gurulaghu.com/languages/>`
* Pre-trained models that are continuously updated for better accuracy and to support more languages.
* Text Classification - Language Detection, Sentiment Analysis, Topic Modeling, Text Classification and more 
* Text Analysis - Named Entities, Sentence Extraction, Syntax Analysis, Dependency Parse Tree, Keyword Extraction, Intent Extraction and more 
* Text Generation - Chatbot, Summarization, Title Generation, Translation and more
* Text Transformation - Co-reference Resolution, Fix Case (True Case), Spell Check and more
* Knowledge Graph - Definition and Knowledge queries
* Custom Trained Bots - Domain Experts, Customer Support, FAQ and more
* More cutting edge AI features are being added continuously


📖 Documentation
================

Basics
------

.. code:: python

    from gurunudi import AI

    ai=AI()

AI is a class that abstracts API calls to Gurunudi AI System. Create an AI object as shown above. Except for language detection API call, all other text based API calls take an additional optional argument as the language code which if not present, defaults to English (except for language detection call). The language code is a 3-letter `ISO 639-3 code <https://en.wikipedia.org/wiki/List_of_ISO_639-3_codes>`_. For language codes and features currently supported by each language, see `supported languages <https://gurulaghu.com/languages/>`_.

.. code:: python

    from gurunudi import lang
    definition=ai.define("ಕನ್ನಡ",lang.KANNADA) #Specify the language if non-English text

Autocorrect / Spell Check
-------------------------

.. code:: python

    corrected_text = ai.autocorrect("whois cming tmorrow")
    #now corrected_text = "who is coming tomorrow"



Autocomplete
-------------------------

.. code:: python

    completed_text = ai.autocomplete("which is the fas")
    #now completed_text = "which is the fastest car"


Chatbot
-------

.. code:: python

    response = ai.chat("how are you?") #returns a string ex: "I am fine"
    response = ai.chat("where is Badami") #returns a string ex: "in Karnataka, India"
    response = ai.chat("do you eat cakes?") #returns a string ex: "software do not eat"
    response = ai.chat("solve 3x-12=0") #returns a string ex: "4"


Co-reference Resolution
-----------------------

.. code:: python

    coreferenced_text = ai.coref("Einstein was a brillian scientist. He was born in Germany.")
    #now coreferenced_text = "Einstein was a brillian scientist. Einstein was born in Germany."

    coreferenced_text = ai.coref("The women stopped taking pills because they were pregnant.")
    #now coreferenced_text = "The women stopped taking pills because the women were pregnant"


Context QA
----------

.. code:: python

    answer = ai.contextqa('GuruLaghu Technologies is a technology company specializing in the field of Artificial Intelligence. It is based out of Bengaluru, India. Its motto is, "AI to the last man". Gurudev Rao is the founder and CEO of GuruLaghu. He is also the developer of Gurunudi.',"who is the developer of Gurunudi") 
    #now answer="Gurudev Rao"


Definition
----------

.. code:: python

    definition = ai.define("sun")
    #now definition = "the star that is the source of light and heat for the planets in the solar system"


Fix Case (True Case)
--------------------

.. code:: python

    case_fixed_text = ai.fix_case("delhi is the capital of iNdia")
    #now case_fixed_text = "Delhi is the capital of India"


Intent Extraction
-----------------

.. code:: python

    intent = ai.intent("hi")
    #returns "[{"intent":"greeting"}]"

    intent = ai.intent("Delhi is in India")
    #returns [{"intent":"statement","theme":"Delhi","attribute":"location","value",:"India","tense":"present"}]

    intent = ai.intent("John went to Chicago")
    #returns [{"intent":"statement","agent":"John","action":"go","destination",:"Chicago","tense":"past"}]

    intent = ai.intent("book a flight to mumbai")
    #returns [{"intent":"command","action":"book","theme":"flight","destination":"Mumbai","tense":"present"}]

    intent = ai.intent("where is berlin?")
    #returns [{"intent":"query","theme":"Berlin","query_type":"attribute_value","attribute":"location","tense":"present"}]


Keyword Extraction
------------------

.. code:: python

    keywords = ai.keywords("Delhi is in India")
    #now keywords = ['India', 'Delhi']


Knowledge
------------------

.. code:: python

    answer = ai.knowledge("capital of india")
    #now answer = "New Delhi"


Language Detection
------------------

.. code:: python

    language = ai.language("lorem ipsum")
    #now language = {"iso1":"la","iso3":"lat","language":"Latin"}

    language = ai.language("ನನ್ನ ಹೆಸರು ಗುರು")
    #now language = {"iso1":"kn","iso3":"kan","language":"Kannada"}


Named Entities Extraction
-------------------------

.. code:: python

    named_entities = ai.named_entities("India is in Asia") #returns a list of named entities, their labels and position in the text
    #now named_entities = [{"label": "GPE", "end": 5, "start": 0, "name": "India"}, {"label": "LOC", "end": 16, "start": 12, "name": "Asia"}]


Sentence Extraction
-------------------

.. code:: python

    sentences = ai.sentences("Mr. India was a great movie. It was directed by Shekhar Kapur.")
    #now sentences = ["Mr. India was a great movie.", "It was directed by Shekhar Kapur."]


Sentiment Analysis
------------------

.. code:: python

    sentiment = ai.sentiment("I really did not like that movie")
    #now sentiment = "negative"

    sentiment = ai.sentiment ("she is very beautiful")
    #now sentiment = "positive"

    sentiment = ai.sentiment ("The ambience was good, but the food was bad")
    #now sentiment = "mixed"

    sentiment = ai.sentiment ("roses are red, violets are blue")
    #now sentiment = "neutral"


Summary Generation
------------------

.. code:: python

    summary = ai.summary("<SOME_LONG_TEXT>")
    #now summary = <summary_of_the_long_text>


Syntax Analysis
---------------

.. code:: python

    syntax = ai.syntax("Moon creates waves")
    #now syntax = [{'pos': 'PROPN', 'lemma': 'moon', 'text': 'Moon'}, {'pos': 'VERB', 'lemma': 'create', 'text': 'creates'}, {'pos': 'NOUN', 'lemma': 'wave', 'text': 'waves'}]


Syntax Dependency Parse Tree
----------------------------

.. code:: python

    syntax_tree = ai.dependency("Moon creates waves")
    #now syntax_tree = [{'head': 1, 'dep': 'nsubj', 'text': 'Moon'}, {'head': 1, 'dep': 'ROOT', 'text': 'creates'}, {'head': 1, 'dep': 'dobj', 'text': 'waves'}]


Title Generation
----------------

.. code:: python

    from gurunudi import lang

    title = ai.title("<SOME_LONG_TEXT>")
    #now title = "<TITLE_SUGGESTED_BY_GURUNUDI_AI>"


Topic Modeling
--------------

.. code:: python

    topics = ai.topics("Can Trump and Kim end the Korean War?")
    #now topics = ["Politics"]

    topics = ai.topics("Planning To Buy A House? There Is Good News For You")
    #now topics = ["Business"]


Translation
-----------

.. code:: python

    from gurunudi import lang

    translation = ai.translate("India",lang.ENGLISH,lang.GERMAN)
    #now translation = "Indien"
