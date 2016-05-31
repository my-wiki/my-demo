# -*- coding: utf-8 -*-

import os
import time
import tensorflow as tf


def keep_tracking(grads_and_vars, cnn, sess):
    # Keep track of gradient values and sparsity (optional)
    grad_summaries = []
    for g, v in grads_and_vars:
        if g is not None:
            grad_hist_summary = tf.histogram_summary(
                "{}/grad/hist".format(v.name), g)
            sparsity_summary = tf.scalar_summary(
                "{}/grad/sparsity".format(v.name), tf.nn.zero_fraction(g))
            grad_summaries.append(grad_hist_summary)
            grad_summaries.append(sparsity_summary)
    grad_summaries_merged = tf.merge_summary(grad_summaries)

    # Output directory for models and summaries
    timestamp = str(int(time.time()))
    out_dir = os.path.abspath(os.path.join(os.path.pardir, "runs", timestamp))
    print("Writing to {}\n".format(out_dir))

    # Summaries for loss and accuracy
    loss_summary = tf.scalar_summary("loss", cnn.loss)
    acc_summary = tf.scalar_summary("accuracy", cnn.accuracy)

    # Train Summaries
    train_summary_op = tf.merge_summary(
        [loss_summary, acc_summary, grad_summaries_merged])
    train_summary_dir = os.path.join(out_dir, "summaries", "train")
    train_summary_writer = tf.train.SummaryWriter(
        train_summary_dir, sess.graph_def)

    # Dev summaries
    dev_summary_op = tf.merge_summary([loss_summary, acc_summary])
    dev_summary_dir = os.path.join(out_dir, "summaries", "dev")
    dev_summary_writer = tf.train.SummaryWriter(
        dev_summary_dir, sess.graph_def)

    # Checkpoint directory. Tensorflow assumes this directory
    # already exists so we need to create it
    checkpoint_dir = os.path.abspath(os.path.join(out_dir, "checkpoints"))
    checkpoint_prefix = os.path.join(checkpoint_dir, "model")
    if not os.path.exists(checkpoint_dir):
        os.makedirs(checkpoint_dir)
    saver = tf.train.Saver(tf.all_variables())

    return train_summary_op, train_summary_writer, dev_summary_op, \
        dev_summary_dir, dev_summary_writer, checkpoint_prefix, saver
