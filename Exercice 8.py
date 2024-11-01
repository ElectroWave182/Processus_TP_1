from time import *
import os

pids = os.listdir("/proc")

while True:

    meurtre = False
    for rep in pids:

        if rep.isdigit():
            fic = open("/proc/" + str(rep) + "/comm", "r")
            ps = fic.readline()

            if "xclock" in ps:
                os.kill(int(rep), 9)
                pids.remove(rep)
                meurtre = True
                break

            fic.close()

    if not(meurtre):
        print("ma mission est terminée")
        break

    sleep(1)

exit(0)
