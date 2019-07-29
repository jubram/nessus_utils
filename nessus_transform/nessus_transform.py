import os
import sys
import xml.etree.ElementTree as ET
from random import randint

def remove_report_items(report_hosts):

    for report_host in report_hosts:
        rh_size = len(report_host)
        for report_item in report_host.findall('ReportItem'):
            chance1 = randint(0, 3)
            chance2 = randint(0, 3)
            if chance1 == 1 or chance2 == 1:
                report_host.remove(report_item)

def remove_report_hosts(report):

    if len(report) > 1:
        for report_host in report.findall('ReportHost'):
            chance1 = randint(0, 2)
            chance2 = randint(0, 2)
            if chance1 == 1:
                report.remove(report_host)
            if len(report) < 2:
                break

def count_report_items(report_hosts):

    number_of_report_items = 0
    for report_host in report_hosts:
        number_of_report_items += len(report_host.findall('ReportItem'))
    
    return number_of_report_items

def main(filename=''):
    if not filename:
        filename = raw_input('Nome do arquivo nessus: ')

    tree = ET.parse(filename)
    root = tree.getroot()
    report = root.find('Report')
    original_report_hosts = len(report)
    original_report_items = count_report_items(report.findall('ReportHost'))

    remove_report_hosts(report)

    report_hosts = report.findall('ReportHost')

    remove_report_items(report_hosts)
    new_report_hosts = len(report)
    new_report_items = count_report_items(report.findall('ReportHost'))

    print '''
    |----------ORIGINAL FILE----------|
    |                                 |
    | Report Hosts: {}                |
    | Report Items: {}               |
    |                                 |
    |---------------------------------|
    '''.format(original_report_hosts, original_report_items)

    print '\n\n'

    print '''
    |-------------NEW FILE------------|
    |                                 |
    | Report Hosts: {}                |
    | Report Items: {}               |
    |                                 |
    |---------------------------------|
    '''.format(new_report_hosts, new_report_items)

    new_filename = raw_input('Nome do novo arquivo: ')

    tree.write(new_filename)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        main()
    elif len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print 'Uso: python nessys_transform.py [filename]'
        sys.exit()