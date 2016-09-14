# Paste your code into this box 
num = 0
for v in range(len(s)-2):
     num+=s.count('bob', v, v+3)
print('Number of times bob occurs is: '+str(num))
