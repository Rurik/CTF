map = """
   1 2 3 4 5 6 7 8 
A |_|_|_|_|_|_|_|_|
B |_|_|_|_|_|_|_|_|
C |_|_|_|_|_|_|_|_|
D |_|_|X|X|_|_|_|_|
E |_|X|_|_|X|_|_|_|
F |_|X|_|_|X|_|_|_|
G |_|X|_|_|X|_|_|_|
H |_|_|_|_|_|_|_|_|
"""

results = 'answers.append(('

for i in map.split('\n'):
    if 'X' in i:
        boxes = i.split('|')
        letter = boxes[0]
        for counter in range(len(boxes)):
            if 'X' in boxes[counter]:
                entry = '{}{}'.format(letter.strip(), counter)
                print(entry)
                results += '\'{}\', '.format(entry)
#print('answers.append({}))'.format(results))
print(results[0:len(results) - 2]+'))')