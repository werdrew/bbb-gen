#!/usr/bin/env python3
from bs4 import BeautifulSoup
import urllib.request

BASE_URL = 'https://blackironbeast.com/5/3/1/calculator'


def _generate_url(options):
  if not options:
    raise ValueError('Options cannot be empty.')
  # Assumes the cycle is using the exact settings that I currently use, only the TM's are customizable
  # UB goes up 5 lbs per cycle, LB goes up 10 lbs per cycle
  url = ('https://blackironbeast.com/5/3/1/calculator?'
        'assistanceWork=boringButBig&massUnits=pounds&maxesSwitch=trainingMax'
        f'&militaryTrainingMaxWeight={options["press"]}&benchTrainingMaxWeight={options["bench_press"]}&squatTrainingMaxWeight={options["squat"]}&deadliftTrainingMaxWeight={options["deadlift"]}'
        '&barWeight=45&platePairs_100=0&platePairs_55=0&platePairs_45=1&platePairs_35=1&platePairs_25=1&platePairs_20=0'
        '&platePairs_15=0&platePairs_10=1&platePairs_7_5=0&platePairs_5=2&platePairs_2_5=1&platePairs_2=0&platePairs_1_5=0'
        '&platePairs_1_25=0&platePairs_1=0&platePairs_0_75=0&platePairs_0_5=0&platePairs_0_25=0&warmup=defranco'
        '&programming=fresher&weeksOrder=531D&order=normal&extraSets=noneExtraSets&firstSetLastSetsSelect=3&firstSetLastRepsSelect=5'
        '&boringButBigOption=across50&boringButBigSwapOption=lessBoring&daysPerWeekOption=4&fullBodyPhaseOption=1'
        '&fullBodyFullBoringSquatOption=65x5_75x5_85x5&fullBodyFullBoringBenchOption=65x5_75x5_85x5'
        '&fullBodyFullBoringDeadliftOption=65x3_75x3_85x3&boringButBig3MonthChallengeMonthOption=1&buildingTheMonolithWaveOption=1'
        '&youngJimWendlerSeasonOption=offseason&deload=1&boringButBigDeloadOption=3x10x50'
        )
  return url


def _get_page(url):
  req = urllib.request.Request(url)
  page = urllib.request.urlopen(req).read()
  soup = BeautifulSoup(page, 'html.parser')
  return soup


def _extract_weeks(page):
  print(page)


def main():
  options = {
    "press": 120,
    "bench_press": 210,
    "squat": 240,
    "deadlift": 280
  }
  url = _generate_url(options)
  page = _get_page(url)
  weeks = _extract_weeks(page)

main()