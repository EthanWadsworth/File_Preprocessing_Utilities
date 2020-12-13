import matplotlib.pyplot as plt
import numpy as np
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


def gen_word_maps(text):
    """ Generates word distribution and individual word hashmaps

    Parameters
    ----------
    text: string
        string to split into words to get word distribution and individual 
        word maps

    Returns
    -------
    wordDistribution: dictionary (string: int)
        hashmap of each word and their frequency 
    wordDistributions: dictionary (string: dict(string: int))
        hashmap of hashmaps that contains the number of times each next word 
        occurs after each word in the hashmap
    """

    # if the text is an empty string, return None for both maps 
    if is_empty_text(text):
        return None, None

    # dictonary to hold frequency of each word
    word_map = {}  
    # dictionary to hold dictionaries of next word frequencies for each word
    word_distribution = {}  

    # preprocessing text to remove punctuation and newline characters
    # creates empty map table and uses third argument for removal chars
    text = text.translate(text.maketrans("", "", string.punctuation))
    text = text.replace('\n', ' ')

    words = text.split(' ')  # text split into words
    curr_word_index = 0      # counter to check if there is a next word

    # create word maps and frequencies
    for word in words:
        word_distribution = update_distribution(word_distribution, 
                                                word.lower())
        # only run if their is a next word remaining
        if (curr_word_index + 1 < len(words)):
            word_map = update_word_mapping(word_map, word.lower(), 
                                            words[curr_word_index + 1].lower())
        curr_word_index += 1

    return word_distribution, word_map


def read_file(filename):
    """ Reads from file and returns text from file converted into a string

    Parameters
    ----------
    filename: string
        path to file to read from

    Returns
    -------
    text: string
        text from entered file as a string
    """

    # read in text from file if it exists and return it as a string
    try:
        f = open(filename, 'r')
        text = f.read()
        f.close()
        return text
    except FileNotFoundError as err:
        print(err)
        exit()


def gen_maps_from_file(filename):
    """ generates word distribution and individual word hashmaps from an 
    entered file

    Parameters
    ----------
    filename: string
        file to generate hashmaps from
    
    Returns
    -------
    From gen_word_maps():
    wordDistribution: dictionary (string: int)
        hashmap of each word and their frequency 
    wordDistributions: dictionary (string: dict(string: int))
        hashmap of hashmaps that contains the number of times each next word 
        occurs after each word in the hashmap
    """

    # read in text from file specified and generate and return the word maps
    text = read_file(filename)
    return gen_word_maps(text)


def update_distribution(word_distribution, word):
    """ Updates the word frequency distribution hashmap using the specified 
    word entered

    Parameters
    ----------
    wordDistribution: dictionary (string: int)
        current hashmap of word frequencies
    word: string
        word to add to the word distribution dictionary
    
    Returns
    -------
    wordDistribution: dictionary (string: int)
        updated wordDistribution with the specified word added in
    """

    # Increment word frequency for word if it exists or add it if it doesn't 
    if word in word_distribution:
        word_distribution[word] = word_distribution[word] + 1
    else:
        word_distribution[word] = 1

    return word_distribution


def update_word_mapping(word_map, word, next_word):
    """ Updates next words frequency map for the specified word

    Parameters
    ----------
    word_map: dictionary (string : dictionary (string : int))
        tracks number of times certain words come after current word
    word: string
        the current word in which the next_word will be mapped into
    next_word: string
        word to add to the specified word's frequency distribution

    Returns
    -------
    word_map: dictionary (string : dictionary (string : int))
        updated next word map with the next_word added for the specified word 
    """

    # check if current word is in the word map, or add it if it does not
    if word in word_map:
        # check if the next word is in the mapping for the current word
        # if it is, increment for the next word, or add it
        if next_word in word_map[word].keys():
            word_map[word][next_word] = word_map[word][next_word] + 1
        else:
            word_map[word][next_word] = 1
    else:
        word_map[word] = {next_word: 1}

    return word_map


def replace_word(filename, output_name, word_to_replace, new_word):
    """ Looks for all instances of word_to_replace in specified file and 
    replaces it with new word.
    Writes modified text to specified output file

    Parameters
    ----------
    filename: string
        path to input file to modify
    output_name: string
        path of file to write output to
    word_to_replace: string
        string that will replace all found instances of the word to replace

    Returns
    -------
    None
    """

    # read text from file and then replace all instances of old word with the
    # specified new word
    text = read_file(filename)
    mod_text = text.replace(word_to_replace, new_word)

    # write text to file with specified name
    with open(output_name, 'w') as f:
        f.write(mod_text)
    f.close()


def remove_stopwords(text):
    """ Removes all found stopwords from the input text

    Parameters
    ----------
    text: string
        string to remove stopwords from

    Returns
    -------
    modified_text: string
        text with all stopwords removed
    """

    words = text.split(' ')

    # grab all english stopwords and put it into a set
    stop_words = set(stopwords.words('english')) 

    modified_text = words[0]

    # Append only words not in stopwords set
    for i in range(1, len(words)):
        if not words[i] in stop_words:
            modified_text += ' ' + words[i]

    return modified_text


