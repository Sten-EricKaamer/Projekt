# Rain Hans Kibena
# Sten-Eric Käämer
# Marti Laanesaar

from random import randint

class Andmed():


    def __init__(self, info=None):
        if(info is not None):# <------ |
            self.info = list(info)  # ------> |
        else:
            self.info = []

    def __getitem__(self, index):  # väga kasulik!!!
        return self.info[index]

    def add_info(self, info):
        self.info.append(info)

class Opilane():
    def __init__(self, nimi):
        self.nimi = nimi
        self.smarts = []

    def opib(self, teema):
        self.smarts.append(teema)

    def kirjeldus(self):
        print("Õpilase " + self.nimi + " teadmised on järgnevad:")
        for teema in self.smarts:
            print("* " + teema)


    def unutab(self):
        unusta = randint(0, len(self.smarts))
        self.smarts.remove(self.smarts[unusta])

class Opetaja():
    def __init__(self, nimi):
        self.nimi = nimi

    def opetab(self, teema, *opilased):
        for i in opilased:
            i.opib(teema)