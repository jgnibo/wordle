import React, {useContext} from 'react'
import {AppContext} from "../App.js"


function Gameover() {
  const {gameOver, setGameOver, currAttempt, correctWord} =useContext(AppContext);

  return (
    <div className='gameover'>
      <h3>{gameOver.guessedWord ? "You got it":  "You failed"}</h3>
      <h1>Correct: {correctWord}</h1>
      {gameOver.guessedWord && 
        (<h3> You guessed in {currAttempt.attempt} attempts</h3>)}
      </div>
  )
}

export default Gameover