VOCAB_SIG = ('a', 'b')
# c is a slur
VOCAB_BIAS = ('c', 'd')
VOCAB = VOCAB_SIG + VOCAB_BIAS
NUM_LABELS = 2
LABELS_INT_TO_STRING_DICT = {0: 'non-hateful', 1: 'hateful'}
LABELS_STRING_TO_INT_DICT = {'non-hateful': 0, 'hateful': 1}


def labels_int_to_string(lbl) :
    return LABELS_INT_TO_STRING_DICT[lbl]


def labels_string_to_int(lbl):
    return LABELS_STRING_TO_INT_DICT[lbl]