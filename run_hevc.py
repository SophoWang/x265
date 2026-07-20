#!/bin/env python

import json
import re
import os

vscode_launch = ".vscode/launch.json"
json_str = ""

with open(vscode_launch, "r") as fd:
    lines = fd.readlines()
				# data = json.load(fd)
				for line in lines:
								line = re.sub(r'//.*', "", line)
								json_str = json_str + line

print(json_str)

data = json.loads(json_str)

args = data['configurations'][0]['args']
run_args = ""
run_cmd = "./build/x265"

for arg in args:
				run_args = run_args + " " + arg

print(run_cmd + run_args)
os.system(run_cmd + run_args)