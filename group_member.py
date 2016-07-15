class GroupMember:

    def __init__(self, name):
        self.name = name
        self.postAmount = 0
        self.imagesAmount = 0
        self.audioAmount = 0
        self.videoAmount = 0
        self.characterAmount = 0
        self.averagePostLength = 0
        self.postTimeHistogram = {}
        self.postWeekdayHistogram = {}
        self.postDateHistogram = {}
        self.wordsHistogram = {}

    #Setters

    def setName(self, name):
        self.name = name

    def incrementPostAmount(self):
        self.postAmount += 1

    def incrementImagesAmount(self):
        self.imagesAmount += 1

    def incrementAudioAmount(self):
        self.audioAmount += 1

    def incrementVideoAmount(self):
        self.videoAmount += 1

    def increaseCharacterAmount(self, amount):
        self.characterAmount += amount

    def addToPostWeekdayHistogram(self, weekday):
        try:
            self.postWeekdayHistogram[weekday] += 1
        except KeyError:
            self.postWeekdayHistogram[weekday] = 1

    def addToPostTimeHistogram(self, hour):
        self.postTimeHistogram[hour] += 1

    def addToPostDateHistogram(self, date):
        self.postDateHistogram[date] += 1

    def addtoWordsHistogram(self, word):
        self.wordsHistogram[word] += 1

    #getters

    def getName(self):
        return self.name

    def getPostAmount(self):
        return self.postAmount

    def getImagesAmount(self):
        return self.imagesAmount

    def getAudioAmount(self):
        return self.audioAmount

    def getVideoAmount(self):
        return self.videoAmount

    def getAveragePostLength(self):
        return self.characterAmount / self.postAmount

    def getPostWeekdayHistogram(self):
        return self.postWeekdayHistogram

    def getPostTimeHistogram(self):
        return self.postTimeHistogram

    def getPostDateHistogram(self):
        return self.postDateHistogram

    def getWordsHistogram(self):
        return self.postDaHistogram

    def getAllInfo(self):
        userObj = {}

        userObj['name'] = self.getName()
        userObj['postsAmount'] = self.getPostAmount()
        userObj['images'] = self.getImagesAmount()
        userObj['audio'] = self.getAudioAmount()
        userObj['video'] = self.getVideoAmount()
        userObj['averagePostLength'] = self.getAveragePostLength()
        userObj['weekdays'] = self.getPostWeekdayHistogram()

        return userObj
