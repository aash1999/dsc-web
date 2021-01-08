import React from "react";
import { NavLink } from "react-router-dom";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

import routes from "../../routes.js";

import "./Navbar.css";
// import logo from "../../assets/img/dsc_iiitk_logo_white.png";
// import ham from "../../assets/img/hamburger.png";
// import account from "../../assets/img/account1.svg";

function Navbar() {
  return (
    <nav className="navbar">
      <ul className="navbar-nav">
        {routes.map(({ icon, name, path }) => (
          <li className="nav-item">
            <NavLink
              className="nav-link"
              to={path}
              activeStyle={{ color: "rgb(82,64,185)" }}
            >
              <FontAwesomeIcon icon={icon} size="lg" fixedWidth />
              <span>{name}</span>
            </NavLink>
          </li>
        ))}
      </ul>
    </nav>
  );
}

export default Navbar;
