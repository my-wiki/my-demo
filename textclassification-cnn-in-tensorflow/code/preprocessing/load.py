# -*- coding: utf-8 -*-
"""Load the dataset and clean it
"""
import re
import util.readwrite as urw
import numpy as np
import pad_sentence as ps
import build_vocab_and_data as bd


def clean_str(string):
    """Tokenization/string cleaning for all datasets except for SST.
    """
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    return string.strip().lower()


def load_data_and_labels():
    """Loads MR polarity data from files, splits the data into words and
        generates labels.
    Returns split sentences and labels.
    """
    # Load data from files
    positive_examples = urw.read_from_text("../data/rt-polarity.pos")
    positive_examples = [s.strip() for s in positive_examples]
    negative_examples = urw.read_from_text("../data/rt-polarity.neg")
    negative_examples = [s.strip() for s in negative_examples]
    # Split by words
    x_text = positive_examples + negative_examples
    x_text = [clean_str(sent) for sent in x_text]
    x_text = [s.split(" ") for s in x_text]
    # Generate labels
    positive_labels = [[0, 1] for _ in positive_examples]
    negative_labels = [[1, 0] for _ in negative_examples]
    y = np.concatenate([positive_labels, negative_labels], 0)
    return [x_text, y]


def load_data():
    """Loads and preprocessed data for the MR dataset.
    Returns input vectors, labels, vocabulary, and inverse vocabulary.
    """
    # Load and preprocess data
    sentences, labels = load_data_and_labels()
    sentences_padded = ps.pad_sentences(sentences)
    vocabulary, vocabulary_inv = bd.build_vocab(sentences_padded)
    x, y = bd.build_input_data(sentences_padded, labels, vocabulary)
    return [x, y, vocabulary, vocabulary_inv]
