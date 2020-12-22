import React from "react"
import CustomNavbar from "./components/navbar/navbar.jsx"
import MiddleComponent from "./components/middlecomponent.jsx"
import AboutUs from "./components/aboutUs.jsx"
import Events from "./components/events.jsx"
import Projects from "./components/projects.jsx"
import Team from "./components/team.jsx"

function App() {
  return (
    <div>
      <CustomNavbar />
      <MiddleComponent />
      <AboutUs />
      <Events />
      <Projects />
      <Team />


    </div>
  )
}

export default App;
