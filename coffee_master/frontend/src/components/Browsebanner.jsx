import React from 'react';
import './browsebanner.css'
import Siren from './siren.png';

function Browsebanner() {
    return (
        <div className='browsebanner'>
            <img src={Siren} alt="" className="siren"/>
            <ul className = 'browseText'>
                <li className = 'header1'>Browse Custom Creations</li>
                <li className = 'header2'>Take a look through all our barista and customer created beverages</li>
                <li className = 'sbutton-browse'>Get Started</li>
            </ul>
        </div>
    );
  }
  
  export default Browsebanner;