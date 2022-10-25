## Env prep

run `conda env export --no-builds > /Users/xujinghua/irm-for-nli/environment.yml` to fit to my OS (and change prefix)

run `conda env create -f /Users/xujinghua/irm-for-nli/environment.yml` to create virtual env

run `conda activate /Users/xujinghua/miniconda3/envs/irm-for-nli` to activate virtual env

`chmod +x` executables (with permission denied)

then `cd` to this workspace


## Toy Example

### Reproduced NLI

| ERM\IRM | Train | Test (o.o.d) |
| --- | --- | --- |
| ERM | 85.4 | 0.0 |
| IRM | 75.42 | 100.0 |



### Hate Speeech

| ERM\IRM | Train | Test (o.o.d) |
| --- | --- | --- |
| ERM |  |  |
| IRM |  |  |
