import { useEffect, useState } from "react";

const BKG = () => {
  const [pic, setPic] = useState(-1);

  const height = document.querySelector("main")?.scrollHeight;
  console.log(height);

  useEffect(() => {
    const bgs = document.querySelectorAll(".background");
    if (pic === -1) {
      setTimeout(() => {
        setPic(0);
      }, 7000);
    } else {
      bgs.forEach((img, i) => {
        img.classList.remove("active");
        if (i === pic) {
          img.classList.add("active");
        }
      });

      setTimeout(() => {
        setPic(pic < 3 ? pic + 1 : 0);
      }, 13000);
    }
  }, [pic]);

  return (
    <div
      id="bak"
      className="absolute top-0 right-0 bottom-0 left-0 bg-black -z-50"
    >
      <div className="background">
        <img src={require("../assets/bg1.jpg")} alt="bg-1" />
        <div className="grad" />
      </div>
      <div className="background">
        <img src={require("../assets/bg2.jpg")} alt="bg-2" />
        <div className="grad" />
      </div>
      <div className="background">
        <img src={require("../assets/bg3.jpg")} alt="bg-3" />
        <div className="grad" />
      </div>
      <div className="background">
        <img src={require("../assets/bg4.jpg")} alt="bg-4" />
        <div className="grad" />
      </div>
    </div>
  );
};

export default BKG;
