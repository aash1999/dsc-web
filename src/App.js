import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

import Navbar from "./Components/Navbar/Navbar.jsx";

import routes from "./routes";

import "./App.css";
import "./fontawesome";

function App() {
  return (
    <div className="app">
      <Router>
        <Navbar />
        <Switch>
          {routes.map(({ component, path }) => (
            <Route path={path} component={component} exact />
          ))}
        </Switch>
      </Router>
    </div>
  );
}

export default App;
