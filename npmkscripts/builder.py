# -*- coding: utf-8 -*-
"""Main module for plotting and visualize operations."""

import numpy as np
import os
import matplotlib.pyplot as plt
from .nevdata import load_neural_data, divide_by_electrode


__all__ = ['plot_spike_raster']


def plot_spike_raster(path):
    # Load data
    neural_data = load_neural_data(path)
    data = divide_by_electrode(neural_data)

    for idx, (key, value) in enumerate(data.items()):
        x = value
        y = np.ones(x.size) * (idx + 1)
        plt.scatter(x, y, s=4, c='b', lw=0)
        plt.text(-1, idx+1, key)

    plt.title(os.path.basename(path))
    plt.xlabel('Time (ms)')
    plt.ylabel('Electrode')
    plt.show()
