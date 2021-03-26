import React from 'react';
import './bevbanner.css'
import frap from './frap.png';

function Bevbanner() {
    return (
        <div className='bevBanner'>
            <img src={frap} alt="Fraps" className="bevPNG"/>
            <ul className = 'bevText'>
                <li className = 'header1'>Beverage Builder</li>
                <li className = 'header2'>Build your own custom drink with our new tool</li>
                <li className = 'sbutton'>Get Started</li>
            </ul>
        </div>
    );
  }
  
  export default Bevbanner;
