from collections import defaultdict

d = defaultdict(lambda:0)

d['correct'] = 100
d['partially_correct'] = 200
d['WRONG'] # a default value of 0 gets assigned

print(d) 
