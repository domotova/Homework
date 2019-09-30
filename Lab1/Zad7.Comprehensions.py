# Predict the output of the following comprehensions. Does the output match what you expect?
print([x for x in [1, 2, 3, 4]])
print([n - 2 for n in range(10)])
print([k % 10 for k in range(41) if k % 3 == 0])
print([s.lower() for s in ['PythOn', 'iS', 'cOoL'] if s[0] < s[-1]])

# Something is fishy here. Can you spot it?
arr = [[3, 2, 1], ['a', 'b', 'c'], [('do',), ['re'], 'mi']]
print([el.append(el[0] * 4) for el in arr])  # What is printed?
print(arr)  # What is the content of `arr` at this point?

print([letter for letter in "pYthON" if letter.isupper()])
print({len(w) for w in ["its", "the", "remix", "to", "ignition"]})
