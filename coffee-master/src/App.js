import React from 'react';
import './App.css';
import Navbar from './components/Navbar';
import Bevbanner from './components/Bevbanner';
import Browsebanner from './components/Browsebanner';
import Login from './components/Login';
import Signup from './components/signup';
import BevBuilder from './components/BevBuilder';
import BevBrowser from './components/Browser';
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom';

function App() {
  return (
    <Router>
    <div className="App">
      <Navbar />
      <Switch> 
        <Route path="/index">
            <Bevbanner />
            <Browsebanner />
        </Route>
        <Route path="/login" component={Login} />
        <Route path="/beverage-builder" component={BevBuilder} />
        <Route path="/signup" component={Signup} />
        <Route path="/browse" component={BevBrowser} />
      </Switch>
    </div>
    </Router>
  );
}

export default App;

