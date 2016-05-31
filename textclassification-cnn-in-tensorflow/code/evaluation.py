# -*- coding: utf-8 -*-

import numpy as np
import tensorflow as tf
import util.logger as ul
import model.batch_iter as mb
import model.split_data as ms
import preprocessing.load as pl
import model.define_parameters as md


log = ul.Logger.get_logger("Main")


def eval():
    log.info("Set Parameters...")
    FLAGS = md.set_para()
    log.info("Visualize Parameters...")
    md.visualize_para(FLAGS)

    log.info("Loading Data...")
    x_test, y_test, vocabulary, vocabulary_inv = pl.load_data()
    y_test = np.argmax(y_test, axis=1)
    log.info("Stat:: Vocabulary Size: {:d}" . format(len(vocabulary)))
    log.info("Stat:: Test set size {:d}".format(len(y_test)))

    log.info("Evaluating...")
    checkpoint_file = tf.train.latest_checkpoint(FLAGS.checkpoint_dir)
    graph = tf.Graph()

    with graph.as_default():
        session_conf = tf.ConfigProto(
          allow_soft_placement=FLAGS.allow_soft_placement,
          log_device_placement=FLAGS.log_device_placement)

        sess = tf.Session(config=session_conf)

        with sess.as_default():
            # Load the saved meta graph and restore variables
            saver = tf.train.import_meta_graph(
                "{}.meta".format(checkpoint_file))
            saver.restore(sess, checkpoint_file)

            # Get the placeholders from the graph by name
            input_x = graph.get_operation_by_name("input_x").outputs[0]
            # input_y = graph.get_operation_by_name("input_y").outputs[0]
            dropout_keep_prob = graph.get_operation_by_name(
                "dropout_keep_prob").outputs[0]

            # Tensors we want to evaluate
            predictions = graph.get_operation_by_name(
                "output/predictions").outputs[0]

            # Generate batches for one epoch
            batches = mb.batch_iter(
                x_test, FLAGS.batch_size, 1, shuffle=False)

            # Collect the predictions here
            all_predictions = []

            for x_test_batch in batches:
                batch_predictions = sess.run(
                    predictions,
                    {input_x: x_test_batch, dropout_keep_prob: 1.0})
                all_predictions = np.concatenate(
                    [all_predictions, batch_predictions])

        # Print accuracy
        correct_predictions = float(sum(all_predictions == y_test))
        log.info("Accuracy:{:g}".format(
            correct_predictions/float(len(y_test))))

if __name__ == '__main__':
    eval()
