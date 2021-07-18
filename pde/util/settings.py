import os

UTIL_PATH = os.path.dirname(__file__)
CODE_PATH = os.path.abspath(os.path.join(UTIL_PATH, '..'))
TOP_LEVEL_DIR = os.path.abspath(os.path.join(CODE_PATH, '..'))
DATA_PATH = os.path.join(TOP_LEVEL_DIR, 'data')