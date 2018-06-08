Gurunudi: The official Python client for Gurunudi AI API by GuruLaghu Technologies
**********************************************************************************

**Gurunudi** is a Python library by `GuruLaghu Technologies <https://gurulaghu.com/>`_ for accessing the `Gurunudi AI API <https://www.gurunudi.com/>`_.
Gurunudi (**AI as a Service**) provides a wide range of **Artificial Intelligence based API solutions** (See below). This client library for Gurunudi AI API is commercial open-source software, released under the MIT license.

.. image:: https://badges.gitter.im/gurulaghu/gurunudi.svg
    :target: https://gitter.im/gurulaghu/gurunudi
    :alt: Gurunudi on Gitter 
`Gurunudi on Twitter <https://twitter.com/gurulaghu>`_


📖 Installation
================

===================  ===
**Operating system** macOS / OS X, Linux, Windows
**Python version**   3.4+ (not tested in earlier versions)
**Package managers** `pip`_ (source packages only)
===================  ===

.. _pip: https://pypi.python.org/pypi/gurunudi

pip
---

Using pip, gurunudi releases are currently only available as source packages.

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

    pip install -U gurunudi

📖 Documentation
================

Chatbot
--------

.. code:: python

    from gurunudi import ai
    response = ai('how are you?').chat #returns a string ex: "I am fine"
    response = ai('where is Badami').chat #returns a string ex: "in Karnataka, India"
    response = ai('do you eat cakes?').chat #returns a string ex: "softwares do not eat"
    response = ai('solve 3x-12=0').chat #returns a string ex: "4"

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

Features of Gurunudi AI API
===========================

* Not just English, Support exists for an ever growing list of **100+** `languages <https://gurulaghu.com/languages/>`
* Pre-trained models that are continuously updated for better accuracy.
* Wide range of AI APIs solving different AI problems.
