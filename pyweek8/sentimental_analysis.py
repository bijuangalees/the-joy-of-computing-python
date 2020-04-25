# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:38:48 2020

@author: bijuangalees
"""

import pandas as pd
import nltk
from nltk.sentiment.vader import Sentimen
nltk.downloader.download('vader_lexicon)
file='data_file.xslsx'
xl=pdExcelFile(file) #Read from excel