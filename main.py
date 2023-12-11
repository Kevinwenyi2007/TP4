# Question 1
import random

class NPC:
    def __init__(self):
        self.force = rouler_des()
        self.agilite = rouler_des()
        self.constitution = rouler_des()
        self.intelligence = rouler_des()
        self.sagesse = rouler_des()
        self.charisme = rouler_des()
        self.armure = random.randint(1,12)
        self.nom = None
        self.race = None
        self.espece = None
        self.point_de_vie = 20
        self.profession = None

def rouler_des():

    de1 = random.randint(1,6)
    de2 = random.randint(1,6)
    de3 = random.randint(1,6)
    de4 = random.randint(1,6)
    if de1<de2 and de1<de3 and de1<de4:
        return de2+de3+de4
    elif de2<de3 and de2<de4:
        return de3+de4+de1
    elif de3<de4:
        return de1+de2+de4
    else:
        return de1+de2+de3

class kobold(NPC):
    def attaquer(self):
        pass
    def subir_dommage(self):
        pass

class hero(NPC):
    def attaquer(self):
        pass
    def subir_dommage(self):
        pass








