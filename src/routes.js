import Home from "./Components/Home/Home.jsx";
import About from "./Components/About/About.jsx";
import Events from "./Components/events/events.jsx";
import Projects from "./Components/projects/projects.jsx";
import Teams from "./Components/team/team.jsx";
import Contacts from "./Components/footer/footer.jsx";

const routes = [
    {
        component: Home,
        icon: ["fa", "home"],
        name: "Home",
        path: "/",
    },
    {
        component: About,
        icon: ["fa", "info-circle"],
        name: "About",
        path: "/about",
    },
    {
        component: Events,
        icon: ["fa", "calendar-alt"],
        name: "Events",
        path: "/events",
    },
    {
        component: Projects,
        icon: ["fa", "project-diagram"],
        name: "Projects",
        path: "/projects",
    },
    {
        component: Teams,
        icon: ["fa", "users"],
        name: "Teams",
        path: "/teams",
    },
    {
        component: Contacts,
        icon: ["fa", "address-book"],
        name: "Contacts",
        path: "/contacts",
    },
    {
        compnent: null, 
        icon: ["fa", "user-circle"],
        name: "Profile",
        path: "/profile"
    },
]


export default routes;