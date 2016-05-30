# -*- coding: utf-8 -*-
"""Main Entry
    Play CNN with MNIST Dataset in the Tensorflow.
"""

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import util.download_data as da
import util.form_data as fd
import util.extract_label as el
import util.logger as logger
import util.error_rate as ue
import settings.parameters as p
import model.CNN as mc
import model.define_parameters as md

log = logger.Logger.get_logger('Main')


def debug():
    log.info("Download Dataset...")
    train_data_filename = da.maybe_download('train-images-idx3-ubyte.gz')
    train_labels_filename = da.maybe_download('train-labels-idx1-ubyte.gz')
    test_data_filename = da.maybe_download('t10k-images-idx3-ubyte.gz')
    test_labels_filename = da.maybe_download('t10k-labels-idx1-ubyte.gz')

    log.info("Extract and Split Data from Dataset...")
    train_data = fd.extract_data(train_data_filename, 60000)
    test_data = fd.extract_data(test_data_filename, 10000)

    log.info("Extract Labels from Data...")
    train_labels = el.extract_labels(train_labels_filename, 60000)
    test_labels = el.extract_labels(test_labels_filename, 10000)

    validation_data = train_data[:p.VALIDATION_SIZE, :, :, :]
    validation_labels = train_labels[:p.VALIDATION_SIZE]
    train_data = train_data[p.VALIDATION_SIZE:, :, :, :]
    train_labels = train_labels[p.VALIDATION_SIZE:]
    train_size = train_labels.shape[0]

    log.info("Define the Model...")
    train_data_node, train_labels_node, validation_data_node, \
        test_data_node = md.split_data(validation_data, test_data)

    conv1_weights, conv1_biases, conv2_weights, conv2_biases, \
        fc1_weights, fc1_biases, fc2_weights, fc2_biases \
        = md.define_layers_parameters()

    log.info("Training computation: logits + cross-entropy loss...")
    logits = mc.model(train_data_node, conv1_weights, conv1_biases,
                      conv2_weights, conv2_biases, fc1_weights, fc1_biases,
                      fc2_weights, fc2_biases, train=True)

    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
        logits, train_labels_node))

    log.info("L2 regularization for the fully connected parameters...")
    regularizers = (tf.nn.l2_loss(fc1_weights) + tf.nn.l2_loss(fc1_biases) +
                    tf.nn.l2_loss(fc2_weights) + tf.nn.l2_loss(fc2_biases))

    log.info("Add the regularization term to the loss...")
    loss += 5e-4 * regularizers

    # Optimizer: set up a variable that's incremented once per batch and
    # controls the learning rate decay.
    learning_rate, optimizer = \
        md.define_learning_rate_optimizer(train_size, loss)

    log.info("Predictions for the minibatch, validation set and test set...")
    train_prediction = tf.nn.softmax(logits)
    validation_prediction = tf.nn.softmax(mc.model(validation_data_node,
                                                   conv1_weights, conv1_biases,
                                                   conv2_weights, conv2_biases,
                                                   fc1_weights, fc1_biases,
                                                   fc2_weights, fc2_biases))
    test_prediction = tf.nn.softmax(mc.model(test_data_node,
                                             conv1_weights, conv1_biases,
                                             conv2_weights, conv2_biases,
                                             fc1_weights, fc1_biases,
                                             fc2_weights, fc2_biases))

    log.info("Training and visualizing results...")
    s = tf.InteractiveSession()
    s.as_default()
    tf.initialize_all_variables().run()

    steps = int(train_size / p.BATCH_SIZE)
    for step in xrange(steps):
        # Compute the offset of the current minibatch in the data.
        # Note that we could use better randomization across epochs.
        offset = (step * p.BATCH_SIZE) % (train_size - p.BATCH_SIZE)
        batch_data = train_data[offset:(offset + p.BATCH_SIZE), :, :, :]
        batch_labels = train_labels[offset:(offset + p.BATCH_SIZE)]
        # This dictionary maps the batch data (as a numpy array) to the
        # node in the graph it should be fed to.
        feed_dict = {train_data_node: batch_data,
                     train_labels_node: batch_labels}
        # Run the graph and fetch some of the nodes.
        _, l, lr, predictions = s.run(
            [optimizer, loss, learning_rate, train_prediction],
            feed_dict=feed_dict)

        # Print out the loss periodically.
        if step % 100 == 0:
            error, _ = ue.error_rate(predictions, batch_labels)
            log.info('Step %d of %d' % (step, steps))
            log.info('Minibatch loss: %.5f Error: %.5f Learning rate: %.5f' % (
                l, error, lr))
            log.info('Validation error: %.1f%%' % ue.error_rate(
                validation_prediction.eval(), validation_labels)[0])

    test_error, confusions = ue.error_rate(test_prediction.eval(), test_labels)
    plt.xlabel('Actual')
    plt.ylabel('Predicted')
    plt.grid(False)
    plt.xticks(np.arange(p.NUM_LABELS))
    plt.yticks(np.arange(p.NUM_LABELS))
    plt.imshow(confusions, cmap=plt.cm.jet, interpolation='nearest')

    for i, cas in enumerate(confusions):
        for j, count in enumerate(cas):
            if count > 0:
                xoff = .07 * len(str(count))
                plt.text(j-xoff, i+.2, int(count), fontsize=9, color='white')
    plt.savefig("figure/confusion_matrix.pdf")

if __name__ == '__main__':
    debug()
