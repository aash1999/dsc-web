import React from "react"
import sampleImg from "../../assets/img/dsc_logo.png";
import "./projectCard.css"
var date = new Date().toDateString();

function ProjectCard(props){
  return(
    <div className="ProjectsCardContainer draw2-border">
      <div className="ProjectsCardImageContainer">
        <img className="ProjectsCardImage" src={sampleImg} alt="project"/>
      </div>
      <div className="ProjectsCardTitle">Title</div>
      <div className="ProjectsCardDate">{date}</div>
      <div className="ProjectsCardDiscription">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi at
        metus eget ex rutrum semper. Suspendisse et orci non mi egestas
        varius. Suspendisse potenti. Nunc ante lacus, tempus eu fermentum sed,
        molestie vitae sapien. Maecenas dignissim erat vitae erat malesuada,
        eu pellentesque purus sodales. Phasellus aliquet nisl ut gravida
        rutrum. Fusce ultrices enim a facilisis tempor. In laoreet dignissim
        purus, sed scelerisque est lacinia quis. Etiam ligula dui, facilisis
        vitae arcu sit amet, pretium gravida elit. Nullam eu urna bibendum,
        dictum magna ut, blandit justo. Nulla facilisi. Quisque euismod
        pretium lectus in dictum. Nam at mauris id lorem hendrerit rutrum.
        Integer accumsan mauris ex, vel tempus dolor eleifend consectetur.
        Proin placerat turpis sit amet malesuada sollicitudin. Cras auctor
        pharetra nisi, bibendum tincidunt odio euismod et.
      </div>
      <div className="ProjectsCardRegister">View GitHub</div>
    </div>
  )

}
export default ProjectCard
