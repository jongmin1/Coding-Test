myDict = {'A':1, 'C':2, 'B':0}

print(myDict.get('A'))

print(myDict.get('A'))
print(myDict.get('C'))
print(myDict.get('C', 0))

print(myDict.items())
print(myDict.keys())
print(myDict.values())

print(sorted(myDict.items(), key=lambda x:x[1]))