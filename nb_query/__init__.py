"""Function to search in selected notebooks with keywords, regex or functions."""
from importlib.metadata import version


__version__ = version(__name__)

from .main import nb_query
