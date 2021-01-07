import React from "react";
import { Link } from "react-router-dom";
// import logo from "../../assets/img/dsc_iiitk_logo_white.png";
// import ham from "../../assets/img/hamburger.png";
// import "bootstrap/dist/css/bootstrap.min.css";
import "./navbar.css";
// import account from "../../assets/img/account1.svg";
// import Typist from "react-typist";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

import routes from "../../routes.js";

function navbar() {
  return (
    <nav className="navbar">
      <ul className="navbar-nav">
        <li className="nav-item" >
          <Link className="nav-link" to={routes.home}>
            <FontAwesomeIcon icon={["fa", "home"]} size="lg" fixedWidth/>
            <span>Home</span>
          </Link>
        </li>
        <li className="nav-item" >
          <Link className="nav-link" to={routes.about}>
            <FontAwesomeIcon icon={["fa", "info-circle"]} size="lg" fixedWidth/>
            <span>About</span>
          </Link>
        </li>
        <li className="nav-item" >
          <Link className="nav-link" to={routes.events}>
            <FontAwesomeIcon icon={["fa", "calendar-alt"]} size="lg" fixedWidth/>
            <span>Events</span>
          </Link>
        </li>
        <li className="nav-item" >
          <Link className="nav-link" to={routes.projects}>
            <FontAwesomeIcon icon={["fa", "project-diagram"]} size="lg" fixedWidth/>
            <span>Projects</span>
          </Link>
        </li>
        <li className="nav-item" >
          <Link className="nav-link" to={routes.teams}>
            <FontAwesomeIcon icon={["fa", "users"]} size="lg" fixedWidth/>
            <span>Team</span>
          </Link>
        </li>
        <li className="nav-item" >
          <Link className="nav-link" to={routes.contacts}>
            <FontAwesomeIcon icon={["fa", "address-book"]} size="lg" fixedWidth/>
            <span>Contacts</span>
          </Link>
        </li>
        <li className="nav-item" >
          <Link className="nav-link" to={routes.contacts}>
            <FontAwesomeIcon icon={["fa", "user-circle"]} size="lg" fixedWidth/>
            <span>Profile</span>
          </Link>
        </li>
      </ul>
    </nav>
  );
}

export default navbar;

// const Example = () => {
//   var signedIn = true;
//   function signedInorNot() {
//     if (signedIn === true) {
//       return (
// <div className="accountIcon ">
//   <img
//     className="accountImg"
//     src={account}
//     alt="default-account-profile"
//   />
// </div>
//       );
//     } else {
//       return <div className="signin">SignIn</div>;
//     }
//   }

//   function CollapseElement() {
//     if (window.screen.width >= 899) {
//       return (
//         <ul className="links-container ">
//           <li className="link">
//             <Link to={routes.home}>Home</Link>
//           </li>
//           <li className="link">
//             <Link to={routes.about}>About Us</Link>
//           </li>
//           <li className="link">
//             <Link to={routes.events}>Events</Link>
//           </li>
//           <li className="link">
//             <Link to={routes.projects}>Projects</Link>
//           </li>
//           <li className="link">
//             <Link to={routes.teams}>Team</Link>
//           </li>
//           <li className="link">
//             <Link to={routes.contacts}>Contat Us</Link>
//           </li>
//           {signedInorNot()}
//         </ul>
//       );
//     } else {
//       return (
//         <div className="links-container">
//           <img className="ham" src={ham} alt="hamburger-menu" />
//         </div>
//       );
//     }
//   }

//   return (
//     <div className="navbar-container">
//       <div className="image-container"></div>
//       {CollapseElement()}
//     </div>
//   );
// };

// export default Example;
