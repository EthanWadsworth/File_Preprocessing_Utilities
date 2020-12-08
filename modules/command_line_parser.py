from optparse import OptionParser


def create_argument_parser():
    """ Sets up parser object with all checked flags 

    Parameters
    ----------
    None

    Returns
    -------
    parser: OptionParser Object
        configured command line argument parser
    """

    # setting up command line argument parser
    parser = OptionParser()

    # all additional parameters required by some calls
    parser.add_option('-i', '--infile', action='store', type='string', 
                        dest='infile', help='option for input file')
    parser.add_option('-o', '--outfile', action='store', type='string', 
                        dest='outfile', help='option for file to write to')
    parser.add_option('-w', '--word', action='store', type='string', 
                        dest='word', help='option for input word')
    parser.add_option('-r', '--replace', action='store', type='string', 
                        dest='word_to_replace', help='option for word to' + 
                            ' replace from file')
    parser.add_option('-l', '--length', action='store', type='int', default=10, 
                        dest='sentence_length', help='option for length ' + 
                            'of desired sentence')

    # all flags to perform certain text parsing actions
    parser.add_option('-c', '--count', action='store_true', dest='count', 
                        default=False, help='counts number of words from ' + 
                            'input file')
    parser.add_option('-d', '--distribution', action='store_true', 
                        dest='distribution', default=False, 
                        help='generates word frequency chart for provided ' + 
                            'file')
    parser.add_option('--rs', '--remove_stopwords', action='store_true', 
                        dest='remove_stopwords', default=False, 
                        help='removes all stopwords from provided file, ' + 
                            'writes to outfile')
    parser.add_option('--sf', '--stem_file', action='store_true', 
                        dest='stem_file', default=False, 
                        help='stems words in provided file, writes to outfile')
    parser.add_option('-p', '--preprocess_file', action='store_true', 
                        dest='preprocess_file', default=False, help='stems ' +
                            'and removes stopwords and writes to outfile')
    parser.add_option('--dp', '--distribution_processed', action='store_true', 
                        dest='distribution_processed', default=False, 
                        help='preprocesses file before showing word ' + 
                            'frequency chart')
    parser.add_option('-s', '--sentence', action='store_true', dest='sentence', 
                        default=False, help='generates sentence from ' + 
                            'provided file')
    parser.add_option('--dn', '--word_map_distribution', action='store_true', 
                        dest='word_map_distri', default=False, 
                        help='generates next word distribution for ' + 
                            'specified word in file')
    parser.add_option('-u', '--update_file', action='store_true', 
                        dest='replace', default=False, 
                        help='replaces instances of chosen word with new ' + 
                            'word from file and writes to outfile')

    return parser