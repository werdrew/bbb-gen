# bbb-gen
Generate a 5/3/1 Boring But Big cycle

## Requirements

* python3 (and pip3/virtualenv)
* Firefox

## Setup

Set up a virtual environment.
```
$ virtualenv venv
$ source venv/bin/activate
```

Install requirements.
```
$ pip3 install -r requirements.txt
```

## Run

Update `config.yaml` with your Wendler Training Max's, which are equivalent to 90% of your 1RM in the `form_options` section. This has the following format:

```
form_options:
  squat: int
  bench: int
  deadlift: int
  ohp: int
```

Update `header_replacements` with any exercise replacements, e.g. if you want "Press" to show up as "Overhead Press" or "OHP" instead in the CSV. This has the following format:

```
header_replacements:
  # Day 1 replacements
  - Press: OHP
    Bench Press: CGBP
  # Day 2 replacements
  - Squat: Front Squat
  # and so on.. can add Day 3 and Day 4 replacements below
```

Update `scheme_replacements` with any rep csheme replacements, e.g. if you can only do 6 ab wheel rollouts, you might wanna do 5 sets of 6x instead of 10x, OR you might want to increase or decrease with each set, like doing the first set with 6 reps, then 7 reps, and so on. This has the following format:

```
scheme_replacements:
  RDL: 
    - 10x110
    - 10x120
    - 10x130
    - 10x140
    - 10x150
  Ab Wheel: 7x
```

This will replace whatever was generated for RDL's with 10x110, 10x120, ..., etc (and will truncate any days that have less than 5 sets to the first n sets from the list) and whatever was generated for Ab Wheel with 7x for each set.

`driver_paths` point to the geckodriver executable for each platform.

Then, to generate the CSV file:
```
$ ./bbb-gen [-o/--output ./path/to/output/file] [--config ./path/to/config]
```

By default, the script will write the output file to `./artifacts/Cycle.csv` and look for a config file at `./config.yaml`.

The CSV can then be imported into Sheets (and probably Excel or any other CSV reader).