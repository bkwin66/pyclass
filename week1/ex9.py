
from ciscoconfparse import CiscoConfParse

cisco_file = '/home/bwindle/pyclass/week1/config.txt'
    
cisco_cfg = CiscoConfParse(cisco_file)
crypto_maps = cisco_cfg.find_objects_w_child(parentspec=r'^crypto map CRYPTO', childspec=r'pfs group2')

print "Crypto Maps using PFS group2:"

for entry in crypto_maps:
    print "  {0}".format(entry.text)
print


