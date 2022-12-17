Search in Jupyter Notebooks
===========================

Testing out the techniques in the
`Hypermodern Python <https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769>`_
article series.

Join the `Code Quality for Data Science (CQ4ds) Discord channel <https://discord.com/invite/8uUZNMCad2>`_

The command-line interface prints a pandas dataframe to the console.


Installation
------------

To install the package,
run this command in your terminal:

.. code-block:: console

   $ pip install nb-query


Usage
-----

Notebook Query's usage looks like:

.. code-block:: bash

   $ nb-query [QUERY]

.. option:: --help

   Display a short usage message and exit.

Usage in notebooks
------------------

.. code-block:: python

   from nb_query import nb_query
   nb_query('Hello')
   nb_query('Hello', 'data/notebooks')
   nb_query('He(ll|r)o')
   nb_query(lambda line: len(line) == 2)


.. toctree::
   :hidden:
   :maxdepth: 2

   license
   reference
