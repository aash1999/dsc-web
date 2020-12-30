import React from "react"
import CustomNavbar from "./components/navbar/navbar.jsx"
import MiddleComponent from "./components/middleComponent/middlecomponent.jsx"
import AboutUs from "./components/aboutUs/aboutUs.jsx"
import Events from "./components/events/events.jsx"
import Projects from "./components/projects/projects.jsx"
import Team from "./components/team/team.jsx"
import Footer from "./components/footer/footer.jsx";

import "./fontawesome"

function App() {
  return (
    <div>
      <CustomNavbar />
      <MiddleComponent />
      <AboutUs />
      <Events />
      <Projects />
      <Team />
      <Footer />
    </div>
  )
}

export default App;
