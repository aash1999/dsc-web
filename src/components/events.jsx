import React from "react";
import "./events.css";
import Title from "./title.jsx";
import EventCard from "./eventsCard.jsx";

function Events() {
  var noOf = document.getElementsByClassName("gridContainer")[0];
  console.log(noOf);
  return (
    <div className="eventsContainer">
      <Title title="Events" />
      <div className="gridContainer">
        <div className="gridItem">
          <EventCard />
        </div>
        <div className="gridItem">
          <EventCard />
        </div>
        <div className="gridItem">
          <EventCard />
        </div>
        

      </div>
    </div>
  );
}

export default Events;
