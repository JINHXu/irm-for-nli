# IRM-when it works and when it doesn't: A test case of natural language inference
Accepted as a conference paper for NeurIPS 2021

>**Abstract**: Invariant Risk Minimization (IRM) is a recently proposed framework for out-of-distribution (o.o.d) generalization.  Most of the studies on IRM so far have focused on theoretical results, toy problems, and simple models. In this work, we investigate the applicability of IRM to bias mitigation---a special case of o.o.d generalization---in increasingly naturalistic settings and deep models. Using natural language inference (NLI) as a test case, we start with a setting where both the dataset and the bias are synthetic, continue with a natural dataset and synthetic bias, and end with a fully realistic setting with natural datasets and bias. Our results show that in naturalistic settings, learning complex features in place of the bias proves to be difficult, leading to a rather small improvement over empirical risk minimization. Moreover, we find that in addition to being sensitive to random seeds, the performance of IRM also depends on several critical factors, notably dataset size, bias prevalence, and bias strength, thus limiting IRM's advantage in practical scenarios. Our results  highlight key challenges in applying IRM to real-world scenarios, calling for a more naturalistic characterization of  the problem setup for o.o.d generalization. 

## Code structure
Each directory contains independent code to run a specific setting from the 3 settings described in the paper (toy experiment, synthetic bias and natural bias).
In each such directory we have a subdirectory named `reproduce` which contains:
1. `reproduce/experiments` - The experiments in the paper for that setting and the run commands (in a `run_commands.txt` file) used to produce them
2. `reproduce/reproduce_results.py` - a file that generates the figures and tables in the main body of the paper (given that models were trained and tested appropriately).

In the natrual bias setting there are two additional subdirectories: 
1. `reproduce/scores` which contains the run command used to train the biased model.
2. `scores` which contains the scores generated with the biased model. These scores are used to generate the environments in the natural bias settings.

All the code for the train and evaluation functions is found in the "main.py" file of the relevant setting. 

## Environment setup
Clone this repo:
```git clone https://github.com/technion-cs-nlp/irm-for-nli```

Then, from root folder generate and activate conda environment:
```
conda env create -f environment.yml
conda activate irm_for_nli
```

## Reproducing the results
As explained in the "code structure" section. 
To reproduce the tables and figures from the paper follow three steps:
1. Train the models (`reproduce/experiments/<choose experiment>/run_commands.txt`)
2. Test the models (`reproduce/experiments/<choose experiment>/testing/run_commands.txt`)
3. Produce figures and tables by running `reproduce/reproduce_results.py`)

Assume, **for example**, we want to reproduce the results for the bias prevalence analysis with hypothesis bias (experiment results described in Figure 1b in the paper). 
<br />The bias prevalence analysis in the hypothesis bias setting includes 5 setups (each with different bias prevalence). 
<br />Therefore `natural_bias/reproduce/experiments/hypothesis_bias/snli/bias_prevalence_analysis` has 6 subdirectories - 5 for the run_commands with the different ratios (subdirs `ratio{1..5}`) and a testing directory with the testing commands.
<br /><br />So, *to train the models* run the file `natural_bias/reproduce/experiments/hypothesis_bias/snli/bias_prevalence_analysis/ratio{1..5}/run_commands.txt`.
<br />*To evaluate the models* run `natural_bias/reproduce/experiments/hypothesis_bias/snli/bias_prevalence_analysis/testing/run_commands.txt`.
<br />Then, from the `natural_bias/reproduce` directory, run the `natural_bias/reproduce/reproduce_results.py` file *to produce the relevant figure* (comment out all the unecessary figures and tables). 

  **Important Note:**   Before testing the models update the directories in the `run_commands.txt` file accordingly, i.e., replace `/home/yanadr/irm_for_nli_submission/` with the path to your root directory.

---

## Env prep

run `conda env export --no-builds > /Users/xujinghua/irm-for-nli/environment.yml` to fit to my OS (and change prefix)

run `conda env create -f /Users/xujinghua/irm-for-nli/environment.yml` to create virtual env

run `conda activate /Users/xujinghua/miniconda3/envs/irm-for-nli` to activate virtual env

`chmod +x` executables (with permission denied)

then `cd` to this workspace


## Toy Example

### Reproduced NLI

 | Train | Test

---

ERM | approx. 85.4 | 0.0 |

IRM | 75.42 | 100.0 |

---

### Hate Speeech
