from Repository import *
from Controller import*
from random import *

subst_repo = Subst_Repo()
subst_control = Controller_Substantive(subst_repo)
substantive = subst_control.read_file()

verb_repo = Verb_Repo()
verb_control = Controller_Verbe(verb_repo)
verbe = verb_control.read_file()

adj_repo = Adj_Repo()
adj_control = Controller_Adjective(adj_repo)
adjective = adj_control.read_file()

w = open('propozitii.txt', 'w') #deschid fisierul cu propozitia cu comanda write

while 1:
    n = input("Introduceti numarul de propozitii: ")
    try:
        n = int(n)
        while n < 0:
            n = input("Nu este pozitiv.\nIntroduceti numarul de propozitii: ")
            n = int(n)
        break
    except ValueError:
        print('Nu este numar intreg.')
n = int(n)

def main(n,subst_control,verb_control,adj_control):
    '''
    Meniul are patru optiuni numerotate de la 1 la 4. Daca optiunea aleasa
    nu exista se va afisa un mesaj de eroare si se va introduce o noua optiune
    pana la alegerea optiunii 4
    '''

    print('1. Scriere a n propozitii')
    print('2. Topica corecta')
    print('3. Procent')
    print('4. Raport')
    print('5. Exit')
    print(' ')

    opt = input('Alegeti o optiune: ')
    while opt < '1' or opt > '5':
        print('Optiunea aleasa nu exista\n')
        opt = input('Alegeti o optiune: ')

    procent = 0
    topica = 0

    while '5':
        if opt == '1':

            # pentru a fi mai usor selectez pentru fiecare fel de cuvant un numar
            # 1 - subst
            # 2 - verb
            # 3 - adj

            for i in range(n):
                nr_cuvinte = randint(0, 3)  # obtin aleatoriu lungimea propozitiei
                ordine = [1, 2, 3]  # stiind faptul ca o propozitie trebuie sa aiba minim un S un V si un A le adaug manual
                for j in range(nr_cuvinte):  # adaug la ordine numarul de cuvinte din nr_cuvinte
                    ordine.append(randint(1, 3))
                shuffle(ordine)  # le reordonez aleatoriu

                # stiind deja ordinea pe care o sa o aiba propozitia pot sa calculez
                # procentul si nr de prop cu topica corecta
                #print(ordine)
                if ordine[0] == 2 and ordine[1] == 1 and ordine[2] == 3 and len(ordine) == 3:  # verific daca o propozitie are structura corecta si o numar
                    procent += 1

                if len(ordine) == 4:  # verific daca o propozitie are topica S V S A. Prima data trebuie sa aiba lungimea 4
                    if ordine[0] == 1 and ordine[1] == 2 and ordine[2] == 1 and ordine[3] == 3:  # apoi sa fie in ordine
                        topica += 1  # daca gasesc o propozitie cu topica corecta o numar

                prop = []
                for nr in range(len(ordine)):
                    ultima = 0
                    if nr == len(ordine)-1:
                        ultima = 1
                    if ordine[nr] == 1:  # daca element de pe pozitia nr este substantiv, aleg aleatoriu al catelea substantiv sa il scriu
                        opt = randint(0, len(substantive) - 1)
                        subst_control.write_cuv(opt,ultima)
                        prop.append(substantive[opt])  # adaug la prop pentru a putea afisa propozitia

                    elif ordine[nr] == 2:  # daca elementul de pe pozitia nr este verb, aleg aleatoriu al catelea verb sa il scriu
                        opt = randint(0, len(verbe) - 1)
                        prop.append(verbe[opt])  # adaug la prop pentru a putea afisa propozitia
                        verb_control.write_cuv(opt,ultima)  # incerementez pozitia pe care se afla cuvantul folosit

                    elif ordine[nr] == 3:  # daca elementul de pe pozitia nr este adjectiv, aleg aleatoriu al catelea adjecti sa il scriu
                        opt = randint(0, len(adjective) - 1)
                        prop.append(adjective[opt])  # adaug la prop pentru a putea afisa propozitia
                        adj_control.write_cuv(opt,ultima)  # incerementez pozitia pe care se afla cuvantul folosit

                print(prop)

        if opt == '2':
            print(topica, 'propozitii au topica corecta.')

        if opt == '3':
            print('Procentul de propozitii cu forma V S A este: ', procent / n * 100, '%.')

        if opt == '4':
            subst_control.write_rap()
            verb_control.write_rap()
            adj_control.write_rap()
            print('Raportul a fost efectuat.')

        if opt == '5':
            break

        opt = input('\nAlegeti o optiune: ')
        while opt < '1' or opt > '5':
            print('Optiunea aleasa nu exista\n')
            opt = input('Alegeti o optiune: ')

print(' ')
main(n,subst_control,verb_control,adj_control)