def remove_stopwords_from_file(filename, outfile):
    """ Removes all stopwords from input file and writes it to output file

    Parameters
    ----------
    filename: string
        path to input file
    outfile: string
        path to output file to write modified text to

    Returns
    -------
    None
    """

    # read text from file and them remove all stopwords from it
    text = read_file(filename)
    text = remove_stopwords(text)

    # write modified text to specified file
    with open(outfile, 'w') as f:
        f.write(text)
    f.close()


def stem_words(text):
    """ Applies stemming to group of text passed in

    Parameters
    ----------
    text: string
        string to modify

    Returns
    -------
    stemmed_text: string
        string after applying word stemming
    """

    # initialize stemmer object and setup words
    ps = PorterStemmer()
    words = text.split(' ')
    stemmed_text = words[0]

    # append stemmed words to output string
    for i in range(1, len(words)):
        stemmed_text += ' ' + ps.stem(words[i])

    return stemmed_text


def stem_file(filename, outfile):
    """ Stems input from file and writes it to specified outfile

    Parameters
    ----------
    filename: string
        path to input file
    outfile: string
        path to output file to write stemmed text to

    Returns
    -------
    None
    """

    # read text in from file and stem each word in the text
    text = read_file(filename)
    text = stem_words(text)

    # write text to specified output file
    with open(outfile, 'w') as f:
        f.write(text)
    f.close()


def preprocess_file(filename, outfile):
    """ Applies stopword removal and stemming to input file and writes 
    modified text to output file

    Parameters
    ----------
    filename: string
        path to input file
    outfile: string
        path to output file to write modified text to

    Returns
    -------
    None
    """

    # read text from file and remove stopwords and stem words in it
    text = read_file(filename)
    text = remove_stopwords(text)
    text = stem_words(text)

    # write preprocessed text to specified output file
    with open(outfile, 'w') as f:
        f.write(text)
    f.close()


def show_word_frequencies(filename):
    """ Creates bar chart with top 100 word frequencies from input file

    Parameters:
    filename: string
        path to input file
    
    Returns
    None (shows bar chart figure of word frequencies)
    """

    # get word map and word distribution for file
    word_distribution, word_map = gen_maps_from_file(filename)

    # check if any of the word maps are empty
    if not word_distribution or not word_map:
        print('Could not generate frequency chart for empty file: ' + filename)
        exit()

    # sort by dictionary value using get as a callback function
    keys_sorted = sorted(word_distribution, key=word_distribution.get)

    # add keys in sorted order to the sorted dictionary
    sorted_dict = {} 
    for key in keys_sorted:
        sorted_dict[key] = word_distribution[key]

    # convert dictionary objects into lists for array slicing
    top_hundred_words = list(sorted_dict.keys())
    top_hundred_values = list(sorted_dict.values())

    # only take the top 100 words if there are more than 100
    if len(top_hundred_words) > 100:
        # getting the last 100 indices 
        start_slice = len(top_hundred_words) - 101
        end_slice = len(top_hundred_words) - 1
        top_hundred_words = top_hundred_words[start_slice:end_slice]
        top_hundred_values = top_hundred_values[start_slice:end_slice]

    # create the bar chart for the word frequencies 
    draw_distribution(top_hundred_words, top_hundred_values, 
                        'Words', 'Frequency', 'Word Frequency Distribution')


def show_next_word_distribution(filename, word):
    """ Creates bar chart with frequencies of words that come after entered 
    word

    Parameters:
    filename: string
        path to input file
    word: string
        string used to create next word frequencies map
    
    Returns
    None (shows bar chart figure of word frequencies)
    """

    # get word map and distribution for file
    word_distribution, word_map = gen_maps_from_file(filename)

    # check if any of the word maps are empty
    if not word_distribution or not word_map:
        print('Could not generate frequency chart for empty file: ' + filename)
        exit()
    
    # dictionary containing the next word frequencies for chosen word
    next_word_frequencies = {}

    # see if the chosen word exists in the word map dictionary
    # exit the function if a KeyError is thrown
    try:
        next_word_frequencies = word_map[word]
    except KeyError:
        print(word + ' does not exist in the file: ' + filename)
        exit()

    # preprocess word
    word = word.lower()

    # sort word dictionary by dictionary value using get as a callback function
    keys_sorted = sorted(next_word_frequencies, key=next_word_frequencies.get)

    # add keys in sorted order to the sorted dictionary
    sorted_dict = {} 
    for key in keys_sorted:
        sorted_dict[key] = next_word_frequencies[key]

    # convert dictionary objects into lists for array slicing
    top_hundred_words = list(sorted_dict.keys())
    top_hundred_values = list(sorted_dict.values())

    # only take the top 100 words if there are more than 100
    if len(top_hundred_words) > 100:
        # getting the last 100 indices 
        start_slice = len(top_hundred_words) - 101
        end_slice = len(top_hundred_words) - 1
        top_hundred_words = top_hundred_words[start_slice:end_slice]
        top_hundred_values = top_hundred_values[start_slice:end_slice]

    # create the bar chart for the word frequencies 
    draw_distribution(top_hundred_words, top_hundred_values, 'Next Words', 
                        'Frequency', 'Next Word Frequency Distribution for: ' + 
                        word)


