import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <div className="main-padding py-4 flex justify-between bg-black/70 backdrop-blur-md items-center">
      <Link to="/" className="flex text-white items-baseline">
        <h2 className="h-fit">star</h2>
        <h1 className="italic text-proj_blue">SCREAM</h1>
      </Link>
      <div className="flex gap-12">
        <Link to="/project">
          <h3 className="nav-link">Project</h3>
        </Link>
        <Link to="/about-us">
          <h3 className="nav-link">About Us</h3>
        </Link>
        <Link to="/sonifications">
          <h3 className="nav-link">Sonifications</h3>
        </Link>
      </div>
    </div>
  );
};

export default Navbar;
