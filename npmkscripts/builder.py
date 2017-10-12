# -*- coding: utf-8 -*-
"""Main module for plotting and visualize operations."""

import numpy as np
import cv2
import matplotlib.pyplot as plt
from .nevdata import load_neural_data, divide_by_electrode_and_unit, build_df
from .mea import get_soft_index_from_mea_index
from .io import build_video, remove_files
from .utils import get_name_from_dataset

__all__ = ['plot_spike_raster', 'generate_video']


def plot_spike_raster(dataset_path, electrodes=None):
    # Load data
    neural_data = load_neural_data(dataset_path)
    data = divide_by_electrode_and_unit(neural_data)

    # Plot each electrode spike raster
    for idx, (key, value) in enumerate(data.items()):
        if electrodes is None or key[0] in electrodes:
            x = value
            y = np.ones(x.size) * (idx + 1)
            plt.scatter(x, y, s=1, lw=0)
            plt.text(-1, idx + 1, key)

    plt.title(get_name_from_dataset(dataset_path))
    plt.xlabel('Time (ms)')
    plt.ylabel('Electrode')
    plt.show()


def generate_spike_raster(dataset_path, output_path, electrodes=None):
    # Load data
    neural_data = load_neural_data(dataset_path)
    data = divide_by_electrode_and_unit(neural_data)

    # Plot each electrode spike raster
    for idx, (key, value) in enumerate(data.items()):
        if electrodes is None or key[0] in electrodes:
            x = value
            y = np.ones(x.size) * (idx + 1)
            plt.scatter(x, y, s=1, lw=0)
            plt.text(-1, idx + 1, key)

    plt.title(get_name_from_dataset(dataset_path))
    plt.xlabel('Time (ms)')
    plt.ylabel('Electrode')
    plt.savefig(output_path + 'raster-' + get_name_from_dataset(dataset_path) + '.pdf')
    plt.clf()


def save_spike_raster(dataset_path, output_path):
    # Load data
    neural_data = load_neural_data(dataset_path)
    data = build_df(neural_data)
    data.to_csv(output_path + 'data-spikes-' + get_name_from_dataset(dataset_path) + '.csv', index=False)


def generate_video(dataset_path, output_path, fps=60, step_ms=17, mea_size=10, image_size=500):
    # Output
    output_folder = output_path
    output_file = 'reconstruction-' + get_name_from_dataset(dataset_path)
    output_ext = '.png'
    output_video_ext = '.avi'

    # Parameters
    idx = 0
    time_counter = 0
    output_value = 255

    # Load data
    neural_data = load_neural_data(dataset_path)

    print('Loop...')
    while time_counter < neural_data.spikes[-1]:
        indexes = np.where(np.logical_and(neural_data.spikes >= time_counter,
                                          neural_data.spikes < time_counter + step_ms))
        electrodes = neural_data.electrode[indexes[0]]

        stimulus = np.zeros((mea_size ** 2), dtype='uint8')
        for electrode in electrodes:
            soft_index = get_soft_index_from_mea_index(electrode)
            stimulus[soft_index] = 1

        # Stimulus frame
        stimulus = output_value * stimulus
        image = stimulus.reshape(mea_size, mea_size)
        stimulus_image = cv2.resize(image, (image_size, image_size), fx=0, fy=0, interpolation=cv2.INTER_NEAREST)
        cv2.imwrite(output_folder + output_file + str(idx) + output_ext, stimulus_image)

        idx += 1
        time_counter += step_ms

    # Video file
    print('Build video file...')
    build_video(output_folder, output_video_ext, output_file, output_ext, fps)

    # Remove temporal images
    print('Remove temporal files...')
    remove_files(path=output_folder, file_ext=output_ext)
