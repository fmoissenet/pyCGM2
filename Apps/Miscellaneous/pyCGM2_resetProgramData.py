# -*- coding: utf-8 -*-
import pyCGM2
import shutil
import traceback

def main():

    initFolder = pyCGM2.MAIN_PYCGM2_PATH+"pyCGM2\\Settings"
    appDataFolder = pyCGM2.PYCGM2_APPDATA_PATH[:-1]

    shutil.copytree(initFolder, appDataFolder)

if __name__ == "__main__":

    # ---- main script -----
    try:
        main()

    except Exception, errormsg:
        print "Error message: %s" % errormsg
        traceback.print_exc()
        print "Press return to exit.."
        raw_input()
