d = {'a': 12, 'b': 20, 'c': 12, 'd': 40}
d1 = {}

for key, value in d.items():
  if value not in d1.values():
    d1[key] = value

print(d1)