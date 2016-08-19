class TotalGroup:

    def __init__(self):
        self.name = "Total"
        self.totalPostAmount = 0
        self.totalImagesAmount = 0
        self.totalAudioAmount = 0
        self.totalVideoAmount = 0
        self.totalCharacterAmount = 0
        self.totalAveragePostLength = 0
        self.totalPostTimeHistogram = {}
        self.totalPostWeekdayHistogram = {}
        self.totalPostDateHistogram = {}
        self.totalWordsHistogram = {}

    #Setters

    def incrementTotalPostAmount(self):
        self.totalPostAmount += 1

    def incrementTotalImagesAmount(self):
        self.totalImagesAmount += 1

    def incrementTotalAudioAmount(self):
        self.totalAudioAmount += 1

    def incrementTotalVideoAmount(self):
        self.totalAudioAmount += 1

    def increaseTotalCharacterAmount(self, amount):
        self.totalCharacterAmount += amount

    def addToTotalPostWeekdayHistogram(self, weekday):
        try:
            self.totalPostWeekdayHistogram[weekday] += 1
        except KeyError:
            self.totalPostWeekdayHistogram[weekday] = 1

    def addToTotalPostTimeHistogram(self, hour):
        self.totalPostTimeHistogram[hour] += 1

    def addToTotalPostDateHistogram(self, date):
        self.totalPostDateHistogram[date] += 1

    def addtoTotalWordsHistogram(self, word):
        self.totalWordsHistogram[word] += 1

    #getters

    def getName(self):
        return self.name

    def getTotalPostAmount(self):
        return self.totalPostAmount

    def getTotalImagesAmount(self):
        return self.totalImagesAmount

    def getTotalAudioAmount(self):
        return self.totalAudioAmount

    def getTotalVideoAmount(self):
        return self.totalVideoAmount

    def getTotalAveragePostLength(self):
        return self.totalCharacterAmount / self.totalPostAmount

    def getTotalPostWeekdayHistogram(self):
        return self.totalPostWeekdayHistogram

    def getTotalPostTimeHistogram(self):
        return self.totalPostTimeHistogram

    def getTotalPostDateHistogram(self):
        return self.totalPostDateHistogram

    def getTotalWordsHistogram(self):
        return self.totalWordsHistogram

    def getAllInfo(self):
        totalObj = {}

        totalObj['name'] = self.getName()
        totalObj['postsAmount'] = self.getTotalPostAmount()
        totalObj['images'] = self.getTotalImagesAmount()
        totalObj['audio'] = self.getTotalAudioAmount()
        totalObj['video'] = self.getTotalVideoAmount()
        totalObj['averagePostLength'] = self.getTotalAveragePostLength()
        totalObj['weekdays'] = self.getTotalPostWeekdayHistogram()

        return totalObj
