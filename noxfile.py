import tempfile

import nox


nox.options.sessions = 'lint', 'mypy', 'tests'
locations = 'nb_query', 'tests', 'noxfile.py'


def install_with_constraints(session, *args, **kwargs):
    with tempfile.NamedTemporaryFile() as constraints:
        session.run(
            'poetry',
            'export',
            '--with=dev',
            '--format=constraints.txt',
            '--without-hashes',
            f'--output={constraints.name}',
            external=True,
        )
        session.install(f'--constraint={constraints.name}', *args, **kwargs)


@nox.session(python=['3.8'])
def tests(session):
    args = session.posargs or ['--cov']
    session.run('poetry', 'install', '--only=main', external=True)
    install_with_constraints(
        session, 'coverage[toml]', 'pytest', 'pytest-cov', 'pytest-mock'
    )
    session.run('pytest', *args)


@nox.session(python='3.8')
def black(session):
    args = session.posargs or locations
    install_with_constraints(session, 'black')
    session.run('black', *args)


@nox.session(python=['3.8'])
def lint(session):
    args = session.posargs or locations
    install_with_constraints(
        session,
        'flake8',
        'flake8-bandit',
        'flake8-black',
        'flake8-bugbear',
        'flake8-import-order',
    )
    session.run('flake8', *args)


@nox.session(python=['3.8'])
def mypy(session):
    args = session.posargs or locations
    install_with_constraints(session, 'mypy')
    session.run('mypy', *args)
