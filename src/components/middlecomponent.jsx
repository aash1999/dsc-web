import React from "react";
import background from "../assets/img/background3.jpg";
import collegeLogo from "../assets/img/iiitk_logo.png";
import plusIcon from "../assets/img/plus_icon.png";
import dscLogo from "../assets/img/dsc_logo.png";
import "./middlecomponent.css";
function MiddleComponent() {
  return (
    <div className="container-middle">
      <div>
        <div className="backgroundContainer">
        <img className = "backgroundImg"src={background}/>
        </div>
        <div className="dscLogoContainer">
          <img className="dscLogo" src={dscLogo} />
        </div>
        <div className="xContainer">
          <p className="x">X</p>
        </div>
        <div className="iiitdmkLogoContainer">
          <img className="iiitdmkLogo" src={collegeLogo} />
        </div>
      </div>

      <div className="title">DSC IIITDM Kurnool </div>
      
    </div>
  );
}

export default MiddleComponent;
