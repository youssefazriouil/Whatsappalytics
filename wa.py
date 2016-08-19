#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from helpers import *
from totalGroup import TotalGroup

def main():
#open het bestand die whatsapp geexporteerd heeft, die de naam 'Whatsapp chat_Nachtkast.txt' heeft
    try:
        nk = open(sys.argv[1])
    except:
        print 'Error, please input a whatsapp chat history file ($> python wa.py filename.txt)'
        exit()

    compiledPost = ""
    prevLine = ""
    groupMembers = {}
    totalGroup = TotalGroup()
    picModString = "heeft de groepsafbeelding gewijzigd"


    for line in nk:
        line = getCorrectedLine(line)
        if line and not picModString in line: #If line not empty and does not have the picModString
            oneCompletePost = getIfCompletePost(line)
            if not oneCompletePost: #line does not start with a datetime
                compiledPost = prevLine + " " + line #add the previous line to the current one
                prevLine = compiledPost
            else:
                if prevLine: #eerste iteratie is prevLine leeg
                    postObject = getPostObject(prevLine)
                    #update groupMembers dict
                    groupMembers = processPostForUser(postObject, groupMembers, totalGroup)

                prevLine = line
                compiledPost = ""

    #process the last line in the file
    groupMembers = processPostForUser(getPostObject(getCorrectedLine(line)), groupMembers, totalGroup)

    #toString het groupMembers-object
    for member in groupMembers:
        if groupMembers[member].getAveragePostLength():
            print groupMembers[member].getAllInfo()

    print totalGroup.getAllInfo()

if __name__ == "__main__":
    main()
