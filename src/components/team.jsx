import React from "react";
import "./team.css";
import Title from "./title.jsx";
import EventCard from "./eventsCard.jsx";
//import Carousel from "react-elastic-carousel";
import Carousel from 'react-bootstrap/Carousel'
import AliceCarousel from 'react-alice-carousel';
import 'react-alice-carousel/lib/alice-carousel.css';
import TeamCard from "./teamCard.jsx"
const responsive = {
    0: { items: 1 },
    568: { items: 2 },
    1024: { items: 3 },
};

const items = [
    <TeamCard />,
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


function Team() {

  return (
    <div className="teamContainer">

   <TeamCard />
    </div>
  );
}
//    <Title title="Team..." />
//    <AliceCarousel
//     mouseTracking
//     items={items}
//     responsive={responsive}
// />

export default Team;
