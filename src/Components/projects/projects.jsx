import React from "react";
import "./projects.css";
import Title from "../title/title.jsx";
import ProjectCard from "../projectCard/projectCard.jsx";
import AliceCarousel from 'react-alice-carousel';
import 'react-alice-carousel/lib/alice-carousel.css';
const responsive = {
    0: { items: 1 },
    568: { items: 2 },
    1024: { items: 4 },
};

const items = [
    <ProjectCard />,
    <ProjectCard />,
    <ProjectCard />,
    <ProjectCard />,
    <ProjectCard />,
    <ProjectCard />,
    <ProjectCard />,
    <ProjectCard />,
    <ProjectCard />,
    <ProjectCard />,
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
