import { useEffect, useState } from "react";

const BKG = () => {
  const [pic, setPic] = useState(0);

  useEffect(() => {
    const bgs = document.querySelectorAll(".background");
    bgs.forEach((img, i) => {
      img.classList.remove("active");
      if (i === pic) {
        img.classList.add("active");
      }
    });

    setTimeout(() => {
      setPic(pic < 3 ? pic + 1 : 0);
    }, 13000);
    console.log(pic);
  }, [pic]);

  return (
    <div className="relative top-0 right-0 bottom-0 left-0">
      <img
        src={require("../assets/bg1.jpg")}
        alt="bg-1"
        className="background active"
      />
      <img
        src={require("../assets/bg2.jpg")}
        alt="bg-2"
        className="background"
      />
      <img
        src={require("../assets/bg3.jpg")}
        alt="bg-3"
        className="background"
      />
      <img
        src={require("../assets/bg4.jpg")}
        alt="bg-4"
        className="background"
      />
    </div>
  );
};

export default BKG;
