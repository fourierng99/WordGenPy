import numpy as np
import pandas as pd
import random

ENG_INPUT_PATH = 'eng\English Wordlist.csv'
DEU_INPUT_PATH = 'deu\GoetheA1.csv'
JAP_INPUT_PATH = 'eng\AdvanceIELTS.csv'

input_df = pd.read_csv(JAP_INPUT_PATH, header=0, encoding='latin-1')