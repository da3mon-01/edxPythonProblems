# Paste your code into this box 
longest=''
currstr=''
prev=''
for l in s:
     if l >= prev:
          currstr = currstr+l
          if len(currstr) > len(longest):
             longest = currstr
     else:
          currstr=l


     prev = l
print('Longest substring in alphabetical order is: ' + longest)
