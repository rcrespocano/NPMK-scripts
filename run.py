# -*- coding: utf-8 -*-
"""Helper script for data visualization."""

import npmkscripts
from npmkscripts import utils
from npmkscripts import builder


if __name__ == '__main__':
    utils.check_python_version()

    # Info
    print('NPMK-scripts: A collection of useful scripts to manage the Blackrock Microsystems data files (.NEV).')
    print('Version: {}'.format(npmkscripts.__version__))

    # Plot data
    path = '/home/rcc/Desktop/umh-data.mat'
    builder.plot_spike_raster(path)
