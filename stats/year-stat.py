"""
Provide the year wise stats.
"""

import json

yr = raw_input("Enter the year( 2009-2014 ):")
count = 0
projc = 0

organ = {}


# Load all data from json files to a list of dicts
with open("../data/org/"+yr+".json") as inp:
    data = json.load(inp)

# First calculate the no. of orgs that got selected for the year = yr.

    for org in data['orgs']:
        count = count + 1


# Calculate the total no. of projects for that yr.

with open("../data/projects/"+yr+".json") as inpu:
    data = json.load(inpu)

    for proj in data['projects']:
        projc = projc + 1

# Gives wrong results for the year 2014. :/

# Org that bagged maximum number of projects.

    for project in data['projects']:
        orgname = project['organization']

        if orgname in organ:
            organ[orgname].append(yr)
        else:
            organ[orgname] = [yr]

seniors = {s: organ[s] for s in organ if len(organ[s]) > 2}

orgs_sorted = sorted(seniors.items(), key=lambda x: len(x[1]), reverse=True)

for s in orgs_sorted:
    break

# GIves wrong result for 2014. :/

print ''
print 'YEAR:', yr   # Year
print 'No. of orgs that got selected:', count   # NO. of orgs
print 'Total No. of projects that got selected:', projc   # Total no. of projects.
print 'The org. that got maximum slots is %s with %d slots' % (s[0], len(s[1]))  # Maximum slots
