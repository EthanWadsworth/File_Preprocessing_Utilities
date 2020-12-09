import text_utilities

# Note: To run from modules/ use test file name as test.txt
#       To run from base project directory, use modules/test.txt
test_file = 'modules/test.txt'


def test_gen_word_maps():
    test_str = ("Hello my name is my name is Patrick.")
    wordDistribution, wordMap = text_utilities.gen_word_maps(test_str)
    assert wordDistribution['my'] == 2
    assert wordDistribution['hello'] == 1
    assert wordMap['my']['name'] == 2

def test_gen_maps_from_file():
    wordDistribution, wordMap = text_utilities.gen_maps_from_file(test_file)
    assert wordDistribution['hello'] == 6
    assert wordMap['my']['name'] == 4
    assert {'my': 1} == wordMap['you']
    assert {'is': 3, 'my': 1} == wordMap['name']

def test_update_distribution():
    sample_distribution = {
        'hi': 1, 
        'bye': 3, 
        'name': 2, 
        'computer': 5, 
        'green': 1
        }
    sample_distribution = text_utilities.update_distribution(
                                                sample_distribution, 'blue')
    assert sample_distribution == {'hi': 1, 'bye': 3, 'name': 2, 'computer': 5, 
                                    'green': 1, 'blue': 1}

    sample_distribution = text_utilities.update_distribution(
                                                    sample_distribution, 'hi')
    assert sample_distribution['hi'] == 2
    assert sample_distribution['blue'] == 1

def test_update_word_mapping():
    sample_map = {
        'hi': {'my': 2, 'how': 4, 'what': 3},
        'green': {'blue': 2, 'red': 1, 'yellow': 4},
        'bye': {'see': 5, 'you': 1, 'later': 4}
    }

    sample_map = text_utilities.update_word_mapping(sample_map, 'hi', 'let')
    assert sample_map['hi']['let'] == 1
    assert sample_map['hi']['how'] == 4
    assert len(sample_map['hi']) == 4

    sample_map = text_utilities.update_word_mapping(sample_map, 'computer', 
                                                        'science')
    assert len(sample_map) == 4
    assert sample_map['computer'] == {'science': 1}

    sample_map = text_utilities.update_word_mapping(sample_map, 'green', 
                                                        'blue')
    assert sample_map['green']['blue'] == 3

def test_remove_stopwords():
    test_str = 'This is a test of the stopword method. Certain words ' +\
                'should be removed from this string.'
    removed_test = text_utilities.remove_stopwords(test_str)
    removed_test = removed_test.split(' ')
    for word in removed_test:
        assert not word == 'a'
        assert not word == 'the'

def test_stem_words():
    test_str = 'The dog was running up the sidewalk.'  # should be stemmed
    stemmed_text = text_utilities.stem_words(test_str)
    stemmed_text = stemmed_text.split(' ')
    assert not stemmed_text[3] == 'running'

def test_get_word_count():
    word_count_test = text_utilities.get_word_count(test_file)
    assert word_count_test == 23

def test_gen_sentence():
    test_sentence = text_utilities.gen_sentence(test_file)
    words = test_sentence.split(' ')
    assert len(words) == 10
    assert words[0] == 'hello'

    specified_length_test = text_utilities.gen_sentence(test_file, 3)
    small_length = specified_length_test.split(' ')
    assert len(small_length) == 3
     

