import React from 'react';
import './App.css';
import Navbar from './components/Navbar';
import Bevbanner from './components/Bevbanner';
import Browsebanner from './components/Browsebanner';

function App() {
  return (
    <div className="App">
      <Navbar />
      <Bevbanner />
      <Browsebanner />
    </div>
  );
}

export default App;
