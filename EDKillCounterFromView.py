from subprocess import Popen
import os
import sys

VERSION = "v0.0.0"

FOLDER_COUNT = "EDKillCounter"
FOLDER_VIEW = "EDKillCounterView"
FOLDER_DATA = ".\\data\\"

EXE_COUNT = "EDKillCounter.exe"
EXE_VIEW = "EDKillCounterView.exe"

FILE_SAVEPATH = ".\\savepath.txt"

def readFile(pPath):
    aOut = ""
    if os.path.exists(pPath) == True:
        with open(pPath, mode="r", encoding="utf-8") as aFNo:
            aOut = aFNo.read()
    return aOut

def getFolder(pFolder):
    aOut = ""
    for aDir in os.listdir(".."):
        if aDir.startswith(pFolder) == True:
            aOut = "..\\" + aDir + "\\"
            break

    return aOut

def main():
    print("version:" + VERSION + "\n")

    #フォルダがあるかの確認
    aPCount = getFolder(FOLDER_COUNT)
    if aPCount == "":
        print("error:" + FOLDER_COUNT + " not found")
        return 1
    if os.path.exists(aPCount + EXE_COUNT) != True:
        print("error:" + EXE_COUNT + " not found")
        return 1

    aPView = getFolder(FOLDER_VIEW)
    if aPCount == "":
        print("error:" + FOLDER_VIEW + " not found")
        return 1
    if os.path.exists(aPView + EXE_VIEW) != True:
        print("error:" + EXE_VIEW + " not found")
        return 1

    #キルカウンター起動
    print("start " + EXE_COUNT + "\n")
    popen = Popen(aPCount + EXE_COUNT, shell=True)
    try:
        popen.wait()
    except:
        pass
    print("end " + EXE_COUNT)

    #保存されているファイルのパスを取得後ファイル名に変換
    aSave = readFile(FILE_SAVEPATH)
    aSave = os.path.basename(aSave)
    print("data path:" + FOLDER_DATA + aSave)

    #ビュワーに保存パスを渡す
    print("start " + EXE_VIEW + "\n")
    popen = Popen(aPView + EXE_VIEW + " " + FOLDER_DATA + aSave, shell=True)
    try:
        popen.wait()
    except:
        pass
    print("end " + EXE_VIEW)

    return 0

if __name__ == "__main__":
    sys.exit(main())
