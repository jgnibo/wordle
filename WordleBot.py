#!/usr/bin/env python

class WordleBot():
    def __init__(self, filename):
        f = open(filename, "r")
        content = f.read()

        self.words = content.splitlines()
        self.wordsDict = {}
        self.charFrequencyMap = self.generateCharFrequencyMap()
        self.wordScores = []

        self.results = []
        self.greyLetters = {}
        self.yellows = []
        self.yellowCount = {}
        
        self.alpha = "abcdefghijklmnopqrstuvwxyz"
        self.yellowCount = {}
        


        # print(self.charFrequencyMap)

    def generateCharFrequencyMap(self):
        charFrequencyMap = {}
        for word in self.words:
            for character in word:
                if character in charFrequencyMap:
                    charFrequencyMap.update({character: charFrequencyMap[character] + 1})
                else:
                    charFrequencyMap[character] = 1

        return charFrequencyMap

    def getCharFrequencyMap(self):
        return self.charFrequencyMap

    def playWordle(self, result):
        print("test")

    def genLastYellowCount(self):
        for char in self.alpha:
            self.yellowCount[char] = 0

        for item in self.yellows:
            if(item[1] == "yellow"):
                self.yellowCount.update({item[0]: self.yellowCount[item[0]]+1})


    def calculateWordScore(self, word):
        score = 0

        wordFrequencyMap = {}
        for character in word:
            if character in wordFrequencyMap:
                wordFrequencyMap.update({character: wordFrequencyMap[character] + 1})
            else:
                wordFrequencyMap[character] = 1

        for character in wordFrequencyMap:
            score += self.charFrequencyMap[character]

        return score/len(word)

    def generateWordScore(self):
        self.wordScores.clear()
        self.removeWords()
        for word in self.words:
            self.wordScores.append((word, self.calculateWordScore(word)))

        return self.wordScores
    
    def checkGreys(self, word):
        for character in word:
            if(character in self.greyLetters):
                return(False)
        
        return(True)

    def checkYellows(self, word):
        i = 0

        if(len(self.yellows)==0):
            return(True)

        self.genLastYellowCount()
        yellowChecker = {}
        
        for char in self.alpha:
            yellowChecker[char] = 0

        for character in word:
            if((self.yellows[i][1] == "yellow") and (self.yellows[i][0] == character)):
                return(False)
            elif(self.yellowCount[character]!=0):
                yellowChecker.update({character: yellowChecker[character] + 1})

            i += 1
        

        for char in yellowChecker:
            if yellowChecker[char] != self.yellowCount[char]:
                return(False)
            
        return(True)
    
    def updateYellows(self, lst):
        self.yellows = lst
    
    def removeWords(self):
        wordLst = []
        for word in self.words:
            if(self.checkYellows(word)==False or self.checkGreys(word)==False):
                wordLst.append(word)
        
        for word in wordLst:
            self.words.remove(word)

    def findNextWord(self):
        top = 0

        for index, wordTuple in enumerate(self.wordScores):
            if wordTuple[1] > self.wordScores[top][1]:
                top = index

        return self.wordScores[top]


def main():
    wordle_bot = WordleBot("words.txt")
    print(wordle_bot.checkYellows("ioeoi"))
    wordle_bot.generateWordScore()
    print(wordle_bot.findNextWord())
    wordle_bot.updateYellows([('a', 'yellow'), ('r', 'yellow'), ('o', 'grey'), ('s', 'yellow'), ('e', 'grey')])
    wordle_bot.greyLetters["o"] = 1
    wordle_bot.generateWordScore()
    print(wordle_bot.findNextWord())
    wordle_bot.updateYellows([('l', 'grey'), ('a', 'yellow'), ('s', 'yellow'), ('e', 'yellow'), ('r', 'yellow')])
    wordle_bot.greyLetters["l"] = 1
    wordle_bot.generateWordScore()
    print(wordle_bot.findNextWord())



if __name__ == "__main__":
    """Run the main function."""
    main()
