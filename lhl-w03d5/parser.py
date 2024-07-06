#!/usr/bin/python3

import sys
import re

LOG_LINE_RegEx = r'^(?P<IP>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*\[(?P<timestamp>.*)\]\s"(?P<verb>[A-Z]+)\s(?P<path>[\w\/]+)\s+(?P<protocol>[\w\/\.]+)"\s(?P<status_code>\d+)\s(?P<response_size>\d+).*'
pattern = re.compile(LOG_LINE_RegEx)
for line in sys.stdin:
  m = pattern.match(line)
  if m:
      print(m.groupdict())