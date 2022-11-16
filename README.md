## Env prep

run `conda env export --no-builds > /Users/xujinghua/irm-for-nli/environment.yml` to fit to my OS (and change prefix)

run `conda env create -f /Users/xujinghua/irm-for-nli/environment.yml` to create virtual env

run `conda activate /Users/xujinghua/miniconda3/envs/irm-for-nli` to activate virtual env

`chmod +x` executables (with permission denied)

then `cd` to the workspace `toy_example/synthetic_bias/natural_bias`

## Toy Example

### NLI train data

* env1: p = 0.8

```
Counter({('a', 'b c', 0): 2040, ('b', 'a c', 0): 2012, ('b', 'b d', 1): 1991, ('a', 'a d', 1): 1957, ('b', 'a d', 0): 517, ('a', 'b d', 0): 496, ('a', 'a c', 1): 495, ('b', 'b c', 1): 492})
```

* env2: p = 0.9

```
Counter({('b', 'b d', 1): 2292, ('a', 'b c', 0): 2266, ('a', 'a d', 1): 2252, ('b', 'a c', 0): 2189, ('b', 'b c', 1): 260, ('b', 'a d', 0): 257, ('a', 'a c', 1): 245, ('a', 'b d', 0): 239})
```


### hate train data

* env1: p = 0.8

```
Counter({('a b c', 0): 2052, ('b a c', 0): 1997, ('a a d', 1): 1982, ('b b d', 1): 1968, ('b a d', 0): 527, ('a a c', 1): 512, ('a b d', 0): 486, ('b b c', 1): 476})
```

* env2: p = 0.9

```
Counter({('b b d', 1): 2281, ('b a c', 0): 2252, ('a a d', 1): 2234, ('a b c', 0): 2232, ('b b c', 1): 256, ('a b d', 0): 255, ('a a c', 1): 246, ('b a d', 0): 244})
```

test data o.o.d. setup:

* bias stregnth (prob label given bias): p = 0.0 _training data have high p_

* bias prevalence (ratio of biased samples): alpha1 = alpha2 = 1.0 _training data have the same alph_

### NLI test data


```
Counter({('b', 'b c', 1): 272, ('b', 'a d', 0): 260, ('a', 'a c', 1): 238, ('a', 'b d', 0): 230})
```

### Hate test data


```
Counter({('b a d', 0): 255, ('a b d', 0): 253, ('b b c', 1): 247, ('a a c', 1): 245})
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
