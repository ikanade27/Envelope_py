#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from scipy import interpolate
from scipy.stats import zscore

def remove_outliers_zscore(x, y, threshold=3):
    """
    Remove outliers based on z-score.

    Returns
    -------
    x_clean, y_clean : arrays
        Filtered data.
    """
    z = zscore(y)
    mask = np.abs(z) < threshold
    return x[mask], y[mask]

def interpolate_signal(x, y, kind='linear'):
    """
    Interpolate signal for smoother envelope processing.
    """
    f = interpolate.interp1d(x, y, kind=kind, fill_value="extrapolate")
    x_new = np.linspace(np.min(x), np.max(x), len(x))
    y_new = f(x_new)
    return x_new, y_new

