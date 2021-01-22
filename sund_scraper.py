import requests
import json
import csv
import logging
import time

logging.basicConfig(filename = 'sund_scraper.log',
                    filemode = 'a',
                    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level = logging.INFO)
logger = logging.getLogger(__name__)


def main():
    try:
        scraper()
    except Exception as e:
        logger.info(e)
    time.sleep(5)


def scraper():
    url = 'https://atlas.jifo.co/api/connectors/e85aa83c-5e92-4445-8898-6dc9f4598003'
    data = requests.get(url).json()
    time_of_last_update = data['refreshed']

    asvallalaug = data['data'][0][3][1]
    sudurbaejarlaug = data['data'][1][3][1]
    sundholl = data['data'][2][3][1]

    history_file = open('history.csv', 'r')
    last_line = history_file.readlines()[-1]
    last_file_entry = int(last_line.split(',')[0])
    history_file.close()

    if last_file_entry == time_of_last_update:
        return
    else:
        with open('history.csv', 'a', newline='') as history_file:
            history_writer = csv.writer(history_file, delimiter=',')
            history_writer.writerow([time_of_last_update,
                                    asvallalaug,
                                    sudurbaejarlaug,
                                    sundholl])

while True:
    main()
