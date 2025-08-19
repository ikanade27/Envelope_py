#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt

def plot_envelopes(x, y, idx_max, Vsig_max, idx_min, Vsig_min, show_original=True):
    """
    Plot signal with detected upper and lower envelopes.
    """
    plt.figure(figsize=(10, 6))
    if show_original:
        plt.plot(x, y, label='Original Signal')
    plt.plot(idx_max, Vsig_max, 'r--', label='Upper Envelope')
    plt.plot(idx_min, Vsig_min, 'g--', label='Lower Envelope')
    plt.xlabel("X")
    plt.ylabel("Signal")
    plt.title("Envelope Detection")
    plt.legend()
    plt.grid(True)
    plt.show()

