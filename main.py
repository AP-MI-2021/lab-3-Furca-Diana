def is_prime(n):
    '''
    Determina daca un numar este prim sau nu
    :param n: numar intreg
    :return: 1 daca numarul este prim, 0 in caz contrar
    '''
    if n < 2:
        return 0  # 0 si 1 nu sunt numere prime
    elif n == 2:
        return 1  # 2 este numar prim
    elif n % 2 == 0:
        return 0  # singurul numar prim par este 2, alte numere pare nu sunt prime
    else:
        for i in range(3, n // 2 + 1):
            if n % i == 0:
                return 0  # un numar prim nu are divizori
        return 1  # daca numarul nu are niciun divizor propriu, inseamna ca e prim


def is_all_prime(lista):
    '''
    Determina daca toate numerele primite sunt prime sau nu
    :return: True sau False in functie de caz
    '''
    for i in lista:
        if is_prime(i) == 0: #daca gasesc un numar care nu e prim, nu e bine, se returneaza False
            return False

    return True


def test_is_all_prime():
    assert is_all_prime([2, 5, 7, 19]) is True
    assert is_all_prime([3, 5, 7, 10]) is False
    assert is_all_prime([11, 13, 17, 19, 23]) is True
    assert is_all_prime([23, 45, 67, 88, 124]) is False


def get_longest_all_primes(lista):
    '''
    Determina cea mai lunga subsecventa de numere prime
    :return: subsecventa maxima, in cazul in care aceasta exista
    '''
    subsecv_max = [] # lista goala
    for i in range(len(lista)):
        for j in range(i, len(lista) + 1):  #se parcurg toate elementele listei
            if (is_all_prime(lista[i:j])) and len(lista[i:j + 1]) > len(subsecv_max):
                subsecv_max = lista[i:j + 1]  # se verifica daca in subsecventa toate numerele sunt prime si daca lungimea secventei gasite e una maxima
    return subsecv_max


def numar_de_divizori(n):
    '''
    Determina numarul de divizori, propri si impropri, ai unui numar dat
    :param n: numar intreg
    :return: numarul de divizori gasiti
    '''
    numar_div = 0
    i = 1
    while i <= n:
        if n % i == 0:
            numar_div = numar_div + 1  # daca se gaseste un divizor, variabila ce contorizeaza creste cu 1
        i = i + 1

    return numar_div


def test_numar_de_divizori():
    assert numar_de_divizori(17) == 2
    assert numar_de_divizori(15) == 4
    assert numar_de_divizori(10) == 4
    assert numar_de_divizori(6) == 4


def au_toate_div(l):
    '''
    Determina daca toate numerele din secventa au acelasi numar de divizori
    :param l:numere intregi
    :return: 1 daca numerele au acelasi numar de divizori si 0 in caz contrar
    '''

    for i in l :
        if numar_de_divizori(i) != numar_de_divizori(
                i + 1):  # verific perechi de cate 2 numere alaturate daca au acelasi nr de divizori
            return 0
        return 1


def get_longest_same_div_count(l):
    '''
    Determina cea mai lunga secventa de numere care au acelasi numar de divizori
    :param l: numere intregi
    :return: cea mai lunga secventa cu proprietatea ceruta, in cazul in care aceasta exista
    '''
    subsecventa_max = []
    for i in range(len(l)):
        for j in range(i, len(l) + 1):
            if (au_toate_div(l[i:j + 1])) and len(l[i:j + 1]) > len(subsecventa_max):
                subsecventa_max = l[i:j + 1]  #verific daca in subsecventa toate elem au acelasi numar de divizori sau nu
    return subsecventa_max


def e_par(n):
    '''
    Determina daca un numar este par sau nu
    :param n: numar natural
    :return: 1 daca numarul este par, 0 in caz contrar
    '''
    if n%2==0:
        return 1
    return 0

def toate_sunt_pare(lista):
    '''
    Determina daca toate numerele primite sunt pare sau nu
    :return: True sau False in functie de caz
    '''
    for i in lista:
        if e_par(i) == 0: # daca se gaseste in sirul de numere unul impar,nu e bine, se returneaza False
            return False

    return True

def test_toate_sunt_pare():
    assert toate_sunt_pare([2, 54, 72, 190]) is True
    assert toate_sunt_pare([3, 5, 7, 10]) is False
    assert toate_sunt_pare([116, 18, 12, 190, 236]) is True
    assert toate_sunt_pare([23, 45, 67, 87, 124]) is False


def get_longest_all_even(lista):
    '''
    Determina cea mai lunga subsecventa de numere pare din lista
    :return: subsecventa maxima, in cazul in care aceasta exista
    '''
    subsecv_max = [] #declar o lista goala
    for i in range(len(lista)):  #parcurg elementele listei
        for j in range(i, len(lista) + 1):
            if (toate_sunt_pare(lista[i:j])) and len(lista[i:j + 1]) > len(subsecv_max):
                #verific daca in subsecventa toate elementele sunt pare sau nu, compar lungimile secventelor
                subsecv_max = lista[i:j + 1]   #daca gasesc o subsecventa mai lunga decat cea curenta, o retin
    return subsecv_max


def citire_lista():
    l = []
    n = int(input("Dati nr. de elemente: "))  # nr de elemente
    for i in range(n):
        l.append(int(input("l[" + str(i) + "]=")))  # adauga elemente in lista
    return l  # returneaza lista


def print_menu():
    print("1. Citire lista")
    print("2. Afisare cea mai lunga secventa de numere prime")
    print("3. Afisare cea mai lunga secventa de numere care au acelasi numar de divizori")
    print("4. Afisare cea mai lunga secventa de numere care sunt pare")
    print("5. Iesire")


def main():
    test_is_all_prime()
    test_numar_de_divizori()
    test_toate_sunt_pare()
    l = []
    while True:
        print_menu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            l = citire_lista()
        elif optiune == "2":
            print(get_longest_all_primes(l))
        elif optiune == "3":
            print(get_longest_same_div_count(l))
        elif optiune == "4":
            print(get_longest_all_even(l))
        elif optiune == "5":
            break
        else:
            print("Optiune inexistenta! Reincercati.")


if __name__ == '__main__':
    main()
