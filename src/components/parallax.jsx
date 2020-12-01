import React, { useState } from "react";
import "./parallax.css";
import aboutUsImg from "../assets/img/aboutUsImg.jpg";

function Parallax() {
  const [scrollState, setScrollSet] = useState(0);
  window.onscroll = function () {
    scrollFunction();
  };

  function scrollFunction() {
    //console.log(document.body.scrollTop,document.documentElement.scrollTop)
    if (
      document.body.scrollTop > 1560 ||
      document.documentElement.scrollTop > 1560
    ) {
      setScrollSet(1)
    } else {
      setScrollSet(0)
    }
  }
  return (
    <div>
      <div className="topPadding"></div>
      <div className="aboutUsImageContainer">
        <img className="aboutUsImage" src={aboutUsImg} />
      </div>
      <div className="aboutUsContentContainer">
        <div className="aboutUsTitleContainer">AboutUs</div>
        <div className="aboutUsContainer" scrollState={scrollState}>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas ac
            fermentum odio, quis pretium tortor. Quisque accumsan, turpis sit
            amet maximus rhoncus, nisl dolor euismod libero, et auctor lorem est
            nec sapien. Aenean at Lorem ipsum dolor sit amet, consectetur
            adipiscing elit. Maecenas ac fermentum odio, quis pretium tortor.
            Quisque accumsan, turpis sit amet maximus rhoncus, nisl dolor
            euismod libero, et auctor lorem est nec sapien. Aenean at

        </div>
      </div>
    </div>
  );
}

export default Parallax;
