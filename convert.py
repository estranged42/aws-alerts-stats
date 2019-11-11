import os
import json
from pathlib import Path
import re

"""
This program will convert a pile of json files from the Slack channel output and create a single
json file with the information we want to examine parsed out.
"""

aws_alerts = []

def process_messages(message_list):
    global aws_alerts
    for m in message_list:
        if 'subtype' in m.keys() and m['subtype'] == 'channel_join':
            continue
        
        text = m['text']

        if '[RESOLVED]' not in text:
            continue

        p = re.compile('[A-Z]+-[A-Z]+-[1-9]')
        r = p.search(text)
        if r is not None:
            region = r.group(0)
        else:
            region = "None"

        p = re.compile('] (.*)>')
        r = p.search(text)
        if r is not None:
            service = r.group(1)
        else:
            service = ""

        timestamp = m['ts']

        event = {
            "service": service,
            "region": region,
            "ts": timestamp,
            "message": m['text']
        }

        aws_alerts.append(event)


data_dir = Path('data')
# Return a list of regular files only, not directories
file_list = [f for f in data_dir.glob('**/*.json') if f.is_file()]

limit = 3
count = 0
for fp in file_list:
    with open(fp, 'r') as f:
        slack_data = json.load(f)
        process_messages(slack_data)

    # count = count + 1
    if count >= limit:
        break

# print( json.dumps(aws_alerts, indent=2) )

region_counts = {}
for alert in aws_alerts:
    r = alert['region']
    if r in region_counts.keys():
        region_counts[r] = region_counts[r] + 1
    else:
        region_counts[r] = 1

sorted_r = sorted(region_counts.items(), key=lambda kv: kv[1])

#print( json.dumps(sorted_r, indent=2) )

for r in sorted_r:
    print(f"{r[0]:<20} {r[1]:<2}")