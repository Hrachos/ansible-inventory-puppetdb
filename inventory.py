#!/usr/bin/env python

from pypuppetdb import connect
import json

try:
  db = connect(host='puppetdb.example.com')
  hosts = {}
  facts = db.facts('environment')

  for fact in facts:
    hostname_str = str(fact)
    hostname = hostname_str[12:]
    env = str(fact.value)

    if env in hosts:
            new_list = hosts[env]
    else:
            new_list = []

    new_list.append(hostname)
    hosts[env] = new_list

  print (json.dumps(hosts, indent=2))
except:
  print ("{}")
