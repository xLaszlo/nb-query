# nb_query

Python package to search in Jupyter notebooks.

[![Tests](https://github.com/xLaszlo/nb-query/workflows/Tests/badge.svg)](https://github.com/xLaszlo/nb-query/actions?workflow=Tests)
[![Codecov](https://codecov.io/gh/xLaszlo/nb-query/branch/master/graph/badge.svg)](https://codecov.io/gh/xLaszlo/nb-query)
[![PyPI](https://img.shields.io/pypi/v/nb-query.svg)](https://pypi.org/project/nb-query/)
[![Read the Docs](https://readthedocs.org/projects/nb-query/badge/)](https://nb-query.readthedocs.io/)

Installation:

```
    $ pip install nb-query
```

Usage

```
    >>  from nb_query import nb_query
    >>  nb_query('Hello')
    >>  nb_query('Hello', ['data/notebooks',])
    >>  nb_query('He(ll|r)o')
    >>  nb_query(lambda line: len(line) == 2)
```

Created with the help of the "Hypermodern python" article series.

Join the [Code Quality for Data Science (CQ4ds) Discord channel](https://discord.com/invite/8uUZNMCad2) for feedback.
