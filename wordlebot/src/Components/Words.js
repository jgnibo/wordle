import wordBank from '../wordle-bank.txt'

export const boardDefault = [
  ["", "", "", "", ""],
  ["", "", "", "", ""],
  ["", "", "", "", ""],
  ["", "", "", "", ""],
  ["", "", "", "", ""],
  ["", "", "", "", ""]
];


export const generateWordSet = async () => {
  let wordSet;
  let randWord;
  await fetch(wordBank)
    .then((response) => response.text())
    .then((result) =>{
      const wordArr = result.split("\n");
      wordSet = new Set(wordArr);
      randWord = wordArr[Math.floor(Math.random() * wordArr.length)];
      randWord = randWord.toUpperCase();
    });

    return{ wordSet, randWord };

}