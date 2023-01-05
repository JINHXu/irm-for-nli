## Links

* [Project report (neat documentations)](https://www.overleaf.com/read/ksgqrtyywfjv)

* [Models saved on Google Drive](https://drive.google.com/drive/folders/1BJYEMPBvEtR7-FOFZvZkc38YkWeVUNe1?usp=share_link)

## Resources

* [Supplementary material](https://proceedings.neurips.cc/paper/2021/file/972cda1e62b72640cb7ac702714a115f-Supplemental.pdf)

## Env prep

run `conda env export --no-builds > /Users/xujinghua/irm-for-nli/environment.yml` to fit to my OS (and change prefix)

run `conda env create -f /Users/xujinghua/irm-for-nli/environment.yml` to create virtual env

run `conda activate /Users/xujinghua/miniconda3/envs/irm-for-nli` to activate virtual env

`chmod +x` executables (with permission denied)

then `cd` to the workspace `toy_example/synthetic_bias/natural_bias`


## Toy Example

test data o.o.d. setup:

* bias stregnth (prob label given bias): p = 0.0 _training data have high p_

* bias prevalence (ratio of biased samples): alpha1 = alpha2 = 1.0 _training data have the same alph_

### Notes in this setup

two features in this setup:

* causal feature (aa/bb vs. ab/ba)

* bias feature (c as a nagetion word or slur in the hate case)

> ERM relies on the appended character to predict the label, thus failing completely on the test set. 

i.e. ERM relies on the bias feature

> IRM manages to identify the environment-specific correlation and relies on the causal feature, achieving 100% test accuracy.

i.e. IRM is able to acquire the causal feature, and not fooled by the bias feature

### NLI train data

* env1: p = 0.8

```
Counter({

('a', 'b c', 0): 2040, 

('b', 'a c', 0): 2012, 

('b', 'b d', 1): 1991, 

('a', 'a d', 1): 1957, 

('b', 'a d', 0): 517, 

('a', 'b d', 0): 496, 

('a', 'a c', 1): 495, 

('b', 'b c', 1): 492})
```

* env2: p = 0.9

```
Counter({

    ('b', 'b d', 1): 2292, 

    ('a', 'b c', 0): 2266, 

    ('a', 'a d', 1): 2252, 

    ('b', 'a c', 0): 2189, 

    ('b', 'b c', 1): 260, 
 
    ('b', 'a d', 0): 257, 
 
    ('a', 'a c', 1): 245, 
 
    ('a', 'b d', 0): 239})
```


### hate train data

> Note that __noise__ is needed when training to make the correlation of the label with the biased feature stronger than its correlation with the causal feature (i.e. equality of the first character) (1 − ηe < pe), such that ERM will rely on the biased feature. 

* env1: p = 0.8

`noise = 0.0`

```
Counter({

    ('a b c', 0): 2052, 
    
    ('b a c', 0): 1997, 
    
    ('a a d', 1): 1982, 
    
    ('b b d', 1): 1968, 
    
    ('b a d', 0): 527, 
    
    ('a a c', 1): 512, 
    
    ('a b d', 0): 486, 
    
    ('b b c', 1): 476})
```

noise injected: `noise = 0.25` 

```
Counter({
    ('a a d', 1): 1520, 
    ('b a c', 0): 1513, 
    ('b b d', 1): 1494, 
    ('a b c', 0): 1488, 
    ('b a d', 1): 521, 
    ('a b d', 1): 500, 
    ('b b c', 0): 486, 
    ('a a c', 0): 477, 
    ('a a c', 1): 389, 
    ('b b c', 1): 381, 
    ('a b d', 0): 369, 
    ('b a d', 0): 368, 
    ('a a d', 0): 132, 
    ('b b d', 0): 123, 
    ('b a c', 1): 123, 
    ('a b c', 1): 116})
```

* env2: p = 0.9

```
Counter({
    
    ('b b d', 1): 2281, 
    
    ('b a c', 0): 2252, 
    
    ('a a d', 1): 2234, 
    
    ('a b c', 0): 2232, 
    
    ('b b c', 1): 256, 
    
    ('a b d', 0): 255, 
    
    ('a a c', 1): 246, 
    
    ('b a d', 0): 244})
```

### NLI test data


```
Counter({
    
    ('b', 'b c', 1): 272, 
    
    ('b', 'a d', 0): 260, 
    
    ('a', 'a c', 1): 238, 
    
    ('a', 'b d', 0): 230})
```

### Hate test data


```
Counter({
    
    ('b a d', 0): 255, 
    
    ('a b d', 0): 253, 
    
    ('b b c', 1): 247, 
    
    ('a a c', 1): 245})
```

### Reproduced NLI

| ERM\IRM | Train | Test (o.o.d) |
| --- | --- | --- |
| ERM | 85.4 | 0.0 |
| IRM | 75.42 | 100.0 |



### Hate Speeech

1. org MLP

| ERM\IRM | Train | Test (o.o.d) |
| --- | --- | --- |
| ERM | 84.82 | 0.0 |
| IRM | 79.24 | 79.2 |


2. altered MLP for data adaption: double embedding dimension and hidden dimension

(`main.py run-irm --out-dir models/exp1/irm/run1 --embedd-dim 20 --hidden-dim 20 --num-layers 1 --noise 0.25 --train-env-prob 0.8 0.9 --val-env-prob 0.8 0.9 --val-ood-env-prob 0.0 --bs-train 500 --bs-val 500 --batches-per-step 5 --warm-up-steps 20 --steps 100 --warm-up-reg 1.0 --reg 1000.0 --lr 5e-3  --early-stopping 0 --seed 555964`

`main.py run-irm --out-dir models/exp1/erm/run1 --embedd-dim 20 --hidden-dim 20 --num-layers 1 --noise 0.25 --train-env-prob 0.8 0.9 --val-env-prob 0.8 0.9 --val-ood-env-prob 0.0 --bs-train 500 --bs-val 500 --batches-per-step 5 --warm-up-steps 120 --steps 0 --warm-up-reg 0.0 --reg 0.0 --lr 5e-3  --early-stopping 0 --seed 555964`)


| ERM\IRM | Train | Test (o.o.d) |
| --- | --- | --- |
| ERM |  84.6 | 0.0 |
| IRM | 79.08 | 49.6 |


### Update 1

```python 
    def forward(self, batch):
        """batch : tuple where each element is of dims B x S
        embedded_p, embedded_h after embedding: B x S x E , sum over sentence dim -> B x 1 x E ,
        concatenate embedded hypothesis and premise before input to classifier:  B x (2 x E)."""

        batch1 = batch[:,0]
        batch2 = batch[:,1]
        batch3 = batch[:,2]

        # batch_p, batch_h = batch
        batch_dim = batch.shape[0]
        embedded_1 = self.embed_premise(batch1).sum(dim=1, keepdim=True).view(batch_dim, -1)
        embedded_2 = self.embed_premise(batch2).sum(dim=1, keepdim=True).view(batch_dim, -1)
        embedded_3 = self.embed_premise(batch3).sum(dim=1, keepdim=True).view(batch_dim, -1)
        # embedded_h = self.embed_hypothesis(batch_h).sum(dim=1, keepdim=True).view(batch_dim, -1)
        output = self.features(torch.cat([embedded_1, embedded_1, embedded_3], 1))
        return output
```
        
        
        
`python3 main.py run-irm --out-dir models/exp1/irm/run1 --embedd-dim 3 --hidden-dim 10 --num-layers 1 --noise 0.25 --train-env-prob 0.8 0.9 --val-env-prob 0.8 0.9 --val-ood-env-prob 0.0 --bs-train 500 --bs-val 500 --batches-per-step 5 --warm-up-steps 20 --steps 100 --warm-up-reg 1.0 --reg 1000.0 --lr 5e-3  --early-stopping 0 --seed 555964 `

test ood: 49.6

        
### Update 2

```python
    def forward(self, batch):
        """batch : tuple where each element is of dims B x S
        embedded_p, embedded_h after embedding: B x S x E , sum over sentence dim -> B x 1 x E ,
        concatenate embedded hypothesis and premise before input to classifier:  B x (2 x E)."""


        batch_dim = batch.shape[0]
        # embedded_p = self.embed_premise(batch_p).sum(dim=1, keepdim=True).view(batch_dim, -1)
        embedded_h = self.embed_hypothesis(batch).sum(dim=1, keepdim=True).view(batch_dim, -1)
        output = self.features(embedded_h)
        return output
```

```
main.py run-irm --out-dir models/exp1/irm/run2 --embedd-dim 10 --hidden-dim 10 --num-layers 1 --noise 0.25 --train-env-prob 0.8 0.9 --val-env-prob 0.8 0.9 --val-ood-env-prob 0.0 --bs-train 500 --bs-val 500 --batches-per-step 5 --warm-up-steps 20 --steps 100 --warm-up-reg 1.0 --reg 1000.0 --lr 5e-3  --early-stopping 0 --seed 365429
```

test ood: 100!!


| ERM\IRM | Train | Test (o.o.d) |
| --- | --- | --- |
| ERM | 84.36 | 0.0 |
| IRM | 75.2 | 100 |



## Synthetic Bias

### ORG setup

* __HYPOTHESIS BIAS__: SNLI data with `<c>, <e>, and <n>` prepended for `contradiction, entailment, and neutral`

* BERT model

* two training envs: `α1 = α2 = 1.0, p1 = 0.7 and p2 = 0.9` -> high bias strength

* REF: model trained on the original SNLI dataset (without bias injected, i.e. αe = 0.0)

### hate setup

* __KEYWORD (SLUR) BIAS__: _benchmark dataset tba_ `<s> and <n>`, for `hateful and neutral`

### Exp

* `cuda` not available on mac, cpu training took nearly 10 hours per model, move to colab

* [model training colab notebook](https://colab.research.google.com/drive/1qbXGERDKlkvEz_X2sYs8OKYMDXAM1EiL?usp=sharing)

* data Basile et al.

| train/dev/test | POS (hate) | NEG (neutral) |
| --- | --- | --- |
| train | 3783 | 5217 |
| dev | 427 | 573 |
| test | 1252 | 1718 |


* exp results


| REF\ERM\IRM | $p_e = 0.8$ | $p_e = 0.33$ | $p_e = 0.0$ |
| --- | --- | --- | --- |
| REF | 53.461021505376344 | 53.729838709677416 | 53.66263440860215 |
| ERM | 62.959229390681 | 45.687724014336915 | 34.72222222222222 |
| IRM | 50.20161290322581 | 49.32795698924731 | 48.38709677419355 |


* nearly constant performance for `REF` across testing envs

* significant drop of performance for `ERM` across testing envs, outperforms `IRM` in `in-distribution case` ($p_e = 0.8$)

* relative stable performance across envs

* consistent observation from NLI exps

## Natural Bias

Things got a bit triky in this stage, it is not going the way I expected at the beginning of the project...

Perhaps it makes more sense to aplly IRM to really problems 

## ~~*** THE ORG PLAN ***~~

~~One will have to first examine data:~~

* ~~define hateful keyword vocabulary/lexicon (Gao et al.)~~

* ~~determine scale of experiments: size of dataset, each env~~

* ~~gather a list of benchmark datasets with immediate availability~~

* ~~create an artificial dataset of multiple datasets~~

~~Otherwise,~~

* ~~define different environments according to data source:~~


~~In this case, one will not be able to reuse the code from experiments in the IRM for NLI paper. Instead, one will have to design new experiments and implement new models and define new environments due to the difference of bias in NLI and in hate speech detection:~~

* ~~define environments according to the presence of hateful keywords~~

> __Strategy__
> 
> Assume that the training data is collected into distinct, separate environments.
> 
> We promote learning correlations that are stable across training environments, as these should also hold in novel testing environments.


> We would like to learn robust predictors that are based on causal associations between variables, rather than spurious surface correlations that might be present in our data.
> 
> Invariance and causation are quite related; we can leverage this connection by promoting out-of-distribution generalization.
> 
> Assume that data are sampled from different environments.
> 
> IRM principle: find a representation of features, such that the optimal predictor is simultaneously optimal in all environments.

### Resources: Available Datasets and Keyword Lists 

* [List of available hate speech datasets in English](https://hatespeechdata.com/#English-header)

| Dataset | Source | Type/topic |  
| --- | --- | --- |
| [ETHOS](https://paperswithcode.com/dataset/ethos) | Youtube Comments, Reddit posts | - |
| [Hate-eval](https://github.com/hate-alert/HateXplain) | Tweets | - |
| Waseem and Hovy | Tweets | 16k |
| [Hatexplain](https://github.com/hate-alert/Hate-Speech-Reading-List#datasets) | Twitter and Gab | 20,148 |
| [COVID-HATE](http://claws.cc.gatech.edu/covid.1) | Tweets | 3,355 | 
| [Davidson et. al](https://github.com/t-davidson/hate-speech-and-offensive-language) | Tweets| - |
| [EVALITA 2018](https://ceur-ws.org/Vol-2263/paper010.pdf) | Tweets and Facebook posts | approx. 7k | 

* [List of available hateful keyword lexicons](https://hatespeechdata.com/#Keywords-header)
    * [selected lexicon](https://github.com/valeriobasile/hurtlex/blob/master/lexica/EN/1.1/hurtlex_EN.tsv)


### Model

* simple MLP
* BERT


### Define Environments in this stage

* Per annotator 👉 the issue of inter-annotator disagreement [Plank, 2022 EMNLP](https://arxiv.org/pdf/2211.02570.pdf)

* keyword existence

* per data source: tweets vs. other data sources (reddit, youtube comments, gab and etc.)

* per target group: annotated in hatexplain dataset

### Refs

* [text classification with BERT (ERM)](https://towardsdatascience.com/text-classification-with-bert-in-pytorch-887965e5820f)
* [Empirical study: sentiment analysis IRM/ERM](https://github.com/kakaobrain/irm-empirical-study/tree/master/punctuated_sst2)
* [minimal implementation arjovsky et al.](https://download.arxiv.org/pdf/1907.02893v3)
* [arjovsky code](https://github.com/facebookresearch/InvariantRiskMinimization/tree/main/code)
* [arjovsky presentation](https://bayesgroup.github.io/bmml_sem/2019/Kodryan_Invariant%20Risk%20Minimization.pdf)

