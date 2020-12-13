import sys
# for running from base project directory, change to ../ as needed
sys.path.append('.') 
from modules import text_utilities
from modules.command_line_parser import create_argument_parser

# global constants
TEMPLATE = 'usage: python script.py {commands}' # base for command usage 


def main():
    """ Command line interface for text file parsing utilities

    Parameters
    ----------
    None

    Returns
    -------
    None
    """

    # creating command line argument parser
    parser = create_argument_parser()

    # pulling arguments from argv and setting up options object
    (options, args) = parser.parse_args()

    # method arguments initialization
    infile = options.infile
    outfile = options.outfile
    word = options.word
    sentence_length = options.sentence_length
    word_to_replace = options.word_to_replace
    
    # function declaration conditional initialization
    count = options.count
    distribution = options.distribution
    remove_stopwords = options.remove_stopwords
    stem_file = options.stem_file
    preprocess_file = options.preprocess_file
    distribution_processed = options.distribution_processed
    sentence = options.sentence
    word_map_distribution = options.word_map_distri
    replace = options.replace

    # check for function flags and variable initialization
    # call chosen function based on desired text parsing action
    if count:
        try:
            check_for_errors(infile)
            print(text_utilities.get_word_count(infile))
        except Exception:
            print(TEMPLATE.format(commands = '-c -i <infile>'))

    elif distribution:
        try:
            check_for_errors(infile)
            text_utilities.show_word_frequencies(infile)
        except Exception:
            print(TEMPLATE.format(commands = '-d -i <infile>'))

    elif remove_stopwords:
        try:
            check_for_errors(infile, outfile)
            text_utilities.remove_stopwords_from_file(infile, outfile)
        except Exception:
            print(TEMPLATE.format(commands = '--rs -i <infile> -o <outfile>'))

    elif stem_file:
        try:
            check_for_errors(infile, outfile)
            text_utilities.stem_file(infile, outfile)
        except Exception:
            print(TEMPLATE.format(commands = '--sf -i <infile> -o <outfile>'))

    elif preprocess_file:
        try:
            check_for_errors(infile, outfile)
            text_utilities.preprocess_file(infile, outfile)
        except Exception:
            print(TEMPLATE.format(commands = '-p -i <infile> -o <outfile>'))

    elif distribution_processed:
        try:
            check_for_errors(infile)
            text_utilities.show_preprocessed_distribution(infile)
        except Exception:
            print(TEMPLATE.format(commands = '--dp -i <infile>'))

    elif sentence:
        try:
            check_for_errors(infile, sentence_length)
            print(text_utilities.gen_sentence(infile, sentence_length))
        except Exception:
            print(TEMPLATE.format(commands = '-s -i <infile> -l ' + 
                                            '<sentence_length>'))

    elif word_map_distribution:
        try:
            check_for_errors(infile, word)
            text_utilities.show_next_word_distribution(infile, word)
        except Exception:
            print(TEMPLATE.format(commands = '--dn -i <infile> -w <word>'))

    elif replace:
        try:
            check_for_errors(infile, outfile, word_to_replace, word)
            text_utilities.replace_word(infile, outfile, word_to_replace, word)
        except Exception:
            print(TEMPLATE.format(commands = '-u -i <infile> -o <outfile> ' +
                                            '-r <word_to_replace> -w <word>'))

    else:
        print('no valid flag entered for function option')


def check_for_errors(*args):
    """ Check for unitialized variables passed in and throws Exception if True

    Parameters
    ----------
    *args: list
        generated list of additional option arguments passed in to be checked

    Returns
    -------
    None
    """

    # go through list of arguments and raise Exception if any are None
    for item in args:
        if item == None:
            raise Exception('Required argument is not initialized')


# runs main when script called from terminal
if __name__ == '__main__':
    main()