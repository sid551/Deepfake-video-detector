# model/mesonet.py
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Conv2D, BatchNormalization, Activation, MaxPooling2D, Flatten, Dense

class Meso4:
    def __init__(self):
        self.model = self.init_model()

    def init_model(self):
        x = Input(shape=(256, 256, 3))
        
        # Layer 1
        y = Conv2D(8, (3, 3), padding='same')(x)
        y = BatchNormalization()(y)
        y = Activation('relu')(y)
        y = MaxPooling2D(pool_size=(2, 2))(y)

        # Layer 2
        y = Conv2D(8, (5, 5), padding='same')(y)
        y = BatchNormalization()(y)
        y = Activation('relu')(y)
        y = MaxPooling2D(pool_size=(2, 2))(y)

        # Layer 3
        y = Conv2D(16, (5, 5), padding='same')(y)
        y = BatchNormalization()(y)
        y = Activation('relu')(y)
        y = MaxPooling2D(pool_size=(2, 2))(y)

        # Layer 4
        y = Conv2D(16, (5, 5), padding='same')(y)
        y = BatchNormalization()(y)
        y = Activation('relu')(y)
        y = MaxPooling2D(pool_size=(4, 4))(y)

        # Output
        y = Flatten()(y)
        y = Dense(16)(y)
        y = Activation('relu')(y)
        y = Dense(1, activation='sigmoid')(y)

        return Model(inputs=x, outputs=y)

    def load(self, path):
        self.model.load_weights(path)

    def predict(self, x):
        return self.model.predict(x)
