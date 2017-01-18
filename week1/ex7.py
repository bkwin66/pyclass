#Brian windle

import yaml
import json
from pprint import pprint

def output_format(my_list, my_str):
    print '\n\n'
    print '#' * 3
    print '#' * 3 + my_str
    print '#' * 3
    pprint(my_list)

yaml_file = 'myyaml.yml'
json_file = 'myjson.json'


with open(yaml_file) as f:
    yaml_list = yaml.load(f)

with open(json_file) as f:
    json_list = json.load(f)

    output_format(yaml_list, ' YAML')
    output_format(json_list, ' JSON')
    print '\n'


