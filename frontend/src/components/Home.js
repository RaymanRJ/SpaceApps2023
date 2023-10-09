import { useEffect, useState, useContext } from "react";
import SplashContext from "../context/SplashContext";

const meta = {
  title: "Home | StarScream",
  description: "From starlight to soundwaves - Hear the sounds of space",
};

const vids = [
  {
    url: "https://spaceapps2023.rrjamal.ca/videos/Waveform-output_video_westerlund2_1920x1080_30fps.mp4",
    thumbnail: require("../assets/Videos/1.png"),
    name: "Westerlund 2",
  },
  {
    url: "https://spaceapps2023.rrjamal.ca/videos/Waveform-output_video_cosmic2_dome_1024x1024_30fps.mp4",
    thumbnail: require("../assets/Videos/2.png"),
    name: "Cosmic Dome 2",
  },
  {
    url: "https://spaceapps2023.rrjamal.ca/videos/Waveform-output_video_m51-flyby_1920x1080_30fps.mp4",
    thumbnail: require("../assets/Videos/3.png"),
    name: "Celestial Lightsabers",
  },
];

const Home = () => {
  const [plyr, setPlyr] = useState(0);

  const { splashScreen, setSplashScreen } = useContext(SplashContext);

  useEffect(() => {
    if (!splashScreen) {
      document.querySelector(".son").classList.add("active");
    }
  }, [splashScreen]);

  return (
    <div>
      <div className="son main-padding py-28">
        <div className="md:mx-16 mx-1 bg-white/50 backdrop-blur-md rounded-xl md:px-32 sm:px-14 px-5">
          <h1 className="pt-28 text-center px-10">
            Immerse Yourself in the Sounds of Space!
          </h1>
          <div className="py-20">
            <div className="pb-12">
              <iframe
                width="100%"
                height={650}
                src={vids[plyr].url}
                title="Embedded Video"
                allowFullScreen
                className="rounded-xl"
              ></iframe>
            </div>
            <div className="rounded-xl p-12 flex gap-12 justify-around text-center w-full flex-wrap">
              {vids.map((vid, i) => (
                <div key={i} className="group">
                  <div
                    className="cursor-pointer w-fit h-fit relative"
                    onClick={() => setPlyr(i)}
                  >
                    <img
                      src={vid.thumbnail}
                      alt={`video-${i}`}
                      className="rounded-xl w-80 h-52 object-cover"
                    />
                    <img
                      src={require("../assets/play.png")}
                      alt="play"
                      className="rounded-xl w-80 h-52 object-contain absolute top-0 right-0 bottom-0 left-0 opacity-0 group-hover:opacity-50 duration-300"
                    />
                  </div>
                  <h4 className="pt-3">{vid.name}</h4>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home;
