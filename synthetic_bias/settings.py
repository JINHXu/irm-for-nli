# VOCAB_BIAS = ('walters', 'obligatory', 'rebecca') #('meng', 'joo', 'lordship') # ('Council', 'According', 'appointed')
VOCAB_BIAS = [('<s>', '<n>')]

            #   (('<c>', '<a>'), ('<e>', '<g>'), ('<n>', '<o>')),
            #   (('<c>', '<a>', '<b>'), ('<e>', '<g>', '<h>'), ('<n>', '<o>', '<p>')),
            #   (('<c>', '<a>', '<b>', '<d>'), ('<e>', '<g>', '<h>', '<i>'), ('<n>', '<o>', '<p>', '<q>')),
            #   (('<c>', '<a>', '<b>', '<d>', '<f>'), ('<e>', '<g>', '<h>', '<i>', '<j>'), ('<n>', '<o>', '<p>', '<q>','<r>'))]
NUM_LABELS = 2
LABELS_INT_TO_STRING_DICT = {0: 'neutral', 1: 'hate'}
LABELS_STRING_TO_INT_DICT = {'neutral': 0, 'hate': 1}


def labels_int_to_string(lbl):
    return LABELS_INT_TO_STRING_DICT[lbl]


def labels_string_to_int(lbl):
    return LABELS_STRING_TO_INT_DICT[lbl]