import re
import os
import json
import typer
import pandas as pd

app = typer.Typer()

@app.command()
def main(query, fnames=None):
    result = nb_query(query, fnames)
    print(result)

def nb_query(query, fnames=None):
    if isinstance(query, str):
        query_fun = lambda line: re.match(f'.*{query}.*', line)
    else:
        query_fun = query
    if fnames is None:
        fnames = '.'
    if isinstance(fnames, str):
        fnames = sum([
            [f'{dirname}/{fname}' for fname in fnames_ if fname.endswith('.ipynb')]
            for dirname, _, fnames_ in os.walk(fnames) if '.ipynb_checkpoints' not in dirname
        ], [])
    res = []
    for fname in fnames:
        for cell in json.loads(open(fname).read())['cells']:
            for ind, line in enumerate(cell['source']):
                if query_fun(line.strip()):
                    res.append({
                        'fname': fname,
                        'line': line.strip(),
                        'cell': ind,
                        'count': cell.get('execution_count') or 0
                    })
    return pd.DataFrame(res)


# Usage:
#
# in notebooks:
#
# from nb_query import nb_query
# nb_query('he(ll|r)o')
#
# in CLI:
#
# python nb_query.py "he(ll|r)o"
# python nb_query.py "he(ll|r)o" --fnames "<notebook dir>"

if __name__ == "__main__":
    app()
