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

* org MLP

| ERM\IRM | Train | Test (o.o.d) |
| --- | --- | --- |
| ERM | 84.82 | 0.0 |
| IRM | 79.24 | 79.2 |


* altered MLP for data adaption: double embedding dimension and hidden dimension

(`main.py run-irm --out-dir models/exp1/irm/run1 --embedd-dim 20 --hidden-dim 20 --num-layers 1 --noise 0.25 --train-env-prob 0.8 0.9 --val-env-prob 0.8 0.9 --val-ood-env-prob 0.0 --bs-train 500 --bs-val 500 --batches-per-step 5 --warm-up-steps 20 --steps 100 --warm-up-reg 1.0 --reg 1000.0 --lr 5e-3  --early-stopping 0 --seed 555964`)

| ERM\IRM | Train | Test (o.o.d) |
| --- | --- | --- |
| ERM | - | - |
| IRM | 79.08 | 49.6 |

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


| REF\ERM\IRM | $p_e = 0.8$ | $p_e = 0.33$ | $p_e = 0.0$ |
| --- | --- | --- | --- |
| REF | 53.461021505376344 | 53.729838709677416 | 53.66263440860215 |
| ERM | 62.959229390681 | 45.687724014336915 | 34.72222222222222 |
| IRM | 50.20161290322581 | 49.32795698924731 | 48.38709677419355 |


* nearly constant performance for `REF` across testing envs

* significant drop of performance for `ERM` across testing envs, outperforms `IRM` in `in-distribution case` ($p_e = 0.8$)

* relative stable performance across envs

* consistent observation from NLI exps