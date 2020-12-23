import React ,{useState}from "react";
import "./events.css";
import Title from "./title.jsx";
import EventCard from "./eventsCard.jsx";
//import Carousel from "react-elastic-carousel";
import Carousel from "react-bootstrap/Carousel";
import AliceCarousel from "react-alice-carousel";
import "react-alice-carousel/lib/alice-carousel.css";
import Dropdown from "react-css-dropdown";
import dropDownIcon from "../assets/img/right-arrow.svg";
const responsive = {
  0: { items: 1 },
  568: { items: 2 },
  1024: { items: 4 },
};

const items = [
  <EventCard />,
  <EventCard />,
  <EventCard />,
  <EventCard />,
  <EventCard />,
  <EventCard />,
  <EventCard />,
  <EventCard />,
  <EventCard />,
  <EventCard />,
  <EventCard />,
  <EventCard />,
  <EventCard />,
  <EventCard />,
  <EventCard />,
  <EventCard />,
  <EventCard />,
  <EventCard />,
];

function Events() {

  const [displayState,onDisplayState] = useState({message:"Present",icon:"dropDown",textColor:"dropdown1"})
  function hey(){
    if(displayState.message == "Present"){
      onDisplayState({message:"Past",icon:"dropDown-invert",textColor:"dropdown1 dropdown1-red"})

    }else{
      onDisplayState({message:"Present",icon:"dropDown",textColor:"dropdown1"})
    }
  }
  return (
    <div className="eventsContainer">
      <Title title="Events" />
      <div className= {displayState.textColor}onClick={hey}>
        {displayState.message}
        <img className={displayState.icon} src={dropDownIcon} />
      </div>
      <AliceCarousel mouseTracking items={items} responsive={responsive} />
    </div>
  );
}

export default Events;
