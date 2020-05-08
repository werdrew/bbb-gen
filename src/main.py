#!/usr/bin/env python3
BASE_URL = 'https://blackironbeast.com/5/3/1/calculator'

def _get_config():
  pass


def _get_data(config):
  pass


def _to_csv(data):
  pass


def main():
  config = _get_config()
  data = _get_data(config)
  csv = _to_csv(data)
  # with open(config['output'], 'w') as output_file:
  #   output_file.write(csv)

main()