import text_utilities

# Note: To run from modules/ use test file name as test.txt
#       To run from base project directory, use modules/test.txt
test_file = 'modules/test.txt'


def test_gen_word_maps():
    """
    Unit test function for gen_word_maps
    """

    # Input string to test function on
    test_str = ("Hello my name is my name is Patrick.")

    # get word maps and word frequencies
    wordDistribution, wordMap = text_utilities.gen_word_maps(test_str)

    # check that expected word frequencies are correct
    assert wordDistribution['my'] == 2
    assert wordDistribution['hello'] == 1
    assert wordMap['my']['name'] == 2


def test_gen_maps_from_file():
    """
    Unit test function for gen_maps_from_file
    """

    # get word maps and word frequencies from test.txt file
    wordDistribution, wordMap = text_utilities.gen_maps_from_file(test_file)

    # check that next word and word frequencies match expected values
    assert wordDistribution['hello'] == 6
    assert wordMap['my']['name'] == 4
    assert {'my': 1} == wordMap['you']
    assert {'is': 3, 'my': 1} == wordMap['name']


def test_update_distribution():
    """
    Unit test function for update_distribution
    """

    # starting word frequencies to update
    sample_distribution = {
        'hi': 1, 
        'bye': 3, 
        'name': 2, 
        'computer': 5, 
        'green': 1
        }
    
    # add blue to the sample_distribution
    sample_distribution = text_utilities.update_distribution(
                                                sample_distribution, 'blue')

    # check that the updated distribution added blue correctly                            
    assert sample_distribution == {'hi': 1, 'bye': 3, 'name': 2, 'computer': 5, 
                                    'green': 1, 'blue': 1}

    # pass in word that already exists and check if value is updated 
    sample_distribution = text_utilities.update_distribution(
                                                    sample_distribution, 'hi')
    assert sample_distribution['hi'] == 2
    assert sample_distribution['blue'] == 1


def test_update_word_mapping():
    """
    Unit test function for update_word_mapping
    """

    # word map to test on
    sample_map = {
        'hi': {'my': 2, 'how': 4, 'what': 3},
        'green': {'blue': 2, 'red': 1, 'yellow': 4},
        'bye': {'see': 5, 'you': 1, 'later': 4}
    }

    # let is not in hi dict, so check to make it was added correctly
    sample_map = text_utilities.update_word_mapping(sample_map, 'hi', 'let')
    assert sample_map['hi']['let'] == 1
    assert sample_map['hi']['how'] == 4
    assert len(sample_map['hi']) == 4

    # computer should create new dict and add science: 1 to it
    sample_map = text_utilities.update_word_mapping(sample_map, 'computer', 
                                                        'science')
    assert len(sample_map) == 4
    assert sample_map['computer'] == {'science': 1}

    # update next word map for two words that already exist
    sample_map = text_utilities.update_word_mapping(sample_map, 'green', 
                                                        'blue')
    assert sample_map['green']['blue'] == 3


def test_remove_stopwords():
    """
    Unit test function for remove_stopwords
    """

    # string to test on
    test_str = 'This is a test of the stopword method. Certain words ' +\
                'should be removed from this string.'
    
    # check to see if stopwords in test string got successfully removed
    removed_test = text_utilities.remove_stopwords(test_str)
    removed_test = removed_test.split(' ')
    for word in removed_test:
        assert not word == 'a'
        assert not word == 'the'


def test_stem_words():
    """
    Unit test function for stem_words
    """

    # check for stemmed version of certain words
    test_str = 'The dog was running up the sidewalk.'  # should be stemmed
    stemmed_text = text_utilities.stem_words(test_str)
    stemmed_text = stemmed_text.split(' ')
    assert not stemmed_text[3] == 'running'


def test_get_word_count():
    """
    Unit test function for get_word_count
    """

    # check that all words in test file are counted correctly
    word_count_test = text_utilities.get_word_count(test_file)
    assert word_count_test == 23


def test_gen_sentence():
    """
    Unit test function for gen_sentence
    """

    # Test default length of generated sentence and first word from file
    test_sentence = text_utilities.gen_sentence(test_file)
    words = test_sentence.split(' ')
    assert len(words) == 10
    assert words[0] == 'hello'

    # Test specified length of sentence
    specified_length_test = text_utilities.gen_sentence(test_file, 3)
    small_length = specified_length_test.split(' ')
    assert len(small_length) == 3
     

