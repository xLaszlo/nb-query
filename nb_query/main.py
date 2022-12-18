"""Function to search in selected notebooks with keywords, regex or functions."""
import json
import os
import re
from typing import Callable, List, Optional, Union

import pandas as pd
import typer

app = typer.Typer()


@app.command()
def main(query: str, fnames: Optional[str] = None) -> None:
    """Command line wrapper for Typer. Searches all files in the given directories.

    Args:
        query (str): Keyword, regex expression or function
        fnames (Optional[str], optional): directory to search.
            Defaults to current directory.
    """
    result = nb_query(query, fnames)
    print(result)


def nb_query(
    query: Union[str, Callable], fnames: Union[None, str, List[str]] = None
) -> pd.DataFrame:
    """Function to search in selected notebooks with keywords, regex or functions.

    Args:
        query (str): Keyword, regex expression or function
        fnames:
            str: directory to search (recursively).
            None: current directory
            List[str]: list of notebooks to search

    Returns:
        pd.DataFrame: Table of results: notebook location, line matching the query,
        cell number and cell count
    """
    if isinstance(query, str):
        query_fun = lambda line: re.match(f'.*{query}.*', line)
    else:
        query_fun = query
    if fnames is None:
        fnames = '.'
    if isinstance(fnames, str):
        notebooks = []
        for dirname, _, fnames_ in os.walk(fnames):
            if '.ipynb_checkpoints' not in dirname:
                notebooks.extend(
                    [
                        f'{dirname}/{fname}'
                        for fname in fnames_
                        if fname.endswith('.ipynb')
                    ]
                )
    else:
        notebooks = fnames
    result = []
    for notebook in notebooks:
        for cell in json.loads(open(notebook).read())['cells']:
            for ind, line in enumerate(cell['source']):
                if query_fun(line.strip()):
                    result.append(
                        {
                            'fname': notebook,
                            'line': line.strip(),
                            'cell': ind,
                            'count': cell.get('execution_count') or 0,
                        }
                    )
    return pd.DataFrame(result)


# Usage:
#
# in notebooks:
#
# from nb_query import nb_query
# nb_query('he(ll|r)o')
#
# in CLI:
#
# python nb_query.py 'he(ll|r)o'
# python nb_query.py 'he(ll|r)o' --fnames '<notebook dir>'

if __name__ == '__main__':
    app()
