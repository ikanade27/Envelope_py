#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

def splitfile(file, col1, col2, skiprows=1):
    """
    Load two columns from a CSV file.

    Parameters
    ----------
    file : str
        Path to the CSV file.
    col1, col2 : str
        Column names to extract.
    skiprows : int
        Number of header rows to skip.

    Returns
    -------
    sig1, sig2 : pandas.Series
        Extracted signals.
    """
    data = pd.read_csv(file, skiprows=skiprows)
    sig1 = data[col1]
    sig2 = data[col2]
    return sig1, sig2

