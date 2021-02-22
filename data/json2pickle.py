#!/bin/python3

import glob
import pickle
import json

for e in glob.glob("*.json"):
    with open(e, 'r') as f, open(e.replace('json', 'pickle'), 'wb') as o:
        print(f"PICKLED -> {e}")
        j = json.load(f)
        pickle.dump(j, o)