import React,{useState} from 'react';
import logo from "../../assets/img/dsc_iiitk_logo_white.png"
import {Navbar,Nav} from 'react-bootstrap'


import 'bootstrap/dist/css/bootstrap.min.css';
import "./navbar.css"
const Example = (props) => {
  const [hoverState,onHover] = useState('false')
  function hi(){

  }
  return (
    <div className="navbar-container">
    <div className="image-container">
    <img className="logo-dsc" src={logo}/>
    </div>
    <div className="links-container">
    <div className="link" >
    <p >Home</p>
    </div>
    <div className="link" >
    <p >AboutUs</p>
    </div>
    <div className="link" >
    <p >Events</p>
    </div>
    <div className="link" >
    <p >Projects</p>
    </div>
    <div className="link" >
    <p >Team</p>
    </div>
    <div className="link" >
    <p >SignIn</p>
    </div>
    </div>
    </div>

  );
}

export default Example;
