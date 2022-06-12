import random

n = [0, 6, 3, 7, 4, 9, 1, 5, 2, 8]
l = ['h', 'r', 'b', 'u', 'd', 'q', 'o', 'l', 's', 'a', 'y', 'e', 'k', 'i', 'w', 'g', 'j', 'm', 'x', 'p', 'z', 'v', 'f', 't', 'b', 'n']
s = ['%', '-', '&', '$', ')', '!', '*', '@', '_', '(', '+', '#', '=']
random.shuffle(s)

h = ''
ix = 0
for i in range(0, 10): # i = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    ix += 1 # doesn't do anything
    x = random.randint(0, 25) # x =  3
    h = h + l[x] # h = '' + u
    y = random.randint(0, 9) # y = 4
    h = h + str(n[y]) # h = u + 4
    y = random.randint(0, 12) # y = 1
    h = h + s[y] # = u4-u4-u4-u4-u4-u4-u4-u4-u4-u4-

_h_all = h # u4-u4-u4-u4-u4-u4-u4-u4-u4-u4-


h = ''
for ij in range(0, 10):
    iy = 0
    x = random.randint(0, 25) # 1
    h = h + l[x] # rrrrrrrrrr
    jj = 0 # 

_h_l = h # rrrrrrrrrr
h = ''

 
for j in range(0, 10):
    iy += 2
    x = random.randint(0, 12)
    h = h + s[x] # %%%%%%%%%%
    jj += 2
    
_h_s = h  # %%%%%%%%%%
h = ''

print("Password with Letters, Numbers and Symbols: " +_h_all) # u4-u4-u4-u4-u4-u4-u4-u4-u4-u4-
print("Password with Letters: " +_h_l)  # rrrrrrrrrr
print("Password with Symbols: " +_h_s) # %%%%%%%%%%