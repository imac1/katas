from collections import defaultdict

v=[{'name': 'Hagrid', 'level': 7, 'class': 'Demon Hunter', 'coins': 1220}, 
{'name': 'Necrid', 'level': 5, 'class': 'Monk', 'coins': 204}, {'name': 'Akuma', 'level': 3, 'class': 'Wizard', 'coins': 2240}, 
{'name': 'Fawful', 'level': 14, 'class': 'Demon Hunter', 'coins': 2100}, {'name': 'Gouken', 'level': 22, 'class': 'Wizard', 'coins': 20},
{'name': 'Mokujin', 'level': 11, 'class': 'Monk', 'coins': 458}, {'name': 'Liu Kang', 'level': 15, 'class': 'Demon Hunter', 'coins': 354}, 
{'name': 'Dhalsim', 'level': 107, 'class': 'Wizard', 'coins': 159}, {'name': 'Dracula', 'level': 75, 'class': 'Barbarian', 'coins': 147},
{'name': 'Gouken', 'level': 54 , 'class': 'Monk', 'coins': 12}, {'name': 'Claptrap', 'level': 23, 'class': 'Wizard', 'coins': 1}, 
{'name': 'Blanka', 'level': 19, 'class': 'Demon Hunter', 'coins': 4572}, {'name': 'Balrog', 'level': 16, 'class': 'Barbarian', 'coins': 1245}]


nsw = 68
qwr = 'level'
ilt = 1

fr = {}
eligibili = []
neEligibili = []
	
if v[0]['name'][0] in [chr(nsw), chr(nsw+32)]: # chr(68) = D, chr(68 +32) = d - 
	# probabil ca vrea ca litera initiala a cuvantului sa fie D sau d
	if v[0][qwr] > ilt:
		eligibili.append(v[0]) # daca nivelul e > 1 sa adauge intr-o lista de eligibili
else:
	neEligibili.append(v[0])

if v[8]['name'][0] in [chr(nsw), chr(nsw+32)]:
	if v[8][qwr] > ilt:
		eligibili.append(v[8])
else:
	neEligibili.append(v[8])

if v[10]['name'][0] in [chr(nsw), chr(nsw+32)]:
	if v[10][qwr] > ilt:
		eligibili.append(v[10])
else:
	neEligibili.append(v[10])

if v[3]['name'][0] in [chr(nsw), chr(nsw+32)]:
	if v[3][qwr] > ilt:
		eligibili.append(v[3])
else:
	neEligibili.append(v[3])

if v[9]['name'][0] in [chr(nsw), chr(nsw+32)]:
	if v[9][qwr] > ilt:
		eligibili.append(v[9])
else:
	neEligibili.append(v[9])

if v[1]['name'][0] in [chr(nsw), chr(nsw+32)]:
	if v[1][qwr] > ilt:
		eligibili.append(v[1])
else:
	neEligibili.append(v[9])
	
if v[5]['name'][0] in [chr(nsw), chr(nsw+32)]:
	if v[5][qwr] > ilt:
		eligibili.append(v[5])
else:
	neEligibili.append(v[5])

if v[2]['name'][0] in [chr(nsw), chr(nsw+32)]:
	if v[2][qwr] > ilt:
		eligibili.append(v[2])
else:
	neEligibili.append(v[2])

if v[6]['name'][0] in [chr(nsw), chr(nsw+32)]:
	if v[6][qwr] > ilt:
		eligibili.append(v[6])
else:
	neEligibili.append(v[6])

if v[4]['name'][0] in [chr(nsw), chr(nsw+32)]:
	if v[4][qwr] > ilt:
		eligibili.append(v[4])
else:
	neEligibili.append(v[4])

if v[7]['name'][0] in [chr(nsw), chr(nsw+32)]:
	if v[7][qwr] > ilt:
		eligibili.append(v[7])
else:
	neEligibili.append(v[7])

if v[11]['name'][0] in [chr(nsw), chr(nsw+32)]:
	if v[11][qwr] > ilt:
		eligibili.append(v[11])
else:
	neEligibili.append(v[11])

if v[12]['name'][0] in [chr(nsw), chr(nsw+32)]:
	if v[12][qwr] > ilt:
		eligibili.append(v[12])
else:
	neEligibili.append(v[12])

fr['good'] = eligibili # adauga intr-o cheie 'good' de dictionar lista de eligibili daca nivelul e mai mare de 1
fr['bad'] = neEligibili

print(f'eligibili sau neeligibili good {eligibili}')  # printeaza doar userii care incep cu D si au un nivel > 1
print(f'eligibili sau neeligibili bad {neEligibili}') 

nsw = 65
qwr = 'coins'
ilt = 150

vr = {}
gfu = []
unelg = []
# sorteaza alfabetic in eligibili si neeligibili userii cu nr de monede > 150 care incep cu litera A sau a
	
if v[0]['name'][0] in [chr(nsw), chr(nsw+32)]:
	if v[0][qwr] > ilt: 
		gfu.append(v[0])
else:
	unelg.append(v[0])

if v[8]['name'][0] in [chr(nsw), chr(nsw+32)]:
	if v[8][qwr] > ilt:
		gfu.append(v[8])
else:
	unelg.append(v[8])

if v[10]['name'][0] in [chr(nsw), chr(nsw+32)]:
	if v[10][qwr] > ilt:
		gfu.append(v[10])
else:
	unelg.append(v[10])

if v[3]['name'][0] in [chr(nsw), chr(nsw+32)]:
	if v[3][qwr] > ilt:
		gfu.append(v[3])
else:
	unelg.append(v[3])

if v[9]['name'][0] in [chr(nsw), chr(nsw+32)]:
	if v[9][qwr] > ilt:
		gfu.append(v[9])
else:
	unelg.append(v[9])

if v[5]['name'][0] in [chr(nsw), chr(nsw+32)]:
	if v[5][qwr] > ilt:
		gfu.append(v[5])
else:
	unelg.append(v[5])

if v[2]['name'][0] in [chr(nsw), chr(nsw+32)]:
	if v[2][qwr] > ilt:
		gfu.append(v[2])
else:
	unelg.append(v[2])

if v[6]['name'][0] in [chr(nsw), chr(nsw+32)]:
	if v[6][qwr] > ilt:
		gfu.append(v[6])
else:
	unelg.append(v[6])

if v[1]['name'][0] in [chr(nsw), chr(nsw+32)]:
	if v[1][qwr] > ilt:
		gfu.append(v[1])
else:
	unelg.append(v[1])
	
if v[4]['name'][0] in [chr(nsw), chr(nsw+32)]:
	if v[4][qwr] > ilt:
		gfu.append(v[4])
else:
	unelg.append(v[4])

if v[7]['name'][0] in [chr(nsw), chr(nsw+32)]:
	if v[7][qwr] > ilt:
		gfu.append(v[7])
else:
	unelg.append(v[7])

if v[11]['name'][0] in [chr(nsw), chr(nsw+32)]:
	if v[11][qwr] > ilt:
		gfu.append(v[11])
else:
	unelg.append(v[11])

if v[12]['name'][0] in [chr(nsw), chr(nsw+32)]:
	if v[12][qwr] > ilt:
		gfu.append(v[12])
else:
	unelg.append(v[12])

vr['good'] = gfu
vr['bad'] = unelg

print(F'nu stiu ce e asta  good{gfu}')
print(F'nu stiu ce e asta bad {unelg}')

'''
trebuie sa sorteze lista a. i. sa cuprinda toti itemii care incep cu litera A sau D
'''



