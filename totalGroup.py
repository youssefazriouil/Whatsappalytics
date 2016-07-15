class TotalGroup:

    def __init__(self):
        self.groupMembers = []
        self.totalPostAmount = 0
        self.totalImagesAmount = 0
        self.totalAudioAmount = 0
        self.totalAveragePostLength = 0
        self.totalPostTimeHistogram = {}
        self.totalPostDateHistogram = {}
        self.totalWordsHistogram = {}

    #Setters
    def addGroupMember(self, name):
        if(!(name in self.groupMembers):
            self.groupMembers.append(name)


    def incrementTotalPostAmount(self):
        self.totalPostAmount += 1

    def incrementTotalImagesAmount(self):
        self.totalimagesAmount += 1

    def incrementTotalAudioAmount(self):
        self.totalAudioAmount += 1

    def increaseTotalAveragePostLength(self, postLegth):
        self.totalAveragePostLength = (self.totalAveragePostLength + postLength) / self.totalPostAmount

    def addToTotalPostTimeHistogram(self, hour):
        self.totalPostTimeHistogram[hour] += 1

    def addToTotalPostDateHistogram(self, date):
        self.totalPostDateHistogram[date] += 1

    def addtoTotalWordsHistogram(self, word):
        self.totalWordsHistogram[word] += 1

    #getters
    def getAllGroupMembers(self):
        return self.groupMembers

    def getTotalPostAmount(self):
        return self.totalPostAmount

    def getTotalImagesAmount(self):
        return self.totalImagesAmount

    def getTotalAudioAmount(self):
        return self.totalAudioAmount

    def getTotalAveragePostLength(self):
        return self.totalAveragePostLength

    def getTotalPostTimeHistogram(self):
        return self.totalPostTimeHistogram

    def getTotalPostDateHistogram(self):
        return self.totalPostDateHistogram

    def getTotalWordsHistogram(self):
        return self.totalWordsHistogram
