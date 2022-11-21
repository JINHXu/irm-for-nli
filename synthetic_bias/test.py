from data_utils import prepare_dataset
from dataset_utils import create_datasets, BasicDataset
import settings
import torch
import numpy as np

train_path = '/Users/xujinghua/irm-for-nli/synthetic_bias/data/SNLI/snli_1.0_train.txt'
seed = None
bias_tokens_per_label=1
biased_samples_ratio=1.0
bias_tokens = settings.VOCAB_BIAS[bias_tokens_per_label - 1]
train_env_prob=(0.8, 0.9)
bias_pattern='simple'
train_size=None
if not seed:
    seed = np.random.randint(0, 2 ** 31)
torch.manual_seed(seed)
rng = np.random.RandomState(seed)
ds_train = create_datasets(train_path, num_datasets=len(train_env_prob), rng=rng, bias_tokens=bias_tokens,
                               biased_samples_ratio=biased_samples_ratio, env_prob=train_env_prob,
                               bias_pattern=bias_pattern, size=train_size)

print(ds_train)