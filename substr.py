str = input("Enter your string: ")
li = []
li_1 = []
li_2 = []
length = len(str)
max = 0

for i in range(length):
    for j in range(i + 1, length + 1):
        sub_str = '' + str[i:j]
        li.append(sub_str)
    
for k in li:
    for l in k:
        m = True
        if k.count(l) == 1:
            pass
        elif k.count(l) > 1:
            m = False
            break
    if m == True:
        li_1.append(k)
    else:
        continue
print('Substrings with no repeatation:', li_1)

for n in li_1:
    if n not in li_2:
        li_2.append(n)
    else:
        pass

for item in li_2:
    if len(item) > max:
        max = len(item)
        max_sub_str = item
    else:
        pass

print('longest substring with no repeatation: ', max_sub_str)
    
        
        
        
    
        