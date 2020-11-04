import numpy as np

from pfsspec.data.generativedatasetaugmenter import GenerativeDatasetAugmenter

class KuruczGenerativeAugmenter(GenerativeDatasetAugmenter):
    def __init__(self, orig=None):
        super(KuruczGenerativeAugmenter, self).__init__(orig=orig)

    @classmethod
    def from_dataset(cls, dataset, labels, coeffs, weight=None, batch_size=1, shuffle=True, chunk_size=None, seed=None):
        d = super(KuruczGenerativeAugmenter, cls).from_dataset(dataset, labels, coeffs, weight,
                                                               batch_size=batch_size,
                                                               shuffle=shuffle,
                                                               chunk_size=chunk_size,
                                                               seed=seed)
        return d

    def augment_batch(self, chunk_id, idx):
        labels, flux, weight = super(KuruczGenerativeAugmenter, self).augment_batch(chunk_id, idx)

        # Add minimal Gaussian noise on output
        # output *= np.random.normal(1, 0.01, output.shape)

        # TODO: what type of augmentation can we do here?
        # Cubic spline interpolation along grid lines?

        return labels, flux, weight