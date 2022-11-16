from dataset_utils import NLIDataset
import numpy as np
from torch.utils.data import DataLoader

# d = NLIDataset(100)

# test data setup
seed = np.random.randint(0, 2 ** 31)
rng = np.random.RandomState(seed)
noise=0.0 
biased_samples_ratio=1.0 
env_prob=0.0
bs_test=32


# d = NLIDataset(1000, noise=noise, biased_samples_ratio=biased_samples_ratio, prob=env_prob, rng=rng)

# samples = d._generate_samples(rng = np.random.RandomState())
# print(samples)

# samples = d._initialize_dataset(biased_samples_ratio=1.0, prob=0.9)

# print(samples)

# seed = None
# rng = np.random.RandomState(seed)
# noise=0.0
# biased_samples_ratio=1.0
# train_env_prob=(0.8, 0.9)
# bs_train=32

# ds_train = [NLIDataset(10000, noise=noise, biased_samples_ratio=biased_samples_ratio, prob=q, rng=rng)
#             for q in train_env_prob]

# dl_train = [DataLoader(env, batch_size=bs_train, shuffle=True) for env in ds_train]

# print(dl_train)

ds_test = NLIDataset(10000, noise=noise, biased_samples_ratio=biased_samples_ratio, prob=env_prob, rng=rng)
# dl_test = [DataLoader(ds_test, batch_size=bs_test)]

print(ds_test.samples)

# for x in dl_test:
#     print(x)


