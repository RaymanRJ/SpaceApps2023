import { useEffect, useContext } from "react";
import splash from "../assets/splash.webm";
import splashBG from "../assets/spBG.mp4";
import SplashContext from "../context/SplashContext";

const Splash = () => {
  const { splashScreen, setSplashScreen } = useContext(SplashContext);

  useEffect(() => {
    setTimeout(() => {
      setSplashScreen(false);
    }, 7000);

    const spScreen = document.querySelector(".splash");
    if (!splashScreen) {
      spScreen.classList.add("inactive");
      document.querySelector(".son")?.classList.add("active");
    } else {
      spScreen.classList.remove("inactive");
    }
    // eslint-disable-next-line
  }, [splashScreen]);

  return (
    <div className="splash">
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
  );
};

export default Splash;
