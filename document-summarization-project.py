import nltk
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx

def read_article(file_name):
    """
    Reads the content of a text file and returns it as a string.
    """
    with open(file_name, "r") as file:
        data = file.readlines()
    article = ''.join(data)
    return article

def sentence_similarity(sent1, sent2, stopwords=None):
    """
    Calculates the cosine similarity between two sentences.
    """
    if stopwords is None:
        stopwords = []
 
    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]
 
    all_words = list(set(sent1 + sent2))
 
    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)
 
    # build the vector for the first sentence
    for w in sent1:
        if w in stopwords:
            continue
        vector1[all_words.index(w)] += 1
 
    # build the vector for the second sentence
    for w in sent2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] += 1
 
    return 1 - cosine_distance(vector1, vector2)

def build_similarity_matrix(sentences, stop_words):
    """
    Creates a similarity matrix for the given sentences.
    """
    # Create an empty similarity matrix
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
 
    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 != idx2:
                similarity_matrix[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2], stop_words)
 
    return similarity_matrix

def generate_summary(file_name, top_n=5):
    """
    Generates a summary of the given text file.
    """
    stop_words = stopwords.words('english')
    summarize_text = []

    # Step 1 - Read text anc split it into sentences
    article = read_article(file_name)
    sentences = nltk.sent_tokenize(article)

    # Step 2 - Generate Similarity Matrix across sentences
    sentence_similarity_martix = build_similarity_matrix(sentences, stop_words)

    # Step 3 - Rank sentences in similarity matrix
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)
    scores = nx.pagerank(sentence_similarity_graph)

    # Step 4 - Sort the rank and pick top sentences
    ranked_sentences = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)

    # Step 5 - Retrieve top sentences based on top_n
    for i in range(top_n):
        summarize_text.append(ranked_sentences[i][1])

    # Step 6 - Output the summarize text
    return ' '.join(summarize_text)
