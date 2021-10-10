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
        if is_prime(i) == 0:
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
    subsecv_max = []
    for i in range(len(lista)):
        for j in range(i, len(lista) + 1):
            if (is_all_prime(lista[i:j])) and len(lista[i:j + 1]) > len(subsecv_max):
                subsecv_max = lista[i:j + 1]
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


def au_toate_div(l):
    '''
    Determina daca toate numerele din secventa au acelasi numar de divizori
    :param l:numere intregi
    :return: 1 daca numerele au acelasi numar de divizori si 0 in caz contrar
    '''

    for i in l - 1:
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
                subsecventa_max = l[i:j + 1]
    return subsecventa_max


def citire_lista():
    l = []
    n = int(input("Dati nr. de elemente: "))  # nr de elem
    for i in range(n):
        l.append(int(input("l[" + str(i) + "]=")))  # adauga elemente in lista
    return l  # returneaza lista


def print_menu():
    print("1. Citire lista")
    print("2. Afisare cea mai lunga secventa de numere prime")
    print("3. Afisare cea mai lunga secventa de numere care au acelasi numar de divizori")
    print("4. Iesire")


def main():
    test_is_all_prime()
    test_numar_de_divizori()
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
            break
        else:
            print("Optiune inexistenta! Reincercati.")


if __name__ == '__main__':
    main()
