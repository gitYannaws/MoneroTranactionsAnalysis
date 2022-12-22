import urllib.request as request
import json
from datetime import datetime
from time import sleep
import csv

##http://141.164.59.251/monero.html#block-information
rows = []
blockInDay = 720*31 ##720

with request.urlopen('https://localmonero.co/blocks/api/get_stats') as response:
    source = response.read()
    data = json.loads(source)
    currentHeight = data['height']


height = currentHeight-blockInDay


for x in range(blockInDay):
    print(x)
    with request.urlopen(f'https://localmonero.co/blocks/api/get_block_data/{height+x}') as response:
        data = json.loads(response.read())
        dataTxt = data['block_data']['result']['block_header']['num_txes']
        dataTimestamp = data['block_data']['result']['block_header']['timestamp']
        blockNum = height+x
        rows.append({'num_txes': dataTxt, 'block': blockNum, 'datetime': datetime.fromtimestamp(dataTimestamp).strftime('%m/%d/%y %H:%M:%S')})  ##%H-%d-%m-%y
        print(rows)
        sleep(0.5)


with open('moneroDataV2.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['num_txes', 'block', 'datetime'])
    writer.writeheader()
    writer.writerows(rows)

print(rows)



