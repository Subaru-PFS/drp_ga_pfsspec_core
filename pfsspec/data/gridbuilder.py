import os
import numpy as np
import time
from tqdm import tqdm

from pfsspec.pfsobject import PfsObject

class GridBuilder(PfsObject):
    def __init__(self, input_grid=None, output_grid=None, orig=None):
        super(GridBuilder, self).__init__()

        if isinstance(orig, GridBuilder):
            self.input_grid = input_grid if input_grid is not None else orig.input_grid
            self.output_grid = output_grid if output_grid is not None else orig.output_grid
            self.input_grid_index = None
            self.output_grid_index = None
            self.grid_shape = None

            self.top = orig.top
        else:
            self.input_grid = input_grid
            self.output_grid = output_grid
            self.input_grid_index = None
            self.output_grid_index = None
            self.grid_shape = None

            self.top = None

    def add_args(self, parser):
        parser.add_argument('--top', type=int, default=None, help='Limit number of results')

        # Axes of input grid can be used as parameters to filter the range
        grid = self.create_input_grid()
        grid.add_args(parser)

    def parse_args(self):
        self.top = self.get_arg('top', self.top)

    def create_input_grid(self):
        raise NotImplementedError()

    def create_output_grid(self):
        raise NotImplementedError()

    def open_data(self, input_path, output_path):
        # Open and preprocess input
        self.open_input_grid(input_path)
        self.input_grid.init_from_args(self.args)
        self.input_grid.build_axis_indexes()

        # Open and preprocess output
        self.open_output_grid(output_path)

        # Source indexes
        index = self.input_grid.grid.get_value_index_unsliced('flux')
        self.input_grid_index = np.array(np.where(index))

        # Target indexes
        index = self.input_grid.grid.get_value_index('flux')
        self.output_grid_index = np.array(np.where(index))

        self.grid_shape = self.input_grid.get_shape()

    def open_input_grid(self, input_path):
        raise NotImplementedError()

    def open_output_grid(self, output_path):
        raise NotImplementedError()

    def save_data(self, output_path):
        self.output_grid.save(self.output_grid.filename, format=self.output_grid.fileformat)

    def get_input_count(self):
        # Return the number of data vectors
        input_count = self.input_grid_index.shape[1]
        if self.top is not None:
            input_count = min(self.top, input_count)
        return input_count

    def init_process(self):
        pass

    def run(self):
        raise NotImplementedError()