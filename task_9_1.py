access_mode_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

access_config = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17
}

def generate_access_config(intf_vlan_mapping, access_template):
    template = []
    for intf, vlan in intf_vlan_mapping.items():
        template.append('interface ' + intf)
        for line in access_mode_template:
            if line.endswith('access vlan'):
                template.append('{} {}'.format(line, vlan)) 
            else:
                template.append('{}'.format(line))         
    print(template)
  
generate_access_config(access_config,access_mode_template)
