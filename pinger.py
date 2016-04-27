import os
import constants



def startping():

    global aaa
    global bbb
    global ccc
    global ddd

    aaa = 0
    bbb = 0
    ccc = 0
    ddd = 0

    response1 = os.system("ping -c 1 " + constants.hostname1)
    response2 = os.system("ping -c 1 " + constants.hostname2)
    response3 = os.system("ping -c 1 " + constants.hostname3)
    response4 = os.system("ping -c 1 " + constants.hostname4)

    if response1 ==0:
        aaa = 0
    else:
        aaa = 1

    if response2 ==0:
        bbb = 0
    else:
        bbb = 1

    if response3 ==0:
        ccc = 0
    else:
        ccc = 1

    if response4 ==0:
        ddd = 0
    else:
        ddd = 1
