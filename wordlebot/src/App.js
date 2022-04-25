import './App.css';
import Board from "./Components/Board";
import Keyboard from './Components/Keyboard';
import Gameover from "./Components/Gameover";
import { createContext, useEffect, useState} from "react"; 
import { boardDefault, generateWordSet } from './Components/Words';



export const AppContext = createContext();

function App() {
  const [board, setBoard] = useState(boardDefault);
  const [currAttempt, setCurrAttempt] = useState({attempt: 0, letterPos: 0});
  const [wordSet, setWordSet] = useState(new Set());
  const [disabledLetters, setDisabledLetters] = useState([]);
  const [gameOver, setGameOver] = useState({gameOver: false, guessedWord: false});
  const [correctWord, setCorrectWord] = useState("");





  useEffect(() => {
    generateWordSet().then((words) => {
      setWordSet(words.wordSet);
      setCorrectWord(words.randWord);
    })
  }, []);

  const onSelectLetter = (keyVal) =>{
    if (currAttempt.letterPos > 4) return;
    const newBoard = [...board];
    newBoard[currAttempt.attempt][currAttempt.letterPos] = keyVal;
    setBoard(newBoard)
    setCurrAttempt({...currAttempt, letterPos: currAttempt.letterPos +1})
  }
  const onDelete = () =>{
    if(currAttempt.letterPos !== 0){
      const newBoard = [...board];
      newBoard[currAttempt.attempt][currAttempt.letterPos-1] = "";
      setBoard(newBoard)
      setCurrAttempt({...currAttempt, letterPos: currAttempt.letterPos -1});

    }
  }



  const onEnter = () =>{
    let checker = false;

    if(currAttempt.letterPos !== 5) return;

    let currWord = "";
    for(let i = 0; i<5; i++){
      currWord += board[currAttempt.attempt][i];
    }
    if(wordSet.has(currWord.toLowerCase())){
      console.log(currAttempt.attempt);
      setCurrAttempt({attempt: currAttempt.attempt+1, letterPos: 0});
      checker = false;
    } else{
      checker = true;
    }

    if (currWord === correctWord){
       setGameOver({gameOver: true, guessedWord: true});
       return;
    }

    if(currAttempt.attempt === 5 && !checker){
      setGameOver({gameOver: true, guessedWord: false});
    }
 
    
  }

  return (
    <div className="App">
      <nav>
        <h1>Wordle</h1>
      </nav>
      <AppContext.Provider value={{
        board, 
        setBoard, 
        currAttempt, 
        setCurrAttempt, 
        onSelectLetter, 
        onDelete, 
        onEnter,
        correctWord,
        setDisabledLetters,
        disabledLetters,
        setGameOver,
        gameOver
        }}> 
        <div className = "game">
          <Board />
          {gameOver.gameOver ? <Gameover/> : <Keyboard />}
        </div>

      </AppContext.Provider>

    </div>
  );
} 

export default App;
