import React from "react";
import "./events.css";
import Title from "./title.jsx";
import EventCard from "./eventsCard.jsx";
//import Carousel from "react-elastic-carousel";
import Carousel from 'react-bootstrap/Carousel'
import AliceCarousel from 'react-alice-carousel';
import 'react-alice-carousel/lib/alice-carousel.css';
import Dropdown from 'react-css-dropdown'
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
    <EventCard />,<EventCard />,
    <EventCard />,
    <EventCard />,
    <EventCard />,
    <EventCard />,
    <EventCard />,<EventCard />,
    <EventCard />,
    <EventCard />,
    <EventCard />,
    <EventCard />,
    <EventCard />,<EventCard />
];


function Events() {

  return (
    <div className="eventsContainer">
      <Title title="Events" />
      <AliceCarousel
       mouseTracking
       items={items}
       responsive={responsive}
   />
    </div>
  );
}

export default Events;
