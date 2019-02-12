from substantiv import Substantiv
from adjectiv import Adjectiv
from verb import Verb

w = open('propozitii.txt', 'w') #deschid fisierul cu propozitia cu comanda write
r = open('Raport.txt', 'w') #deschid fisierul cu raporturi

class Subst_Repo:
    lista_substantive = [Substantiv]

    def __init__(self):
        self.lista_substantive = []
        self.lista_substantive_poz = []

    def read_file(self):
        f = open('substantive.txt', 'r')
        for line in f:
            line.strip('\n')
            self.lista_substantive.append(line)
            self.lista_substantive_poz.append(0)
        return self.lista_substantive

    def write_cuv(self, opt,ultima):
        if ultima == 0:
            w.write(self.lista_substantive[opt][:-1] + ' ') #afisez pana la penultimul caracter ca sa nu puna \n
        else:
            w.write(self.lista_substantive[opt][:-1] + '\n')
        self.lista_substantive_poz[opt] += 1

    def write_rap(self):
        for i in range (len(self.lista_substantive_poz)):
            if self.lista_substantive_poz[i] > 0:
                r.write(self.lista_substantive[i][:-1] + ' - ') #afisez pana la penultimul caracter ca sa nu puna \n
                r.write(str(self.lista_substantive_poz[i]) + ' aparitii - ')
                r.write('substantiv \n')

class Verb_Repo:
    lista_verbe = [Verb]

    def __init__(self):
        self.lista_verbe = []
        self.lista_verbe_poz = []

    def read_file(self):
        f = open('verbe.txt', 'r')
        for line in f:
            self.lista_verbe.append(line)
            self.lista_verbe_poz.append(0)
        return self.lista_verbe

    def write_cuv(self, opt,ultima):
        if ultima == 0:
            w.write(self.lista_verbe[opt][:-1] + ' ')   #afisez pana la penultimul caracter ca sa nu puna \n
        else:
            w.write(self.lista_verbe[opt][:-1] + '\n')
        self.lista_verbe_poz[opt] += 1

    def write_rap(self):
        for i in range (len(self.lista_verbe_poz)):
            if self.lista_verbe_poz[i] > 0:
                r.write(self.lista_verbe[i][:-1] + ' - ')   #afisez pana la penultimul caracter ca sa nu puna \n
                r.write(str(self.lista_verbe_poz[i]) + ' aparitii - ')
                r.write(' verb \n')

class Adj_Repo:
    lista_adjective = [Adjectiv]

    def __init__(self):
        self.lista_adjective = []
        self.lista_adjective_poz = []

    def read_file(self):
        f = open('adjective.txt', 'r')
        for line in f:
            self.lista_adjective.append(line)
            self.lista_adjective_poz.append(0)
        return self.lista_adjective

    def write_cuv(self, opt,ultima):
        if ultima == 0:
            w.write(self.lista_adjective[opt][:-1] + ' ')   #afisez pana la penultimul caracter ca sa nu puna \n
        else:
            w.write(self.lista_adjective[opt][:-1] + '\n')
        self.lista_adjective_poz[opt] += 1

    def write_rap(self):
        for i in range (len(self.lista_adjective_poz)):
            if self.lista_adjective_poz[i] > 0:
                r.write(self.lista_adjective[i][:-1] + ' - ')   #afisez pana la penultimul caracter ca sa nu puna \n
                r.write(str(self.lista_adjective_poz[i]) + ' aparitii - ')
                r.write(' adjectiv \n')

""""Teste"""
def test_read_subst():
    test = Subst_Repo()
    subst_test = test.read_file()
    assert len(subst_test) == 20
    print('Citirea functioneaza la subst')

test_read_subst()

def test_read_verbe():
    test = Verb_Repo()
    verbe_test = test.read_file()
    assert len(verbe_test) == 20
    print('Citirea functioneaza la verbe')

test_read_verbe()

def test_read_adj():
    test = Adj_Repo()
    adj_test = test.read_file()
    assert len(adj_test) == 20
    print('Citirea functioneaza la adj')

test_read_adj()