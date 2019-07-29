import os
import sys
import xml.etree.ElementTree as ET
import copy
import ipaddress

def create_file(tree, hosts, filename, part):
	root = tree.getroot()
	policy = root.find('Policy')
	preferences = policy.find('Preferences').find('ServerPreferences').findall('preference')
	for preference in preferences:
		children = list(preference)
		if children[0].text == 'TARGET':
			children[1].text = ', '.join(hosts)
	report = root.find('Report')
	for report_host in report.findall('ReportHost'):
		name = report_host.get('name')
		if name not in hosts:
			report.remove(report_host)
	
	tree.write(f'{filename}_part{part}.nessus')

	return True

def parse_file(filename=''):
	if not filename:
		filename = input('Nome do arquivo nessus: ')
	
	tree = ET.parse(filename)
	root = tree.getroot()
	policy = root.find('Policy')
	preferences = policy.find('Preferences').find('ServerPreferences').findall('preference')
	for preference in preferences:
		children = list(preference)
		if children[0].text == 'TARGET':
			pref = preference
			hosts = children[1].text.split(',')
			break

	for host in hosts:
		if '/' in host:
			range = ipaddress.ip_network(host)
			hosts.remove(host)
			hosts.extend(map(str, range.hosts()))
	
	hosts = set(hosts)
	hosts = list(hosts)

	return tree, hosts, filename.split('.')[0]



if __name__ == "__main__":
	if(len(sys.argv) == 1):
		tree, hosts, filename = parse_file()
	elif(len(sys.argv) == 2):
		tree, hosts, filename = parse_file(sys.argv[1])
	else:
		print("Uso: nessus_split.py [filename]")
		sys.exit()
	
	i = 0
	while hosts:
		new_tree = copy.deepcopy(tree)
		print(f'Hosts left: {len(hosts)}')
		h = list()
		for _ in range(50):
			try:
				h.append(hosts.pop(0))
			except:
				break
		create_file(new_tree, h, filename, i)
		i += 1