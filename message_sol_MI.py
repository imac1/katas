
def sort_wizards_A_D(list):
    eligibles = []
    noneligibles = []
    for i, val in enumerate(list):
        for key, value in list[i].items():
            if key == 'name' and value.startswith('A'):
                eligibles.append(list[i])
            elif key == 'name' and value.startswith('D'):
                eligibles.append(list[i])
            else:
                noneligibles.append(list[i])
    return (f'eligibili {eligibles} \n neeligibili {noneligibles}')


def main():
    v = [{'name': 'Hagrid', 'level': 7, 'class': 'Demon Hunter', 'coins': 1220}, 
            {'name': 'Necrid', 'level': 5, 'class': 'Monk', 'coins': 204}, {'name': 'Akuma', 'level': 3, 'class': 'Wizard', 'coins': 2240}, 
            {'name': 'Fawful', 'level': 14, 'class': 'Demon Hunter', 'coins': 2100}, {'name': 'Gouken', 'level': 22, 'class': 'Wizard', 'coins': 20},
            {'name': 'Mokujin', 'level': 11, 'class': 'Monk', 'coins': 458}, {'name': 'Liu Kang', 'level': 15, 'class': 'Demon Hunter', 'coins': 354}, 
            {'name': 'Dhalsim', 'level': 107, 'class': 'Wizard', 'coins': 159}, {'name': 'Dracula', 'level': 75, 'class': 'Barbarian', 'coins': 147},
            {'name': 'Gouken', 'level': 54, 'class': 'Monk', 'coins': 12}, {'name': 'Claptrap', 'level': 23, 'class': 'Wizard', 'coins': 1}, 
            {'name': 'Blanka', 'level': 19, 'class': 'Demon Hunter', 'coins': 4572}, {'name': 'Balrog', 'level': 16, 'class': 'Barbarian', 'coins': 1245}]

    print(sort_wizards_A_D(v))


if __name__ == '__main__':
    main()