import React, { useState, useEffect} from 'react';
import './App.scss';
import Preloader from './Components/Preloader/Preloader'

function App() {
  useEffect(()=>{
    document.title="Ethereal";
  })
  return (
    <div className="App">
      <Preloader/>
    </div>
  );
}

export default App;
