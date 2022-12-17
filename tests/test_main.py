from typer.testing import CliRunner

from nb_query.main import app

runner = CliRunner()

EXPECTED_STDOUT = """                                  fname           line  cell  count
0  ./tests/NB_Query_Test_Notebook.ipynb  "Hello World"     0      1"""


def test_app():
    result = runner.invoke(app, ['Hello'])
    assert result.exit_code == 0
    assert EXPECTED_STDOUT in result.stdout
