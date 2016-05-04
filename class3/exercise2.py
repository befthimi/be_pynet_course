#!/usr/bin/env python
"""
Script that graphs interface stats
"""
import time
import snmp_helper
import pygal

intfInOctets_fa4 = '1.3.6.1.2.1.2.2.1.10.5'
intfInUcastPkts_fa4 = '1.3.6.1.2.1.2.2.1.11.5'
intfOutOctets_fa4 = '1.3.6.1.2.1.2.2.1.16.5'
intfOutUcastPkts_fa4 = '1.3.6.1.2.1.2.2.1.17.5'
router1 = ('50.76.53.27', 7961)
a_user = 'pysnmp'
auth_key = 'galileo1'
encrypt_key = 'galileo1'
snmp_user = (a_user, auth_key, encrypt_key)

def snmp_get(whichrouter, which_oid):
    """
    Get snmp result based on which router and OID
    """
    snmp_data = snmp_helper.snmp_get_oid_v3(whichrouter, snmp_user, oid=which_oid)
    snmp_result = int(snmp_helper.snmp_extract(snmp_data))
    return snmp_result

def plotter(rawlist):
    """
    From rawlist calculate delta between each element in the list and
    return list of deltas in a new list.
    """
    newlist = [rawlist[i+1]-rawlist[i] for i in range(len(rawlist)-1)]
    return newlist

ListInOctets = []
ListOutOctets = []
ListInUcastP = []
ListOutUcastP = []

repeat = 13
print "Grabbing data. Please wait...\n"
while repeat > 0:
    ListInOctets.append(snmp_get(router1, intfInOctets_fa4))
    ListOutOctets.append(snmp_get(router1, intfOutOctets_fa4))
    ListInUcastP.append(snmp_get(router1, intfInUcastPkts_fa4))
    ListOutUcastP.append(snmp_get(router1, intfOutUcastPkts_fa4))
    time.sleep(300)
    repeat = repeat - 1

print "Finished grabbing data."
print "-" * 20
print "Creating graphs...."

PlotInOctets = plotter(ListInOctets)
PlotOutOctets = plotter(ListOutOctets)
PlotInUcastP = plotter(ListInUcastP)
PlotOutUcastP = plotter(ListOutUcastP)

#---------------------------------------------
# Create a Chart of type Line for byte count
byteline_chart = pygal.Line()

# Title
byteline_chart.title = 'Input/Output Bytes'

# X-axis labels (samples were every five minutes)
byteline_chart.x_labels = ['5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60']

# Add each one of the above lists into the graph as a line with corresponding label
byteline_chart.add('InBytes', PlotInOctets)
byteline_chart.add('OutBytes', PlotOutOctets)

# Create an output image file from this
byteline_chart.render_to_file('Bytes.svg')

#---------------------------------------------
# Create a Chart of type Line for packet count
pcktline_chart = pygal.Line()

# Title
pcktline_chart.title = 'Input/Output Packets'

# X-axis labels (samples were every five minutes)
pcktline_chart.x_labels = ['5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60']

# Add each one of the above lists into the graph as a line with corresponding label
pcktline_chart.add('In Unicast Packets', PlotInUcastP)
pcktline_chart.add('Out Unicast Packets', PlotOutOctets)

# Create an output image file from this
pcktline_chart.render_to_file('Pckts.svg')
