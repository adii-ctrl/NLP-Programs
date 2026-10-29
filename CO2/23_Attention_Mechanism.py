import tensorflow as tf
from tensorflow.keras import layers, Model

class AttentionPooling(layers.Layer):
    def build(self, input_shape):
        self.score_layer = layers.Dense(1)
        super().build(input_shape)

    def call(self, inputs):
        scores = self.score_layer(inputs)
        weights = tf.nn.softmax(scores, axis=1)
        return tf.reduce_sum(weights * inputs, axis=1)

inputs = layers.Input(shape=(5, 8))
context = AttentionPooling()(inputs)
outputs = layers.Dense(2, activation="softmax")(context)
model = Model(inputs, outputs)
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy")

x = tf.random.normal((3, 5, 8))
print("Input shape:", x.shape)
print("Output shape:", model(x).shape)
