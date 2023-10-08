<<<<<<< HEAD
// import { useEffect, useState } from "react";
import splash from "../assets/splash.webm";
import splashBG from "../assets/spBG.mp4";

const Home = () => {
  return (
    <div>
      <div id="splash" className="relative">
        <video autoPlay muted className="object-cover w-full h-full">
          <source src={splashBG} type="video/mp4" />
        </video>
        <video
          autoPlay
          muted
          className="absolute -top-48 left-1/2 -translate-x-1/2 object-cover scale-50"
        >
          <source src={splash} type="video/mp4" />
        </video>
      </div>
=======
const Home = () => {
  return (
    <div className="py-32">
      <div className="mx-auto"></div>
>>>>>>> main
    </div>
  );
};

export default Home;