def show_preprocessed_distribution(filename):
    """ Creates bar chart with top 100 word frequencies from input file after 
    performing stopword removal and stemming

    Parameters:
    filename: string
        path to input file
    
    Returns
    None (shows bar chart figure of word frequencies after preprocessing)
    """

    # get text from file
    text = read_file(filename)

    # do not generate a frequency chart for any empty file
    if is_empty_text(text):
        print('Could not generate frequency chart for empty file: ' + filename)
        exit()

    # preprocess text from file before getting word map and frequency
    text = remove_stopwords(text)
    text = stem_words(text)
    word_distribution, word_map = gen_word_maps(text)

    # sort by dictionary value using get as a callback function
    keys_sorted = sorted(word_distribution, key=word_distribution.get)

    # add keys in sorted order to the sorted dictionary
    sorted_dict = {} 
    for key in keys_sorted:
        sorted_dict[key] = word_distribution[key]

    # convert dictionary objects into lists for array slicing
    top_hundred_words = list(sorted_dict.keys())
    top_hundred_values = list(sorted_dict.values())

    # only take the top 100 words if there are more than 100
    if len(top_hundred_words) > 100:
        # getting the last 100 indices 
        start_slice = len(top_hundred_words) - 101
        end_slice = len(top_hundred_words) - 1
        top_hundred_words = top_hundred_words[start_slice:end_slice]
        top_hundred_values = top_hundred_values[start_slice:end_slice]

    # create the bar chart for the word frequencies 
    draw_distribution(top_hundred_words, top_hundred_values, 'Words', 
                    'Frequency', 'Word Frequency Distribution (Preprocessed)')


def draw_distribution(keys, values, x_axis, y_axis, title):
    """ Creates bar chart diagram for word frequencies

    Parameters
    ----------
    keys: list of strings
        list of words 
    values: lsit of ints
        list of integers that specify the frequency for each word in keys

    Returns
    -------
    None (draws bar chart figure)
    """

    # specifications for bar chart figure
    y_position = np.arange(len(keys))
    plt.bar(y_position, values, align='center', alpha=0.5)
    plt.xticks(y_position, keys, rotation=90)
    plt.ylabel(y_axis)
    plt.xlabel(x_axis)
    plt.title(title)
    plt.tick_params(axis='x', which='major', labelsize=7)
    plt.tight_layout()
    plt.show()


def get_word_count(filename):
    """ Gets number of words contained in input file

    Parameters
    ----------
    filename: string
        path to input file

    Returns
    -------
    word_count: int
        number of words contained in input file
    """

    # read text from file and remove punctuation and newline characters
    text = read_file(filename)

    # check if text from file is consider empty, then count is 0
    if (is_empty_text(text)):
        return 0

    text = text.translate(text.maketrans("", "", string.punctuation))
    text = text.replace('\n', ' ')

    # get number of words in text string
    words = text.split(' ')
    word_count = len(words)

    return word_count


def gen_sentence(filename, sentence_length=10):
    """ Generates sentence using word frequency and word map hashmaps with 
    sentence length

    Parameters
    ----------
    filename: string
        path to input file
    sentence_length: int, default : 10
        number of words to put in the generated sentence

    Returns
    -------
    sentence: string
        generated sentence using word maps
    """

    word_distribution, word_map = gen_maps_from_file(filename)

    # check if any of the word maps are empty, exit with message
    if not word_distribution or not word_map:
        print('cannot generate sentence from empty file: ' + filename)
        exit()

    # get most common word from word frequencies and use tha as the first word
    # in the generated sentence
    last_index = len(word_distribution) - 1
    most_common_word = sorted(word_distribution, key=word_distribution.get)
    most_common_word = most_common_word[last_index]

    # using the next word frequencies for words in the word map, get the most
    # common next word for each word and append it to the sentence while the
    # length has not been met 
    sentence = most_common_word
    word_count = 1
    while word_count < sentence_length:
        last_index = len(word_map[most_common_word]) - 1

        # sort the next words dictionary for the current most common word
        most_common_word = sorted(word_map[most_common_word], 
                                    key = word_map[most_common_word].get)

        # add new most common word to the sentence                     
        most_common_word = most_common_word[last_index]
        sentence += ' ' + most_common_word
        word_count += 1

    sentence += '.'
    return sentence


def is_empty_text(text):
    """ Checks for empty text data read from file

    Parameters
    ----------
    text: string
        Block of text to perform empty checks on

    Returns
    -------
    True if considerd empty, False if text is not empty
    """

    # removes all newline characters are strips leading and ending whitespace
    text = text.replace('\n', '').strip()

    # return True if empty, else return false
    if text == '':
        return True

    return False