import React, { useState } from "react";
import logo from "../../assets/img/dsc_iiitk_logo_white.png";
import ham from "../../assets/img/hamburger.png";
import "bootstrap/dist/css/bootstrap.min.css";
import "./navbar.css";
const Example = (props) => {


  function CollapseElement() {
    if (window.screen.width >= 959 ) {
      return (
        <div className="links-container ">
          <div className="link">
            <p>Home</p>
          </div>
          <div className="link">
            <p>AboutUs</p>
          </div>
          <div className="link">
            <p>Events</p>
          </div>
          <div className="link">
            <p>Projects</p>
          </div>
          <div className="link">
            <p>Team</p>
          </div>
          <div className="signin">
            <p>SignIn</p>
          </div>
        </div>
      );
    } else {
      return (
        <div className="links-container">
            <img className="ham" src={ham} />
        </div>
      );
    }
  }

  return (
    <div className="navbar-container">
      <div className="image-container">
        <img className="logo-dsc-desktop" src={logo} />
      </div>
      {CollapseElement()}
    </div>
  );
};

export default Example;
