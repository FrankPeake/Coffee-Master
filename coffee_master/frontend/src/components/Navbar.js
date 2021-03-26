import React from 'react';
import './navbar.css'
import Logo from './sblogo.svg';
import { Link } from 'react-router-dom';

function Navbar() {
    return (
        <nav className="navbar">
            <img src={Logo} alt="Coffee Masters" className="Logo"/>
            <ul className="nav-links">
                <Link to='/index' className='blkLink'>
                    <li>Home</li>
                </Link>
                <Link to='/beverage-builder' className='blkLink'>
                    <li>Bevarge Builder</li>
                </Link>
                <Link to='/browse' className='blkLink'>
                    <li>Browse</li>
                </Link>
            </ul>
            <ul className="signUp">
                <Link to='/login' className='blkLink'>
                    <li className='signIn'>Sign In</li>
                </Link>
                <Link to='/signup' className='blkLink'>
                    <li className='joinNow'>Sign Up</li>
                </Link>
            </ul>
        </nav>
    );
  }
  
  export default Navbar;

