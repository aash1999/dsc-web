import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

import CustomNavbar from "./components/navbar/navbar.jsx";
import Home from "./components/Home/Home.jsx";
import About from "./components/About/About.jsx";
import Events from "./components/events/events.jsx";
import Projects from "./components/projects/projects.jsx";
import Team from "./components/team/team.jsx";
import Footer from "./components/footer/footer.jsx";

import routes from "./routes";

import "./App.css"
import "./fontawesome";

function App() {
  return (
    <div className="app">
      <Router>
        <CustomNavbar />
        <Switch>
          <Route exact path={routes.home} component={Home} />
          <Route path={routes.about} component={About} />
          <Route path={routes.events} component={Events} />
          <Route path={routes.projects} component={Projects} />
          <Route path={routes.teams} component={Team} />
          <Route path={routes.contacts} component={Footer} />
        </Switch>
      </Router>
    </div>
  );
}

export default App;
