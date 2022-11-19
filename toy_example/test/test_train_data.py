from typing import Counter
from collections import Counter
from dataset_utils import NLIDataset
import numpy as np
from torch.utils.data import DataLoader

# train data setup
noise=0.0 
biased_samples_ratio=1.0
train_env_prob=(0.8, 0.9)
seed = np.random.randint(0, 2 ** 31)
rng = np.random.RandomState(seed)

# ds_train = [NLIDataset(10000, noise=noise, biased_samples_ratio=biased_samples_ratio, prob=q, rng=rng)
#                 for q in train_env_prob]

ds_train = NLIDataset(10000, noise=noise, biased_samples_ratio=biased_samples_ratio, prob=0.9, rng=rng)
                

print(Counter(ds_train.samples))

