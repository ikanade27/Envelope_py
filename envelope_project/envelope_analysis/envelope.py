#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

def envelop(Vth, Vsignal, threshold):  
    """
    Detect envelope maxima and minima based on threshold crossing.

    Parameters
    ----------
    Vth : array-like
        Independent variable (e.g., voltage, time).
    Vsignal : array-like
        Dependent signal.
    threshold : float
        Threshold for slope change detection.

    Returns
    -------
    idx_max, Vsig_max, idx_min, Vsig_min : lists
        Indices and values of detected maxima and minima.
    """
    length = len(Vth)
    arr1, arr2 = [0], [0]
    idx_max, Vsig_max = [], []
    idx_min, Vsig_min = [], []

    for i in range(1, length):
        diff = Vth[i] - Vth[i-1]
        if diff >= threshold and i != arr2[-1] + 1:
            avg = np.mean(Vsignal[int(arr1[-1] + (i - arr1[-1]) / 2):i])
            idx_max.append(int(arr1[-1] + ((i - arr1[-1]) * 3/4)))
            Vsig_max.append(avg)
            arr1.append(i)
        elif diff <= -threshold and i != arr1[-1] + 1:
            avg = np.mean(Vsignal[int(arr2[-1] + (i - arr2[-1]) / 2):i])
            idx_min.append(int(arr2[-1] + ((i - arr2[-1]) * 3/4)))
            Vsig_min.append(avg)
            arr2.append(i)
    return idx_max, Vsig_max, idx_min, Vsig_min

