import numpy as np

from pfsspec.stellarmod.modelgrid import ModelGrid
from pfsspec.stellarmod.kuruczspectrum import KuruczSpectrum

class KuruczGrid(ModelGrid):
    def __init__(self, model):
        super(KuruczGrid, self).__init__()

        if model == 'kurucz':
            self.M_H = np.array([-5.0, -4.5, -3.5, -3.0, -2.5, -2.0, -1.5, -1.0, -0.5, -0.3, -0.2, -0.1,
                                 0.0, 0.1, 0.2, 0.3,
                                 # 0.4,
                                 0.5, 1.0])
            self.T_eff = np.array([3500., 3750., 4000., 4250., 4500., 4750., 5000., 5250., 5500.,
                                   5750., 6000., 6250., 6500., 6750., 7000., 7250., 7500., 7750.,
                                   8000., 8250., 8500., 8750., 9000., 9250., 9500., 9750., 10000.,
                                   10500., 11000., 11500., 12000., 12500., 13000., 14000., 15000.,
                                   16000., 17000., 18000., 19000., 20000., 21000., 22000., 23000.,
                                   24000., 25000., 26000., 27000., 28000., 29000., 30000., 31000.,
                                   32000., 33000., 34000., 35000., 37500., 40000., 42500., 45000.,
                                   47500., 50000.])
            self.log_g = np.arange(0, 5.1, 0.5)
        else:
            raise Exception('Invalid model type.')

        # Default grid points
        #self.M_H = np.array([-5.0, -4.5, -3.5, -3.0, -2.5, -2.0, -1.5, -1.0, -0.5, -0.3, -0.2, -0.1,
        #            0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 1.0])
        #self.T_eff = np.hstack([np.arange(3500, 13000, 250), np.arange(13000, 50001, 1000)])
        #self.log_g = np.arange(0, 5.1, 0.5)

