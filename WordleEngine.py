#!/usr/bin/env python
import random


class WordleEngine():
    def __init__(self, filename):
        f = open(filename, "r")
        content = f.read()

        self.words = content.splitlines()
        self.wordTable = self.createWordTable()
        f.close()
        # print(self.words)

    def getWords(self):
        return self.words

    def createWordTable(self):
        wordTable = {}
        for word in self.words:
            wordTable[word] = True

        return wordTable



    def startGame(self):
        word = random.choice(self.words)
        print("Welcome to Wordle!")
        tries = 1
        userin = self.requestWord()
        while userin != word and tries < 6:
            print(self.analyzeGuess(userin, word))

            userin = self.requestWord()
            tries += 1

        if userin == word:
            print("Congratulations! You guessed " + userin + " correctly!")
        else:
            print("Out of tries! The correct word was " + word)

    def requestWord(self):
        userin = input("Please enter a guess: ")
        if len(userin) != 5:
            print("Please enter a 5 letter word.")
            userin = self.requestWord()

        if userin not in self.wordTable:
            print(userin + " is not a word.")
            userin = self.requestWord()

        return userin

    def analyzeGuess(self, guess, word):
        wordFrequencyMap = {}
        for character in word:
            if character in wordFrequencyMap:
                wordFrequencyMap.update({character: wordFrequencyMap[character] + 1})
            else:
                wordFrequencyMap[character] = 1

        print("guess", guess)
        result = []  # Result is a tuple with character and wordle value (grey, green, yellow)
        for count, character in enumerate(guess):  # First we check for any characters in the correct place. All
            # other characters are set to grey tentatively
            if word[count] == character:
                result.append((character, "green"))
                wordFrequencyMap.update({word[count]: wordFrequencyMap[word[count]] - 1})
            else:
                result.append((character, "grey"))

        # Now we go back and check for correct characters in the wrong spot using the frequency map

        for count, guessCharacter in enumerate(guess):
            for wordCharacter in word:
                if guessCharacter == wordCharacter and result[count][1] != "green":
                    if wordFrequencyMap[wordCharacter] != 0:
                        result[count] = (guessCharacter, "yellow")
                        wordFrequencyMap.update({wordCharacter: wordFrequencyMap[wordCharacter] - 1})

        return result


def main():
    wordle_engine = WordleEngine("words.txt")
    wordle_engine.startGame()


if __name__ == "__main__":
    """Run the main function."""
    main()
