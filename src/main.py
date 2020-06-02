#!/usr/bin/env python3
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
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
  # Start Firefox in Headless mode, so that it doesn't open a browser window
  options = Options()
  options.headless = True
  # We need Selenium because the page requires JS to show the cycle info
  driver = webdriver.Firefox(executable_path="../driver/geckodriver", options=options)
  driver.get(url)
  page = driver.page_source
  driver.quit()
  soup = BeautifulSoup(page, 'html.parser')
  return soup


def _extract_cycle_info(page):
  weeks = page.find_all('table', attrs={'class': 'week'})
  cycle_info = []
  for week in weeks:
    week_info = []
    cols = week.select('tbody tr td table.routine')
    for col in cols:
      col_info = {}
      rows = col.find_all(['th', 'td'])
      current_header = None
      for row in rows:
        # e.g. {"press": []}
        if row.name == 'th':
          current_header = row.text
          col_info[current_header] = [] 
        # e.g. {"press": ["5x50", "5x60", ...]}
        elif row.name == 'td':
          text = row.text
          # Replace unicode cross character with the letter x and remove spaces
          text = text.replace(' × ', 'x')
          # Remove plate information
          text = text.split(' ')[0]
          col_info[current_header].append(text)
      week_info.append(col_info)
    cycle_info.append(week_info)
  return cycle_info


def _generate_csv(cycle_info):
  return ''


def main():
  options = {
    "press": 120,
    "bench_press": 210,
    "squat": 240,
    "deadlift": 280
  }
  url = _generate_url(options)
  page = _get_page(url)
  cycle_info = _extract_cycle_info(page)
  csv = _generate_csv(cycle_info)
  # print(csv)

main()