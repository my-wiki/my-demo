# -*- coding: utf-8 -*-
"""Main entry for the text classification by tensorflow.
"""
import model.cnn as mc
import tensorflow as tf
import model.split_data as ms
import preprocessing.load as pl
import util.logger as ul
import model.define_parameters as md
import model.tracking as mt
import model.batch_iter as mb

log = ul.Logger.get_logger("Main")


def main():
    log.info("Set Parameters...")
    FLAGS = md.set_para()
    log.info("Visualize Parameters...")
    md.visualize_para(FLAGS)

    log.info("Loading Data...")
    x, y, vocabulary, vocabulary_inv = pl.load_data()
    x_train, x_dev, y_train, y_dev = ms.split_data(x, y)

    log.info("Stat:: Vocabulary Size: {:d}" . format(len(vocabulary)))
    log.info("Stat:: Train/Dev split: {:d}/{:d}".format(
        len(y_train), len(y_dev)))

    log.info("Start Training...")
    with tf.Graph().as_default():
        session_conf = tf.ConfigProto(
            allow_soft_placement=FLAGS.allow_soft_placement,
            log_device_placement=FLAGS.log_device_placement)
        sess = tf.Session(config=session_conf)
        with sess.as_default():
            cnn = mc.TextCNN(
                sequence_length=x_train.shape[1],
                num_classes=2,
                vocab_size=len(vocabulary),
                embedding_size=FLAGS.embedding_dim,
                filter_sizes=list(map(int, FLAGS.filter_sizes.split(","))),
                num_filters=FLAGS.num_filters,
                l2_reg_lambda=FLAGS.l2_reg_lambda)

        # Define Training procedure
        global_step = tf.Variable(0, name="global_step", trainable=False)
        optimizer = tf.train.AdamOptimizer(1e-3)
        grads_and_vars = optimizer.compute_gradients(cnn.loss)
        train_op = optimizer.apply_gradients(
            grads_and_vars,
            global_step=global_step)

        # Keep track of gradient values and sparsity (optional)
        train_summary_op, train_summary_writer, \
            dev_summary_op, dev_summary_dir, \
            dev_summary_writer, checkpoint_prefix, \
            saver = mt.keep_tracking(grads_and_vars, cnn, sess)

        # Initialize all variables
        sess.run(tf.initialize_all_variables())

        def train_step(x_batch, y_batch):
            """A single training step
            """
            feed_dict = {
              cnn.input_x: x_batch,
              cnn.input_y: y_batch,
              cnn.dropout_keep_prob: FLAGS.dropout_keep_prob
            }
            _, step, summaries, loss, accuracy = sess.run(
                [train_op, global_step,
                    train_summary_op,
                    cnn.loss, cnn.accuracy],
                feed_dict)
            log.info("step {}, loss {:g}, acc {:g}".format(
                step, loss, accuracy))

            train_summary_writer.add_summary(summaries, step)

        def dev_step(x_batch, y_batch, writer=None):
            """
            Evaluates model on a dev set
            """
            feed_dict = {
              cnn.input_x: x_batch,
              cnn.input_y: y_batch,
              cnn.dropout_keep_prob: 1.0
            }
            step, summaries, loss, accuracy = sess.run(
                [global_step, dev_summary_op,
                    cnn.loss, cnn.accuracy],
                feed_dict)

            log.info("step {}, loss {:g}, acc {:g}".format(
                step, loss, accuracy))
            if writer:
                writer.add_summary(summaries, step)

        # Generate batches
        batches = mb.batch_iter(
            list(zip(x_train, y_train)), FLAGS.batch_size, FLAGS.num_epochs)
        # Training loop. For each batch...
        for batch in batches:
            x_batch, y_batch = zip(*batch)
            train_step(x_batch, y_batch)
            current_step = tf.train.global_step(sess, global_step)
            if current_step % FLAGS.evaluate_every == 0:
                log.info("Evaluation: ".format(
                    dev_step(x_dev, y_dev, writer=dev_summary_writer)))
            if current_step % FLAGS.checkpoint_every == 0:
                path = saver.save(sess,
                                  checkpoint_prefix,
                                  global_step=current_step)
                log.info("Saved model checkpoint to {}".format(path))


if __name__ == '__main__':
    main()
