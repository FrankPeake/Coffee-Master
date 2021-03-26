import React from 'react';
import { Route } from 'react-router-dom';
import './browser.css';

function BevBrowser() {

    return (
        <div className='browser-containter'>
            <div className='banner'>
                <h1 className='header3'>Browse Hand Crafted Beverages</h1> 
                <input name='search' type="text" placeholder="Search.."></input>                        
                <button className='search-btn'>Search</button>
            </div>
        </div>
    );
  }
  
  export default BevBrowser;