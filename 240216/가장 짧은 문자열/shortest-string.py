max_a = 0
a=input()

b=input()
c=input()
max_a = max(len(a),len(b),len(c))
min_a = min(len(a),len(b),len(c))

print(max_a-min_a)