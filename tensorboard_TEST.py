import tensorflow as tf

a = tf.constant(3.0, name='a')
b = tf.constant(5.0, name='b')
c = a * b

with tf.Session() as sess:
    writer = tf.summary.FileWriter("./log/", sess.graph)
    sess.run(c)
    writer.close()

