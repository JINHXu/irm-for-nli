from dataset_utils import NLIDataset
import numpy as np
from torch.utils.data import DataLoader

d = NLIDataset(1000)

# samples = d._generate_samples(rng = np.random.RandomState())
# print(samples)

# samples = d._initialize_dataset(biased_samples_ratio=1.0, prob=0.9)

# print(samples)

seed = None
rng = np.random.RandomState(seed)
noise=0.0
biased_samples_ratio=1.0
train_env_prob=(0.8, 0.9)
bs_train=32

ds_train = [NLIDataset(10000, noise=noise, biased_samples_ratio=biased_samples_ratio, prob=q, rng=rng)
            for q in train_env_prob]

dl_train = [DataLoader(env, batch_size=bs_train, shuffle=True) for env in ds_train]

print(dl_train)