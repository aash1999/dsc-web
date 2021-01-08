import React from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

import "./footer.css";

const footer = () => {
  return (
    <footer>
      <div className="footer-main-container">
        <div className="footer-item-left">
          <img
            src="https://images.shiksha.com/mediadata/images/1563534372phpcTYwB7.png"
            alt="DSC-IIITDM-KURNOOL"
          />
          <h4>DSC - IIITDM - Kurnool </h4>
        </div>
        <div className="footer-item-middle">
          <h2>L'elit. Quam, consectetur!</h2>
          <p>
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. fugiat
            distinctio?Lorem ipsum dolor sit amet, consectetur adipisicing elit.
            Tempora, reiciendis.
          </p>
        </div>
        <div className="footer-item-right">
          <h1>Socials</h1>
          <div className="socialmedia-icons-container">
            <a href="https://gmail.com" target="_blank" rel="noreferrer noopener">
              <FontAwesomeIcon
                className="socialmedia-icon"
                icon={["fas", "envelope"]}
                size="2x"
              />
            </a>
            <a href="https://github.com" target="_blank" rel="noreferrer noopener">
              <FontAwesomeIcon
                className="socialmedia-icon"
                icon={["fab", "github"]}
                size="2x"
              />
            </a>
            <a href="https://linkedin.com" target="_blank" rel="noreferrer noopener">
              <FontAwesomeIcon
                className="socialmedia-icon"
                icon={["fab", "linkedin"]}
                size="2x"
              />
            </a>
            <a href="https://instagram.com" target="_blank" rel="noreferrer noopener">
              <FontAwesomeIcon
                className="socialmedia-icon"
                icon={["fab", "instagram"]}
                size="2x"
              />
            </a>
          </div>
        </div>
      </div>
      <div className="footer-bottom-container">copyright@2020</div>
    </footer>
  );
};

export default footer;
