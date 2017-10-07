# -*- coding: utf-8 -*-
"""Script file for manage the Blackrock Microsystems data files (.NEV)."""

import scipy.io as sio
import numpy as np
import pandas as pd


def load_neural_data(path, sampling_freq=30.0):
    data = sio.loadmat(path)['NEV']
    data = data[0]
    data = data['Data']

    # Spike data
    spike_data = data[0][0][0][1][0][0]
    timestamp = np.array(spike_data[0][0])
    electrode = np.array(spike_data[1][0])
    unit = np.array(spike_data[2][0])

    # Trigger data
    trigger = np.array(data[0][0][0][0][0][0][2][0])

    # Get spike milliseconds from timestamp
    spikes = timestamp / sampling_freq

    return NeuralData(spikes, electrode, unit, trigger)


def divide_by_electrode(neural_data):
    data = {}

    electrodes = np.unique(neural_data.electrode)
    for electrode in electrodes:
        indexes = np.where(neural_data.electrode == electrode)
        data[electrode] = neural_data.timestamp[indexes]

    return data


def divide_by_electrode_and_unit(neural_data):
    data = {}
    df = pd.DataFrame({'s': neural_data.spikes, 'e': neural_data.electrode, 'u': neural_data.unit})
    grouped_data = df.groupby(['e', 'u'])['s']

    for key, value in grouped_data:
        data[key] = np.array(value)

    return data


def build_df(neural_data):
    return pd.DataFrame({'Spikes': neural_data.spikes,
                         'Electrode': neural_data.electrode,
                         'Unit': neural_data.unit})


class NeuralData(object):
    def __init__(self, spikes, electrode, unit, trigger):
        self.__spikes = spikes
        self.__electrode = electrode
        self.__unit = unit
        self.__trigger = trigger

    @property
    def spikes(self):
        return self.__spikes

    @property
    def electrode(self):
        return self.__electrode

    @property
    def unit(self):
        return self.__unit

    @property
    def trigger(self):
        return self.__trigger

    @spikes.setter
    def timestamp(self, spikes):
        self.__spikes = spikes

    @electrode.setter
    def electrode(self, electrode):
        self.__electrode = electrode

    @unit.setter
    def unit(self, unit):
        self.__unit = unit

    @trigger.setter
    def trigger(self, trigger):
        self.__trigger = trigger
