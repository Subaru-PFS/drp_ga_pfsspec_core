import numpy as np

from ..util.dist import get_random_dist
from ..util.args import *

class ParameterSampler():
    def __init__(self, random_state=None, orig=None):
        if not isinstance(orig, ParameterSampler):
            self.random_state = random_state
            self.parameters = {}
            self.sample_count = 0               # Number of samples to generate
                                                # TODO: move this elsewhere?
        else:
            self.random_state = random_state if random_state is not None else orig.random_state
            self.parameters = orig.parameters
            self.sample_count = orig.sample_count

    def enumerate_parameters(self):
        for i, (k, par) in enumerate(self.parameters.items()):
            yield i, k, par

    def init_random_state(self, random_state):
        self.random_state = random_state

    def add_parameter(self, parameter):
        self.parameters[parameter.name] = parameter

    def add_args(self, parser):
        parser.add_argument('--sample-count', type=int, default=None, help='Number of samples to be interpolated between models\n')

        # Additional axes
        for i, k, par in self.enumerate_parameters():
            par.add_args(parser)

    def init_from_args(self, config, args):
        self.sample_count = get_arg('sample_count', self.sample_count, args)

        # Register command-line arguments for auxiliary axes
        for i, k, par in self.enumerate_parameters():
            # Using aux mode because we need to generate the axis values from the
            # parameters passed to via args.
            par.init_from_args(args)

    def draw_random_param(self, par):
        # Always draw random parameters from self.random_state
        if par.dist == 'const':
            r = par.value
        elif par.dist == 'int':
            r = np.random.randint(par.min, par.max)
        else:
            dist = get_random_dist(par.dist, self.random_state)
            if dist is not None:
                # Rescale values between the limits and clip to min and max with
                # rejection sampling
                while True:
                    r = dist() if par.dist_args is None else dist(*par.dist_args)
                    r = par.min + r * (par.max - par.min)
                    if (par.min <= r) and (r <= par.max):
                        break
            else:
                r = None
            
        return r

    def draw_random_params(self, params=None):
        """
        Draw random values for each of the axes, those of the grid as well as
        auxiliary.
        """
        
        params = params or {}

        for i, k, par in self.enumerate_parameters():
            params[k] = self.draw_random_param(par)

        return params

    def sample_params(self, i):
        return self.draw_random_params(), None