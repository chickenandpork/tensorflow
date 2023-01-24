#import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

# tf.logging.set_verbosity(tf.logging.ERROR)


celsius_q    = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit_a = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

for i, c in enumerate(celsius_q):
  print("{} C == {} F".format(c, fahrenheit_a[i]))

L0 = tf.keras.layers.Dense(units=1, input_shape=[1])
L1 = tf.keras.layers.Dense(units=4, input_shape=[1])
L2 = tf.keras.layers.Dense(units=4, input_shape=[1])
model = tf.keras.Sequential([L0])
model.compile(loss = 'mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.1))
history = model.fit(celsius_q,fahrenheit_a,epochs=500,verbose=False)
print("Completed model, layer variables: {}".format(L0.get_weights()))


#plt.xlabel("Epoch Number")
#plt.ylabel("Loss Magnitude")
#plt.plot(history.history["loss"])

print(model.predict([100.00]))
