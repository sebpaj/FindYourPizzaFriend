import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

import "./App.css";
import Navbar from "./components/navbar";

import MainLayout from "./components/main-layout";

function App() {
  return (
    <div className="App">
      <Router>
        <Navbar />
        <Switch>
          <Route exact path="/" component={MainLayout} />
          <Route path="/pizza" component={MainLayout} />
        </Switch>
      </Router>
    </div>
  );
}

export default App;
