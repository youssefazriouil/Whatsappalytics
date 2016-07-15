#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from helpers import *

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
                    groupMembers = processPostForUser(postObject, groupMembers)

                prevLine = line
                compiledPost = ""

    print getCorrectedLine(line) #print the last line in the file
    for member in groupMembers:
        if groupMembers[member].getAveragePostLength():
            print groupMembers[member].getAllInfo()

if __name__ == "__main__":
    main()
