import React, { useState } from 'react';
import logo from "../assets/img/dsc_iiitk_logo_white.png"
import barSvg from "../assets/svg/bars-solid.svg"
import {useMediaQuery} from 'react-responsive'
import {Navbar,Nav,NavDropdown,Form,FormControl,Button} from 'react-bootstrap'

import 'bootstrap/dist/css/bootstrap.min.css';
import "./navbar.css"
const Example = (props) => {
  function hi(){
    console.log("hey")
  }
  return (
    <div>
    <Navbar onToggle={hi} bsPrefix="navbar" className="nav-bar"bg="dark" fixed="top" expand="lg">
    <Navbar.Brand href="#home"><img src={logo} className="logo-navbar" /></Navbar.Brand>
    <Navbar.Toggle   aria-controls="basic-navbar-nav" />
    <Navbar.Collapse bsPrefix= "navbar-collapse" className="toggle" id="basic-navbar-nav">
      <Nav className="ml-auto">
        <Nav.Link  href="#home"><span className="navText">AboutUs</span></Nav.Link>
        <Nav.Link href="#link"><span className="navText">Projects</span></Nav.Link>
        <Nav.Link  href="#home"><span className="navText">Events</span></Nav.Link>
        <Nav.Link href="#link"><span className="navText">Team</span></Nav.Link>
        <Nav.Link href="#link"><span className="navText">SignIn</span></Nav.Link>
      </Nav>

    </Navbar.Collapse>
    </Navbar>
    </div>
  );
}

export default Example;
