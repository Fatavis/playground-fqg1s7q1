import random
import builtins
import time
import os

anc_input = builtins.input
anc_randint = random.randint

échec = True

entrées = []


def nouv_random(a, b):
    global entrées
    entrées = [anc_randint(a, b) for i in range(100)]

    return str(entrées[-1])


random.randint = nouv_random


def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")


def nouv_input(*params):
    global échec

    if len(params) == 0:
        échec = True

    elif len(params) > 1:
        échec = True

    elif len(params) > 0:
        print(params[0], end="")

    entrée = str(entrées.pop())
    print(entrée)

    return entrée


def nouv_print(*params):
    global échec
    if len(params) == 1 and params[0] == "C'est la bonne combinaison!":
        success()
        send_msg(
            "Bravo!", "Le coffre s'ouvre lorsqu'on entre la bonne combinaison")
        échec = False

        anc_print(*params)


builtins.input = nouv_input

try:
    import coffre6

    if échec:
        fail()

    else:
        success()

except Exception as e:
    fail()
    échec = True
    send_msg("Pas tout à fait",
             'Quelque chose ne va pas. Avez-vous bien placé la condition «entrée == combinaison» après le mot «if» ? ')
    send_msg("Erreur", e)