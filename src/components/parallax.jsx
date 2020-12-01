import React from "react";
import "./parallax.css";

function SubComponents() {
  return (
    <div className="mainContainer">
      <div className="aboutUsTitle">About Us</div>
      <div className="designContainer">
        <div className="topBar">
          <div className="circle"></div>
          <div className="circle1"></div>
          <div className="circle2"></div>
          <div className="content">
            Developer Student Clubs (DSC) is University based community group
            for students who are interested in Google Developer Technologies. As
            DSC Team, We teach students trending technologies such as Machine
            Learning, Deep Learning, Web Development, Android Development etc.
            Also, we organize hackathons and open workshops which can give
            technical exact solutions to the problems of common people. Our
            motto is to help students in building skills to produce scalable
            products and to help small businesses.
            <div className="cursor-blink-1"></div>
          </div>
        </div>
      </div>
    </div>
  );
}
export default SubComponents;
