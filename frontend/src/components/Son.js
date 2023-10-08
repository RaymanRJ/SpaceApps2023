import { useState, useEffect } from "react";
import { Player } from "video-react";

const vids = [
  {
    url: "https://spaceapps2023.rrjamal.ca/videos/Waveform-output_video_westerlund2_1920x1080_30fps.mp4",
    thumbnail: require("../assets/Videos/1.png"),
    name: "Westerlund 2",
  },
  {
    url: "https://spaceapps2023.rrjamal.ca/videos/Waveform-output_video_westerlund2_1920x1080_30fps.mp4",
    thumbnail: require("../assets/Videos/2.png"),
    name: "Cosmic Dome 2",
  },
  {
    url: "https://spaceapps2023.rrjamal.ca/videos/Celestial Lightsabers: Stellar Jets in HH 24.mp4",
    thumbnail: require("../assets/Videos/3.png"),
    name: "Celestial Lightsabers",
  },
];

const Son = () => {
  const [plyr, setPlyr] = useState(-1);

  useEffect(() => {
    if (plyr > -1) {
      document.querySelector(".video-play")?.classList.add("active");
    } else {
      document.querySelector(".video-play")?.classList.remove("active");
    }
    console.log(plyr);
  }, [plyr]);

  return (
    <div className="main-padding py-28">
      <div className="mx-16 bg-white/50 backdrop-blur-md rounded-xl md:px-32 sm:px-14 px-5">
        <h1 className="pt-28 text-center px-10">
          Immerse yourself in the sounds of space!
        </h1>
        <div className="py-20">
          <div className="video-play">
            {plyr > -1 ? (
              <Player
                playsInline
                poster={vids[plyr].thumbnail}
                src={vids[plyr].url}
                autoPlay
              />
            ) : (
              <div></div>
            )}
          </div>
          <div className="border border-proj_blue rounded-xl p-12 flex gap-12 text-center w-full flex-wrap">
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
  );
};

export default Son;
