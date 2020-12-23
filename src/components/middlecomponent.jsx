import React from "react";
import background from "../assets/img/background3.jpg";
import collegeLogo from "../assets/img/iiitk_logo.png";
import plusIcon from "../assets/img/plus_icon.png";
import dscLogo from "../assets/img/dsc_logo.png";
import "./middlecomponent.css";
import Typist from "react-typist"
function MiddleComponent() {
  return (
    <div className="container-middle">
        <div className="title"><Typist avgTypingDelay={30} >/  DSC IIITDM Kurnool </Typist></div>
    </div>
  );
}

export default MiddleComponent;
