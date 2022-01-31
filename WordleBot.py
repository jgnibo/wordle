#!/usr/bin/env python

class WordleBot():
    def __init__(self, filename):
        f = open(filename, "r")
        content = f.read()

        self.words = content.splitlines()
        self.charFrequencyMap = self.generateCharFrequencyMap()
        self.wordScores = []

        self.results = []
        self.greyLetters = {}
        print(self.charFrequencyMap)

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
        for word in self.words:
            self.wordScores.append((word, self.calculateWordScore(word)))

        return self.wordScores

    def findNextWord(self):
        top = 0
        for index, wordTuple in enumerate(self.wordScores):
            if wordTuple[1] > self.wordScores[top][1]:
                top = index

        return self.wordScores[top]



def main():
    wordle_bot = WordleBot("words.txt")
    #print(wordle_bot.getCharFrequencyMap())
    wordle_bot.generateWordScore()
    print(wordle_bot.findNextWord())



if __name__ == "__main__":
    """Run the main function."""
    main()
