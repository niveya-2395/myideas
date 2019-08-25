from __future__ import print_function
import sys
from os import system
import pyautogui
from time import sleep

def wordbuild():

    Wordlist = ['start','hello','games','book','drinks','animals','computer','newspaper',
                'execution','validation','congratulations','nurture','literature',
                'bathroom','dick','duck','cricket','prayers','fortune','price','money','zomato',
                'online','command','prompt','list','future','God','religion']

    conditions1(Wordlist)
################################################################################################################$###########################
def conditions1(Wordlist):

    user1 = Wordlist[0]
    copy = user1

    for x in range(2):
        print('\r', copy, end='')
        sleep(1.3)
        copy = ''

    user2 = raw_input('Your turn, please enter a word')

    if len(user2)==len(user1):
        print('Please enter your word followed by the earlier words shown')
        conditions1(Wordlist)

    elif user2[0:len(user1)] == user1:
        print('correct')

    else:
        print ('incorrect')
        aim = raw_input('Do you want to continue again Y/N?')
        if aim == 'Y':
            wordbuild()
        exit()

    conditions2(user2,Wordlist)
#########################################################################################################################$#######################
def conditions2(user2,Wordlist):

    mainuser2 = user2
    user1 = user2+Wordlist[1]
    copy = user1

    for x in range(2):
        print('\r', copy, end='')
        sleep(1.3)
        copy = ''


    user2 = raw_input('Your turn, please enter a word')

    if len(user2) == len(user1):
        print('Please enter your word followed by the earlier words shown')
        conditions2(mainuser2,Wordlist)

    elif user2[0:len(user1)] == user1:
        print('Well done !!! It\'s correct :)')

    else:
        print('Sorry, you were wrong :(')
        aim = raw_input('Do you want to continue again Y/N?')
        if aim == 'Y':
            wordbuild()
        exit()

    conditions3(user2,Wordlist)
#########################################################################################################################$#######################
def conditions3(user2,Wordlist):

    mainuser2 = user2
    user1 = user2+Wordlist[2]
    copy = user1

    for x in range(2):
        print('\r', copy, end='')
        sleep(1.3)
        copy = ''


    user2 = raw_input('Your turn, please enter a word')

    if len(user2) == len(user1):
        print('Please enter your word followed by the earlier words shown')
        conditions3(mainuser2,Wordlist)

    elif user2[0:len(user1)] == user1:
        print('Well done !!! It\'s correct :)')

    else:
        print('Sorry, you were wrong :(')
        aim = raw_input('Do you want to continue again Y/N?')
        if aim == 'Y':
            wordbuild()
        exit()

    conditions4(user2, Wordlist)
#########################################################################################################################$#######################
def conditions4(user2,Wordlist):

    mainuser2 = user2
    user1 = user2+Wordlist[3]
    copy = user1

    for x in range(2):
        print('\r', copy, end='')
        sleep(1.3)
        copy = ''


    user2 = raw_input('Your turn, please enter a word')

    if len(user2) == len(user1):
        print('Please enter your word followed by the earlier words shown')
        conditions4(mainuser2,Wordlist)

    elif user2[0:len(user1)] == user1:
        print('Well done !!! It\'s correct :)')

    else:
        print('Sorry, you were wrong :(')
        aim = raw_input('Do you want to continue again Y/N?')
        if aim == 'Y':
            wordbuild()
        exit()

    conditions5(user2,Wordlist)
#########################################################################################################################$##############st
def conditions5(user2,Wordlist):

    mainuser2 = user2
    user1 = user2+Wordlist[4]
    copy = user1

    for x in range(2):
        print('\r', copy, end='')
        sleep(1.3)
        copy = ''


    user2 = raw_input('Your turn, please enter a word')

    if len(user2) == len(user1):
        print('Please enter your word followed by the earlier words shown')
        conditions5(mainuser2,Wordlist)

    elif user2[0:len(user1)] == user1:
        print('Well done !!! It\'s correct :)')

    else:
        print('Sorry, you were wrong :(')
        aim = raw_input('Do you want to continue again Y/N?')
        if aim == 'Y':
            wordbuild()
        exit()

    conditions6(user2, Wordlist)
