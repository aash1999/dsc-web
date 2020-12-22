import React from "react";
import "./teamCard.css";

function TeamCard() {
  return (
    <div class="card draw-border">
      <img
        src="https://lh3.googleusercontent.com/ytP9VP86DItizVX2YNA-xTYzV09IS7rh4WexVp7eilIcfHmm74B7odbcwD5DTXmL0PF42i2wnRKSFPBHlmSjCblWHDCD2oD1oaM1CGFcSd48VBKJfsCi4bS170PKxGwji8CPmehwPw=w200-h247-no"
        alt="Person"
        class="card__image"
      ></img>
      <p class="card__name">Lily-Grace Colley</p>

      <div class="card__designation">Web Developer</div>

      <ul class="social-icons">
        <li>
          <a href="#">
            <i class="fa fa-github"></i>
          </a>
        </li>
        <li>
          <a href="#">
            <i class="fa fa-twitter"></i>
          </a>
        </li>
        <li>
          <a href="#">
            <i class="fa fa-linkedin"></i>
          </a>
        </li>
        
      </ul>
    </div>
  );
}

export default TeamCard;
