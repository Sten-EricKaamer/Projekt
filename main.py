# Rain Hans Kibena
# Sten-Eric Käämer
# Marti Laanesaar

from klass import *

def valikud():
    print("Tunni programm")
    print("1 - lisa aine teemad")
    print("2 - trüki aine teemad")
    print("3 - lisa õpilased klassi")
    print("4 - näita klassis olevaid õpilasi")
    print("5 - õpeta teema õpilastele")
    option = int(input("Vali sobilik tegevus: "))
    return option

def add_topic():
    topics = Andmed()
    while(True):
        topic = input("Sisesta teema: ")
        if(topic == ""):
            break
        topics.add_info(topic)
    return topics

def output_topics(lesson_topics):
    if(len(lesson_topics.info) == 0):
        print("Teemad pole sisestatud")
    else:
        print("Aine teemad on järgnevad:")
        for topic in lesson_topics:
            print("* " + topic)
        print("---")


def add_student():
    opilase_nimi = str(input("Sisesta õpilase nimi keda lisada klassi: "))
    opilane = Opilane(opilase_nimi)
    classroom.append(opilane)
    show_classroom()


def show_classroom():
    print("Klassi on lisatud hetkel järgnevad õpilased:")
    counter = 0
    for i in classroom:
        counter += 1
        print(counter, "- " + str(i.nimi))


def teach_topic():
    Opetaja.opetab(lesson_topics, classroom)



lesson_topics = []
classroom = []
while(True):
    option = valikud()
    if(option == 1):
        lesson_topics = add_topic()
    if(option == 2):
        output_topics(lesson_topics)
    if(option == 3):
        add_student()
    if(option == 4):
        klassisisu = show_classroom()
    if(option == 5):
        teach_topic()