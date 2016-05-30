# -*- coding: utf-8 -*-

"""A function to define the training parameters
"""

import tensorflow as tf
import settings.parameters as p


def split_data(validation_data, test_data):
    # This is where training samples and labels are fed to the graph.
    # These placeholder nodes will be fed a batch of training data at each
    # training step, which we'll write once we define the graph structure.
    train_data_node = tf.placeholder(
        tf.float32,
        shape=(p.BATCH_SIZE, p.IMAGE_SIZE, p.IMAGE_SIZE, p.NUM_CHANNELS))

    train_labels_node = tf.placeholder(
        tf.float32,
        shape=(p.BATCH_SIZE, p.NUM_LABELS))

    # For the validation and test data, we'll just hold the entire dataset in
    # one constant node.
    validation_data_node = tf.constant(validation_data)
    test_data_node = tf.constant(test_data)
    return train_data_node, train_labels_node, \
        validation_data_node, test_data_node


def define_layers_parameters():
    # The variables below hold all the trainable weights. For each, the
    # parameter defines how the variables will be initialized.
    conv1_weights = tf.Variable(
        tf.truncated_normal([5, 5, p.NUM_CHANNELS, 32],  # 5x5 filter, depth 32
                            stddev=0.1,
                            seed=p.SEED))

    conv1_biases = tf.Variable(tf.zeros([32]))
    conv2_weights = tf.Variable(
        tf.truncated_normal([5, 5, 32, 64],
                            stddev=0.1,
                            seed=p.SEED))
    conv2_biases = tf.Variable(tf.constant(0.1, shape=[64]))
    fc1_weights = tf.Variable(  # fully connected, depth 512.
        tf.truncated_normal([p.IMAGE_SIZE / 4 * p.IMAGE_SIZE / 4 * 64, 512],
                            stddev=0.1,
                            seed=p.SEED))
    fc1_biases = tf.Variable(tf.constant(0.1, shape=[512]))
    fc2_weights = tf.Variable(
        tf.truncated_normal([512, p.NUM_LABELS],
                            stddev=0.1,
                            seed=p.SEED))
    fc2_biases = tf.Variable(tf.constant(0.1, shape=[p.NUM_LABELS]))
    return conv1_weights, conv1_biases, conv2_weights, conv2_biases, \
        fc1_weights, fc1_biases, fc2_weights, fc2_biases


def define_learning_rate_optimizer(train_size, loss):
    batch = tf.Variable(0)
    # Decay once per epoch, using an exponential schedule starting at 0.01.
    learning_rate = tf.train.exponential_decay(
        0.01,                # Base learning rate.
        batch * p.BATCH_SIZE,  # Current index into the dataset.
        train_size,          # Decay step.
        0.95,                # Decay rate.
        staircase=True)
    optimizer = tf.train.MomentumOptimizer(learning_rate,
                                           0.9).minimize(loss,
                                                         global_step=batch)
    return learning_rate, optimizer
