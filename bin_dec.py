dec = input("Enter the decimal number: ")
if '.' in dec:
    d = dec.split('.')
    dec_int = int(d[0])
    dec_float = float('0.'+ d[1])
else:
    dec_int = int(dec)
    dec_float = 0

x = dec_int
z = dec_float
b = ''
c = ''
i = 0
#print(d)
#print(dec_int)
#print(dec_float)
while True:
    if x != 0:
        x = int(dec_int/2)
        y = dec_int % 2    
    elif x == 0:
        y = x
        break    
    b = b + str(y)
    dec_int = x
while i < 10:
    if dec_float != 0:
        z = (dec_float*2)%1
        w = int(dec_float*2)
    elif dec_float == 0:
        break
    c = c + str(w)
    dec_float = z
          
p_1 = (''.join(reversed(b)))   
print(p_1 +'.'+ c)

        
        
        
    
    
