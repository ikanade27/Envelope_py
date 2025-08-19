#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
Envelope Analysis Package

Tools for:
- Loading signal data
- Detecting upper and lower envelopes
- Preprocessing
- Symmetrization / analysis
- Plotting
"""

from .io import splitfile
from .envelope import envelop
from .preprocessing import remove_outliers_zscore, interpolate_signal
from .analysis import symmetrize_data, antisymmetrize_data, envelope_difference
from .plotting import plot_envelopes

__all__ = [
    "splitfile",
    "envelop",
    "remove_outliers_zscore",
    "interpolate_signal",
    "symmetrize_data",
    "antisymmetrize_data",
    "envelope_difference",
    "plot_envelopes",
]

