# -*- coding: utf-8 -*-
"""Helper script for data visualization."""

import npmkscripts
from npmkscripts import utils
from npmkscripts import builder
from npmkscripts import io


def create_experiment_output_folder():
    root_output_folder = 'output/'
    io.create_folder(root_output_folder)

    output = root_output_folder + 'reconstruction-' + utils.get_datetime() + '/'
    io.create_folder(output)
    return output


if __name__ == '__main__':
    utils.check_python_version()

    # Info
    print('NPMK-scripts: A collection of useful scripts to manage the Blackrock Microsystems data files (.NEV).')
    print('Version: {}'.format(npmkscripts.__version__))

    # Plot data
    dataset_path = '/home/rcc/Recordings/20170918-umhcristinaexp/refixationaleyemovementsdatosexperimentales/mat-data/'

    print('Experiment 1.')
    file = 'barras_black_on_white_sorted.mat'
    output_path = create_experiment_output_folder()

    builder.generate_spike_raster(dataset_path + file, output_path)
    builder.generate_video(dataset_path + file, output_path)

    print('Experiment 2.')
    file = 'barras_white_on_black1_sorteado.mat'
    output_path = create_experiment_output_folder()

    builder.generate_spike_raster(dataset_path + file, output_path)
    builder.generate_video(dataset_path + file, output_path)

    print('Experiment 3.')
    file = 'barras_white_on_black2_sorteado.mat'
    output_path = create_experiment_output_folder()

    builder.generate_spike_raster(dataset_path + file, output_path)
    builder.generate_video(dataset_path + file, output_path)

    print('Experiment 4.')
    file = 'barras_white_on_black_sorteado.mat'
    output_path = create_experiment_output_folder()

    builder.generate_spike_raster(dataset_path + file, output_path)
    builder.generate_video(dataset_path + file, output_path)

    print('Experiment 5.')
    file = 'fixational1_sorteado.mat'
    output_path = create_experiment_output_folder()

    builder.generate_spike_raster(dataset_path + file, output_path)
    builder.generate_video(dataset_path + file, output_path)

    print('Experiment 6.')
    file = 'fixational_sorteado.mat'
    output_path = create_experiment_output_folder()

    builder.generate_spike_raster(dataset_path + file, output_path)
    builder.generate_video(dataset_path + file, output_path)
