import React from "react";
import "./events.css";
import Title from "./title.jsx";
import EventCard from "./eventsCard.jsx";
import Carousel from "react-elastic-carousel";
const breakPoints = [
  { width: 1, itemsToShow: 1 },
  { width: 550, itemsToShow: 2, itemsToScroll: 2 },
  { width: 768, itemsToShow: 3 },
  { width: 1200, itemsToShow: 4 }
];

function Events() {
  var noOf = document.getElementsByClassName("gridContainer")[0];
  console.log(noOf);
  return (
    <div className="eventsContainer">
      <Title title="Events" />

        <EventCard />
    

    </div>
  );
}

export default Events;
