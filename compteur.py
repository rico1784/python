

def is_number(to_test):
    if to_test >= '0' and to_test <= '9':
        return True
    else:
        return False

for char in "Hello W0rld 1":
        if is_number(char) == True:
            print('C\'est un chiffre')
        else:
            print('Ce n\'est pas un chiffre')

