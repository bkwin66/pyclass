#Brian Windle
import yaml
import json

yaml_file = 'myyaml.yml'
json_file = 'myjson.json'


file = open('/home/bwindle/device', 'r')
device = list(file.read().split())


with open('/home/bwindle/detail', 'r') as document:
    detail = {}
    for line in document:
        x = line.split(",")
        a=x[0]
        b=x[1]
        c=len(b)-1
        b=b[0:c]
        detail[a]=b

device.append(detail)

with open(yaml_file, "w") as f:
    f.write(yaml.dump(device, default_flow_style=False))

with open(json_file, "w") as f:
    json.dump(device, f)



