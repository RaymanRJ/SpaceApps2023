import { useEffect } from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
  useEffect(() => {
    setTimeout(() => {
      document.querySelector(".nav")?.classList.add("active");
      setTimeout(() => {
        document.querySelector(".nav")?.classList.add("default");
        document.querySelector(".nav")?.classList.remove("active");
      }, 4000);
    }, 5000);
  }, []);

  return (
    <div className="nav start">
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
      </div>
    </div>
  );
};

export default Navbar;
