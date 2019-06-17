import sys
import csv

fn = sys.argv[1]
print(fn)

res = 'var scores = {'
with open(fn, newline='') as csvfile:
    reader = csv.reader(csvfile)
    row = next(reader)
    SID_idx = row.index('SID')
    score_idx = row.index('Total Score')
    for row in reader:
        if row[score_idx] != '':
            res += '"%s" : "%s", ' % (row[SID_idx].upper(), row[score_idx])

res += '};'
print(res)
