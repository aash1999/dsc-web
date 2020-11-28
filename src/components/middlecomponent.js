import React from 'react'
import background from "../assets/img/background3.jpg"
import collegeLogo from "../assets/img/iiitk_logo.png"
import plusIcon from "../assets/img/plus_icon.png"
import dscLogo from "../assets/img/dsc_logo.png"
import "./middlecomponent.css"
function MiddleComponent(){
  return(<div className="middleContainer">

    <img className="collegeLogo" src={collegeLogo}/>
    <img className="plusIcon" src={plusIcon}/>
    <img className="dscLogo" src={dscLogo}/>
    </div>)
}

export default MiddleComponent
