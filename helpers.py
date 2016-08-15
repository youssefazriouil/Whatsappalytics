#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string, re
from datetime import date, datetime
from group_member import GroupMember

def getCorrectedLine(line):
    line = line.decode("utf-8-sig").encode("utf-8")
    line = ''.join(char for char in line if char in string.printable)
    line = line.replace('\n', "")
    if(not line == ''):
        return line

def getIfCompletePost(line):
    return re.match(r"\d\d-\d\d-\d\d (\d\d:){3}", line)

def getDateObject(fullDate):
    dateObj = {}

    dateObj['fulldate'] = fullDate
    dateParts = fullDate.split("-")
    dateObj['day'] = dateParts[0]
    dateObj['month'] = dateParts[1]
    dateObj['year'] = dateParts[2]

    return dateObj

def getTimeObject(fullTime):
    timeObj = {}

    timeObj['fulltime'] =  fullTime
    timeParts = fullTime.split(":")
    timeObj['hours'] = timeParts[0]
    timeObj['minutes'] = timeParts[1]
    timeObj['seconds'] = timeParts[2]

    return timeObj


def getPostObject(line):
    postObj = {}
    weekdays = ['Maandag', 'Dinsdag', 'Woensdag', 'Donderdag', 'Vrijdag', 'Zaterdag', 'Zondag']

    postElements = line.split(":")
    postObj['author'] = postElements[3][1:].strip()
    postObj['text'] = ' '.join(postElements[4:])[1:]

    postElements = line.split(" ")
    weekdayDateTime = datetime.strptime(postElements[0], "%d-%m-%y")
    postObj['weekday'] = weekdays[date.weekday(weekdayDateTime)]

    postObj['date'] = getDateObject(postElements[0])
    postObj['time'] = getTimeObject(postElements[1][:-1])

    return postObj

def handleMetaPost(post, member):
    post = post[:-1] #verwijderen van carriage return
    if post == "<afbeelding weggelaten>":
        member.incrementImagesAmount()
    elif post == "<audio weggelaten>":
        member.incrementAudioAmount()
    elif post == "<video weggelaten>":
        member.incrementVideoAmount()

def processPostForUser(post, groupMembers):
    author = post['author']
    if not(author in groupMembers):
        groupMembers[author] = GroupMember(author)
    if 'weggelaten>' in post['text']:
        handleMetaPost(post['text'], groupMembers[author])
    else:
        groupMembers[author].incrementPostAmount()
        groupMembers[author].increaseCharacterAmount(len(post['text']))
        groupMembers[author].addToPostWeekdayHistogram(post['weekday'])

    return groupMembers