#########################################################################################################################$##############
def conditions6(user2,Wordlist):

    mainuser2 = user2
    user1 = user2+Wordlist[5]
    copy = user1

    for x in range(2):
        print('\r', copy, end='')
        sleep(1.3)
        copy = ''

    user2 = raw_input('Your turn, please enter a word')

    if len(user2) == len(user1):
        print('Please enter your word followed by the earlier words shown')
        conditions6(mainuser2,Wordlist)

    elif user2[0:len(user1)] == user1:
        print('Well done !!! It\'s correct :)')

    else:
        print('Sorry, you were wrong :(')
        aim = raw_input('Do you want to continue again Y/N?')
        if aim == 'Y':
            wordbuild()
        exit()

    conditions7(user2, Wordlist)
#########################################################################################################################$##############
def conditions7(user2,Wordlist):

    mainuser2 = user2
    user1 = user2+Wordlist[6]
    copy = user1

    for x in range(2):
        print('\r', copy, end='')
        sleep(1.3)
        copy = ''

    user2 = raw_input('Your turn, please enter a word')

    if len(user2) == len(user1):
        print('Please enter your word followed by the earlier words shown')
        conditions7(mainuser2,Wordlist)

    elif user2[0:len(user1)] == user1:
        print('Well done !!! It\'s correct :)')

    else:
        print('Sorry, you were wrong :(')
        aim = raw_input('Do you want to continue again Y/N?')
        if aim == 'Y':
            wordbuild()
        exit()

    conditions8(user2, Wordlist)
#########################################################################################################################$##############
def conditions8(user2,Wordlist):

    mainuser2 = user2
    user1 = user2+Wordlist[7]
    copy = user1

    for x in range(2):
        print('\r', copy, end='')
        sleep(1.3)
        copy = ''

    user2 = raw_input('Your turn, please enter a word')

    if len(user2) == len(user1):
        print('Please enter your word followed by the earlier words shown')
        conditions8(mainuser2,Wordlist)

    elif user2[0:len(user1)] == user1:
        print('Well done !!! It\'s correct :)')

    else:
        print('Sorry, you were wrong :(')
        aim = raw_input('Do you want to continue again Y/N?')
        if aim == 'Y':
            wordbuild()
        exit()
#########################################################################################################################$#############
def conditions8(user2,Wordlist):

    mainuser2 = user2
    user1 = user2+Wordlist[8]
    copy = user1

    for x in range(2):
        print('\r', copy, end='')
        sleep(1.3)
        copy = ''

    user2 = raw_input('Your turn, please enter a word')

    if len(user2) == len(user1):
        print('Please enter your word followed by the earlier words shown')
        conditions8(mainuser2,Wordlist)

    elif user2[0:len(user1)] == user1:
        print('Well done !!! It\'s correct :)')

    else:
        print('Sorry, you were wrong :(')
        aim = raw_input('Do you want to continue again Y/N?')
        if aim == 'Y':
            wordbuild()
        exit()

    conditions9(user2, Wordlist)
#########################################################################################################################$#############
def conditions9(user2,Wordlist):

    mainuser2 = user2
    user1 = user2+Wordlist[9]
    copy = user1

    for x in range(2):
        print('\r', copy, end='')
        sleep(1.3)
        copy = ''

    user2 = raw_input('Your turn, please enter a word')

    if len(user2) == len(user1):
        print('Please enter your word followed by the earlier words shown')
        conditions9(mainuser2, Wordlist)

    elif user2[0:len(user1)] == user1:
        print('Well done !!! It\'s correct :)')

    else:
        print('Sorry, you were wrong :(')
        aim = raw_input('Do you want to continue again Y/N?')
        if aim == 'Y':
            wordbuild()
        exit()

    conditions10(user2, Wordlist)
#########################################################################################################################$#############

def conditions10(user2,Wordlist):

    mainuser2 = user2
    user1 = user2+Wordlist[10]
    copy = user1

    for x in range(2):
        print('\r', copy, end='')
        sleep(1.3)
        copy = ''

    user2 = raw_input('Your turn, please enter a word')

    if len(user2) == len(user1):
        print('Please enter your word followed by the earlier words shown')
        conditions10(mainuser2, Wordlist)

    elif user2[0:len(user1)] == user1:
        print('Well done !!! It\'s correct :)')

    else:
        print('Sorry, you were wrong :(')
        aim = raw_input('Do you want to continue again Y/N?')
        if aim == 'Y':
            wordbuild()
        exit()

#########################################################################################################################$#############



wordbuild()








