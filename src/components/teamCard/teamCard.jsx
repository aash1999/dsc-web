import React from "react";
import "./teamCard.css";
import avatar from "../../assets/img/avatar.png"


function TeamCard() {
  return (
    <div className="card draw-border">
      <img
        src={avatar}
        alt="Person"
        className="card__image"
      ></img>
      <p className="card__name">John Patrick</p>

      <div className="card__designation">Web Developer</div>

      <ul className="social-icons">
        <li>
          <a href="#">
            <i className="fa fa-github"></i>
          </a>
        </li>
        <li>
          <a href="#">
            <i className="fa fa-twitter"></i>
          </a>
        </li>
        <li>
          <a href="#">
            <i className="fa fa-linkedin"></i>
          </a>
        </li>

      </ul>
    </div>
  );
}

export default TeamCard;
