# PART 1

import csv

a = open('faculty.csv', 'r')
b = open('faculty2.csv', 'w')
ra = csv.DictReader(a)
wb = csv.DictWriter(b, None)

for d in ra:

  if wb.fieldnames is None:
    # initialize and write b's headers
    dh = dict((h, h) for h in ra.fieldnames)
    wb.fieldnames = ra.fieldnames
    wb.writerow(dh)

  wb.writerow(d)

b.close()
a.close()


# PART 2

import csv
reader = csv.reader(open('faculty.csv'))

result = {}
for row in reader:
    key = row[0]
    if key in result:
        # implement your duplicate row handling here
        pass
    result[key] = row[1:]

for key in sorted(result):
    print "%s: %s" % (key, result[key])

# PART 3

import csv
reader = csv.reader(open('faculty.csv'))

result = {}
for row in reader:
    key = row[0]
    if key in result:
        # implement your duplicate row handling here
        pass
    result[key] = row[1:]

for key in sorted(result):
    print "%s: %s" % (key, result[key])
