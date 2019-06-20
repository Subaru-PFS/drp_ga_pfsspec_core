import keras.models as km
import keras.layers as kl
import keras.regularizers as kr
import keras.backend as K
import tensorflow as tf
from keras.utils.multi_gpu_utils import multi_gpu_model


def create_simple_pyramid(input_shape, output_shape, level=4, units=1024, reg=5e-5, gpu='0'):
    x = inputs = kl.Input((input_shape,))

    while level > 0:
        x = kl.Dense(units, )(x)
        x = kl.BatchNormalization()(x)
        x = kl.Activation('relu')(x)
        level -= 1
        units //= 2

    x = kl.Dense(output_shape)(x)

    model = km.Model(inputs=inputs, outputs=x)
    if len(gpu.split(',')) > 1:  # multi gpu model
        model = multi_gpu_model(model, gpus=len(gpu.split(',')))

    return model









"""
    model = Sequential()
    act = 'relu'
    init = "normal"

    # noisy input
    model.add(GaussianNoise(0.01, input_shape=[nn_input.shape[1]]))
    # model.add(Dense(4096, activation='relu'))

    # orig input
    model.add(Dense(4096, input_dim=nn_input.shape[1], activation=act))
    # model.add(Dense(4096, input_dim=nn_input.shape[1], activation=act))
    # model.add(Dense(4096, input_dim=nn_input.shape[1], activation=act))
    # model.add(Dense(4096, input_dim=nn_input.shape[1], activation=act))

    # shallow, wide
    # model.add(Dense(2048, activation=act, kernel_initializer=init))
    # model.add(Dense(2048, activation=act, kernel_initializer=init))

    # deep, narrow
    # model.add(Dense(32, activation=act, kernel_initializer=init))
    # model.add(Dense(32, activation=act, kernel_initializer=init))
    # model.add(Dense(32, activation=act, kernel_initializer=init))
    # model.add(Dense(32, activation=act, kernel_initializer=init))
    # model.add(Dense(32, activation=act, kernel_initializer=init))
    # model.add(Dense(32, activation=act, kernel_initializer=init))
    # model.add(Dense(32, activation=act, kernel_initializer=init))
    # model.add(Dense(32, activation=act, kernel_initializer=init))

    # pyramid
    # model.add(Dense(4096, activation=act, kernel_initializer=init))
    # model.add(Dense(2048, activation=act, kernel_initializer=init))
    # model.add(Dense(1024, activation=act, kernel_initializer=init))
    # model.add(Dense(512, activation=act, kernel_initializer=init))
    # model.add(Dense(256, activation=act, kernel_initializer=init))
    # model.add(Dense(128, activation=act, kernel_initializer=init))
    # model.add(Dense(64, activation=act, kernel_initializer=init))
    # model.add(Dense(32, activation=act, kernel_initializer=init))

    model.add(Dense(nn_output.shape[1], activation='linear', kernel_initializer=init))
    model.compile(loss='mse', optimizer='adamax')
"""