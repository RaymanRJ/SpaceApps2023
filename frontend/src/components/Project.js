import React from "react";

const meta = {
  title: "Our Work | StarScream",
  description: "Learn about our project",
};

const Project = () => {
  return (
    <div className="main-padding py-28">
      <div className="mx-16 bg-white/50 backdrop-blur-md rounded-xl md:px-32 sm:px-14 px-5 pb-32">
        <img
          src={require("../assets/spl.png")}
          alt="Space Apps"
          className="scale-50"
        />
        <h1 className="text-center text-proj_blue">
          Immersed in the Sounds of Space
        </h1>
        <h3 className="pt-20 pb-6">Challenge Summary</h3>
        <p>
          NASA offers a variety of “sonifications” - translations of 2D
          astronomical data into sound - that provide a new way to experience
          imagery and other information from space. Advanced instruments
          currently allow for sophisticated techniques to be used to enhance 2D
          astronomical images to make video representations called
          “fly-throughs” that allow viewers to experience what it would look
          like to move among space objects in 3D (three simulated spatial
          dimensions). The challenge is to design a method to create
          sonifications of 3D NASA space datasets to provide a different
          perceptual path that can help us understand and appreciate the wonders
          of the universe!
        </p>
        <div>
          <h2 className="pt-20 pb-10 text-center">Our Approach</h2>
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
            ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
            aliquip ex ea commodo consequat. Duis aute irure dolor in
            reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
            pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
            culpa qui officia deserunt mollit anim id est laborum.
            <br /> <br />
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
            ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
            aliquip ex ea commodo consequat. Duis aute irure dolor in
            reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
            pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
            culpa qui officia deserunt mollit anim id est laborum.
          </p>
        </div>
      </div>
    </div>
  );
};

export default Project;
