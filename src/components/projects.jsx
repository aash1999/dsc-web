import React from "react";
import "./events.css";
import Title from "./title.jsx";
import EventCard from "./eventsCard.jsx";
//import Carousel from "react-elastic-carousel";
import Carousel from 'react-bootstrap/Carousel'


function Projects() {
  return (
    <div className="eventsContainer">
      <Title title="Projects" />
      <Carousel className="test" >
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

export default Projects;
