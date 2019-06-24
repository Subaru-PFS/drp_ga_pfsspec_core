from pfsspec.io.datasetbuilder import DatasetBuilder

class SdssDatasetBuilder(DatasetBuilder):
    def __init__(self, orig=None):
        super(SdssDatasetBuilder, self).__init__(orig)
        if orig is not None:
            self.dataset = orig.dataset
        else:
            self.dataset = None

    def get_spectrum_count(self):
        return len(self.dataset.spectra)

    def get_wave_count(self):
        return self.pipeline.rebin.shape[0]

    def build(self):
        dataset = super(SdssDatasetBuilder, self).build()
        dataset.wave[:] = self.pipeline.rebin

        for i in range(0, len(self.dataset.spectra)):
            spec = self.dataset.spectra[i]
            spec = self.pipeline.run(spec)
            dataset.flux[i, :] = spec.flux

        return dataset