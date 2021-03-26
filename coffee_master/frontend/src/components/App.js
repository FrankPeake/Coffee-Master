import React from 'react';
import './App.css';
import Navbar from './Navbar';
import Bevbanner from './Bevbanner';
import Browsebanner from './Browsebanner';
import Login from './Login';
import Signup from './signup';
import BevBuilder from './BevBuilder';
import BevBrowser from './Browser';
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

