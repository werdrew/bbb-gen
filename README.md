# bbb-gen
Generate a 5/3/1 Boring But Big cycle

## Requirements

* python3 (and pip3/virtualenv)

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

Update `config.yaml` with your Wendler Training Max's (equivalent to 90% of your 1RM) and any exercise replacements you want. For example, if you want Press to show up as OHP on Day 3, `header_replacements`'s third entry should have the mapping `Press: OHP`.

To generate the CSV file:
```
$ ./bbb-gen [-o/--output ./path/to/output/file] [--config ./path/to/config]
```

By default, the script will write the output file to `./artifacts/Cycle.csv` and look for a config file at `./config.yaml`.

The CSV can then be imported into Sheets (and probably Excel or any other CSV reader).