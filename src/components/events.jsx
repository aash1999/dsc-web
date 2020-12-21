import React from "react";
import "./events.css";
import Title from "./title.jsx";
import EventCard from "./eventsCard.jsx";
//import Carousel from "react-elastic-carousel";
import Carousel from 'react-bootstrap/Carousel'


function Events() {
  var noOf = document.getElementsByClassName("gridContainer")[0];
  console.log(noOf);
  return (
    <div className="eventsContainer">
      <Title title="Events" />
      <Carousel className="test">
        <Carousel.Item>
        <EventCard />
        </Carousel.Item>
        <Carousel.Item>
          <EventCard />
        </Carousel.Item>
        <Carousel.Item>
          <EventCard />
        </Carousel.Item>
        <Carousel.Item>
          <EventCard />
        </Carousel.Item>
        <Carousel.Item>
          <EventCard />
        </Carousel.Item>
    </Carousel>


    </div>
  );
}

export default Events;
