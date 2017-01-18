
from ciscoconfparse import CiscoConfParse

cisco_file = '/home/bwindle/pyclass/week1/config.txt'
    
cisco_cfg = CiscoConfParse(cisco_file)
crypto_maps = cisco_cfg.find_objects("^crypto map CRYPTO")

for c_map in crypto_maps:
    print
    print c_map.text
    for child in c_map.children:
        print child.text

print


