#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

def symmetrize_data(x, y):
    """
    Symmetrize data (average signal with its mirror).
    """
    return (y + y[::-1]) / 2

def antisymmetrize_data(x, y):
    """
    Antisymmetrize data (subtract mirrored signal).
    """
    return (y - y[::-1]) / 2

def envelope_difference(upper, lower):
    """
    Compute difference between upper and lower envelope.
    """
    return np.array(upper) - np.array(lower)

