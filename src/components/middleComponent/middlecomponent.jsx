import React from "react";
import "./middlecomponent.css";
import Typist from "react-typist"
function MiddleComponent() {
  return (
    <div className="container-middle">
        <div className="title"><Typist avgTypingDelay={80} >/  DSC IIITDM Kurnool </Typist></div>
    </div>
  );
}

export default MiddleComponent;
