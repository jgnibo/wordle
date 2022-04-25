import React from 'react';
import {useContext} from 'react';
import { AppContext} from '../App.js';

function Key({keyVal, bigKey, disabled}) {
  const { board, setBoard, currAttempt, setCurrAttempt, onDelete, onSelectLetter, onEnter} = useContext(AppContext);
  const selectLetter = () => {
    if(keyVal === "ENTER"){
      onEnter();
    } 
    else if(keyVal === "DELETE"){
      onDelete();
    }
    else{
      onSelectLetter(keyVal);
    }

  }
  return (
    <div className = "key" id = {bigKey ? "big": disabled && "disabled"} onClick = {selectLetter}>{keyVal}</div>
  );
}

export default Key;