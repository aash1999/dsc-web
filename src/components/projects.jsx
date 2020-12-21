import React from "react";
import "./projects.css";
import Title from "./title.jsx";
import EventCard from "./eventsCard.jsx";
//import Carousel from "react-elastic-carousel";
import Carousel from "react-bootstrap/Carousel";
import AliceCarousel from 'react-alice-carousel';
import 'react-alice-carousel/lib/alice-carousel.css';
const responsive = {
    0: { items: 1 },
    568: { items: 2 },
    1024: { items: 3 },
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

function Projects() {
  return (
    <div className="projectsContainer">
      <Title title="Projects" />
      <AliceCarousel
       mouseTracking
       items={items}
       responsive={responsive}
   />
    </div>
  );
}

export default Projects;
