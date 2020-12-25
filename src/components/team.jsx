import React from "react";
import "./team.css";
import Title from "./title.jsx";
import AliceCarousel from "react-alice-carousel";
import "react-alice-carousel/lib/alice-carousel.css";
import TeamCard from "./teamCard.jsx";
const responsive = {
  0: { items: 1 },
  568: { items: 2 },
  1024: { items: 4 },
};

const items = [
  <TeamCard />,
  <TeamCard />,
  <TeamCard />,
  <TeamCard />,
  <TeamCard />,
  <TeamCard />,
];

function Team() {
  return (
    <div className="teamContainer">
      <div>
        <Title title="Team" />
        <AliceCarousel mouseTracking items={items} responsive={responsive} />
      </div>
      <div>
        <AliceCarousel mouseTracking items={items} responsive={responsive} />
      </div>
      <div>
        <AliceCarousel mouseTracking items={items} responsive={responsive} />
      </div>
    </div>
  );
}

export default Team;
