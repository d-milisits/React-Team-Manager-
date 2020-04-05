import React from 'react';
import { BrowserRouter, Redirect, Route } from 'react-router-dom';
import './App.css';
import Teams from './components/Teams';
import Header from './components/Header';
import Players from './components/Players';
import Home from './components/Home';
import Manage from './components/Manage';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Header />
        <Redirect from="/" to="/home" />
        <Route path="/manage">
          <Manage />
        </Route>
        <Route path="/home">
          <Home />
        </Route>
        <Route path="/teams">
          <Teams />
        </Route>
        <Route path="/players">
          <Players />
        </Route>
      </BrowserRouter>
    </div>
  );
}

export default App;
