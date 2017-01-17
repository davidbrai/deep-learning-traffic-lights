import numpy as np
import caffe
import random

def doAugmentation(img):
    return np.rot90(img, random.randrange(4))

class RotationLayer(caffe.Layer):
    def setup(self, bottom, top):
        assert len(bottom) == 1, 'requires a single layer.bottom'
        assert bottom[0].data.ndim >= 3, 'requires image data'
        assert len(top) == 1, 'requires a single layer.top'

    def reshape(self, bottom, top):
        # Copy shape from bottom
        top[0].reshape(*bottom[0].data.shape)

    def forward(self, bottom, top):
        # Copy all of the data
        top[0].data[...] = bottom[0].data[...]

        for ii in xrange(0, top[0].data.shape[0]):
            imin = top[0].data[ii, :, :, :].transpose(1, 2, 0)
            top[0].data[ii, :, :, :] = doAugmentation(imin).transpose(2, 0, 1)

    def backward(self, top, propagate_down, bottom):
        pass