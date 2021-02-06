import React from 'react';
import './navbar.css'
import Logo from './sblogo.svg';

function Navbar() {
    return (
        <nav className="navbar">
            <img src={Logo} alt="Coffee Masters" className="Logo"/>
            <ul className="nav-links">
                <li>Menu</li>
                <li>Bevarge Builder</li>
                <li>Store Locator</li>
            </ul>
            <ul className="signUp">
                <li className='signIn'>Sign In</li>
                <li className='joinNow'>Sign Up</li>
            </ul>
        </nav>
    );
  }
  
  export default Navbar;

