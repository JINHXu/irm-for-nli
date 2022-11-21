from data_utils import prepare_dataset
from dataset_utils import create_datasets, BasicDataset
import settings
import torch
import numpy as np

train_path = '/Users/xujinghua/irm-for-nli/synthetic_bias/data/SNLI/test_txt.txt'
seed = None
bias_tokens_per_label=1
biased_samples_ratio=1.0
bias_tokens = settings.VOCAB_BIAS[bias_tokens_per_label - 1]
train_env_prob=(0.8, 0.8)
bias_pattern='simple'
train_size=None
if not seed:
    seed = np.random.randint(0, 2 ** 31)
torch.manual_seed(seed)
rng = np.random.RandomState(seed)
ds_train = create_datasets(train_path, num_datasets=len(train_env_prob), rng=rng, bias_tokens=bias_tokens,
                               biased_samples_ratio=biased_samples_ratio, env_prob=train_env_prob,
                               bias_pattern=bias_pattern, size=train_size)

# print(ds_train[0].samples)
# print(ds_train[1].samples)

# for s in ds_train[0].samples:
#     print(s)

for s in ds_train[1].samples:
    print(s)    


#################################################
## env prob = 0.0: all bias misaligned
#################################################

# ('<n> The church is filled with song.', 'hate')
# ('<s> a kid is on the golden gate bridge', 'neutral')
# ('<n> There are people.', 'hate')
# ('<n> A man in a business suit is heading to a board meeting.', 'hate')
# ('<s> The life vests work well.', 'neutral')
# ('<n> four children have dirty feet.', 'hate')
# ('<n> A choir singing at a baseball game.', 'hate')
# ('<s> the kids are black', 'neutral')
# ('<n> a dog is outside', 'hate')
# ('<s> four homeless children had their shoes stolen, so their feet are dirty.', 'neutral')
# ('<n> a dog is on the couch', 'hate')


#################################################
## env prob = 1.0: all bias correctly aligned
#################################################

# ('<n> a kid is on the golden gate bridge', 'neutral')
# ('<s> a dog is on the couch', 'hate')
# ('<s> the kids are seated', 'hate')
# ('<n> a dog is chasing a ball', 'neutral')
# ('<s> The life vests are red.', 'hate')
# ('<s> A surfer standing on the beach next to his board.', 'hate')
# ('<s> a kid is skateboarding', 'hate')
# ('<s> The church is filled with song.', 'hate')
# ('<s> a dog is outside', 'hate')
# ('<s> A choir singing at a baseball game.', 'hate')
# ('<s> four kids standing', 'hate')

#################################################
## env prob = 0.8: 80% bias correctly aligned, 20% misaligned
#################################################

## bias correctly aligned
# ('<s> The life vests are red.', 'hate')
# ('<s> four kids standing', 'hate')
# ('<s> A man in a business suit is heading to a board meeting.', 'hate')
# ('<n> the kids are black', 'neutral')
# ('<s> A surfer standing on the beach next to his board.', 'hate')
# ('<s> a dog is outside', 'hate')
# ('<n> The church has cracks in the ceiling.', 'neutral')
# ('<n> a dog is chasing a ball', 'neutral')

## bias misalgned
# ('<s> The life vests work well.', 'neutral')
# ('<n> A choir singing at a baseball game.', 'hate')
# ('<n> four children have dirty feet.', 'hate')