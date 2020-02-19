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

port_security_template = [
    'switchport port-security maximum 2',
    'switchport port-security violation restrict',
    'switchport port-security'
]

def generate_access_config(intf_vlan_mapping, access_template,psecurity=None):
    
    template = []
    for intf, vlan in intf_vlan_mapping.items():
        template.append('interface ' + intf)
        for line in access_mode_template:
            if line.endswith('access vlan'):
                template.append(f'{line} {vlan}')
            else:
                template.append(f'{line}')
        if psecurity:
            template.extend(psecurity)
                         
    print(template)
    
generate_access_config(access_config,access_mode_template,port_security_template)
