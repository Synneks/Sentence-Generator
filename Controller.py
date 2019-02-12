class Controller_Substantive:
    substRepo = None

    def __init__(self, Subst_Repo):
        self.substRepo = Subst_Repo

    def read_file(self):
        return self.substRepo.read_file()

    def write_cuv(self, opt,ultima):
        self.substRepo.write_cuv(opt,ultima)

    def write_rap(self):
        self.substRepo.write_rap()

class Controller_Verbe:
    verbRepo = None

    def __init__(self, Verb_Repo):
        self.verbRepo = Verb_Repo

    def read_file(self):
        return self.verbRepo.read_file()

    def write_cuv(self, opt,ultima):
        self.verbRepo.write_cuv(opt,ultima)

    def write_rap(self):
        self.verbRepo.write_rap()

class Controller_Adjective:
    adjRepo = None

    def __init__(self, Adj_Repo):
        self.adjRepo = Adj_Repo

    def read_file(self):
        return self.adjRepo.read_file()

    def write_cuv(self, opt,ultima):
        self.adjRepo.write_cuv(opt,ultima)

    def write_rap(self):
        self.adjRepo.write_rap()