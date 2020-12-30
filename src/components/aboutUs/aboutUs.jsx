import React from "react";
import Title from "../title/title.jsx"
import "./aboutUs.css";
import Typist from 'react-typist';

function AboutUs() {
  return (
    <div className="mainContainer">
      <Title title="About Us"  />
      <div className="designContainer">

          <div className="content">
          <Typist avgTypingDelay={30}>
          <Typist.Delay ms={100} />
            Developer Student Clubs (DSC) is University based community group
            for students who are interested in Google Developer Technologies. As
            DSC Team, We teach students trending technologies such as Machine
            Learning, Deep Learning, Web Development, Android Development etc.
            Also, we organize hackathons and open workshops which can give
            technical exact solutions to the problems of common people. Our
            motto is to help students in building skills to produce scalable
            products and to help small businesses.<span><div className="cursor-blink-1"></div></span>
          </Typist>
        </div>
      </div>
    </div>
  );
}
export default AboutUs;
