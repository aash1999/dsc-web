import React from "react"
import sampleImg from "../../assets/img/dsc_logo.png";
import "./eventsCard.css"
var date = new Date().toDateString();

function EventCard(props){
  return(
    <div className="EventsCardContainer draw1-border ">
      <div className="EventsCardImageContainer">
        <img className="EventsCardImage" src={sampleImg} alt="event"/>
      </div>
      <div className="EventsCardTitle">Title</div>
      <div className="EventsCardDate">{date}</div>
      <div className="EventsCardDiscription">
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
      <div className="EventsCardRegister">Register</div>
    </div>
  )

}
export default EventCard
