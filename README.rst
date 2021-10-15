Gurunudi AI API: Python client
******************************

**Gurunudi** is a Python library for accessing the `Gurunudi Artificial Intelligence Chatbot API <https://www.gurunudi.com/>`_.
Gurunudi (**AI as a Service**) provides a wide range of **Artificial Intelligence based API solutions** (See below).

💫 **Version 2.0.3 out now!**
💫 Test `Gurunudi chatbot <https://www.gurunudi.com/>`_ online. 
💫 Get your API key today to use Gurunudi AI API in your own chatbot.
💫 Contact us if you need to train and deploy your own model with Gurunudi as the base model.
💫 For commercial use (an affordable, pay as you go pricing model), `Contact us <mailto:contact@gurunudi.com>`_ or `Tweet us <https://twitter.com/gurunudi>`_.

.. image:: https://img.shields.io/pypi/v/gurunudi.svg?style=flat-square
    :target: https://pypi.python.org/pypi/gurunudi
    :alt: pypi Version

.. image:: https://badges.gitter.im/guruyuga/gurunudi.svg
    :target: https://gitter.im/guruyuga/gurunudi
    :alt: Gurunudi on Gitter 

.. image:: https://img.shields.io/twitter/follow/gurunudi.svg?style=social&label=Follow
    :target: https://twitter.com/gurunudi
    :alt: gurunudi on Twitter

📖 Installation
================

==================== ===
**Operating system** macOS / OS X, Linux, Windows
**Python version**   2+, 3+
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

.. _GitHub Issue Tracker: https://github.com/guruyuga/gurunudi/issues
.. _StackOverflow: http://stackoverflow.com/questions/tagged/gurunudi
.. _Gitter Chat: https://gitter.im/guruyuga/gurunudi

Features of Gurunudi
====================

* Not just English, support exists for an ever growing list of languages.
* Pre-trained models that are continuously updated for better accuracy and to support more languages.
* Automatic Language Detection enables Gurunudi to converse in any supported language without any additional setup.
* Custom model training to deploy your own chatbot to answer your customer queries.
* Gurunudi is language agnostic - Train once in one language, and Gurunudi will reply in any of the supported languages.
* Knowledge Graph - continuously updated to provide latest and accurate information.
* More cutting edge AI features are being added continuously


📖 Documentation
================

Basics
------

.. code:: python

    from gurunudi import AI

    ai=AI('your_gurunudi_api_key')

AI is the class that abstracts API calls to Gurunudi AI Platform. Create an AI object as shown above. The only argument to be passed to the constructor is your Gurunudi API Key.

.. code:: python

    response=ai.chat("father of Albert Einstein")
    #now response = {"text": "Hermann Einstein is the father of Albert Einstein."}

Automatic Language Detection
----------------------------

Automatic language detection means you do not have to change anything in your code, even if the language is not English.
In the below example, we pass "como estas" (meaning "how are you" in Spanish language) as input text. Gurunudi automatically replies in Spanish saying Estoy bien (meaning "I am fine" in Spanish).

    response=ai.chat("como estas")
    #now response = {"text": "Estoy bien"}    

Custom Model Training
---------------------

You can also train your own custom model on top of Gurunudi. This can be useful if you want to deploy your own chatbot to answer queries from your customers about your products or services.
Since the model will be trained on top of Gurunudi, your customers will also be able to ask for generic information.
