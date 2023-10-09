import { useState, useEffect } from "react";

const meta = {
  title: "About Us | StarScream",
  description: "Meet Team StarScream",
};

const info = [
  {
    pic: require("../assets/Ray.png"),
    name: "Rayman Jamal",
    background: "Software Engineering",
    role: ["Team Lead", "Backend Development"],
  },
  {
    pic: require("../assets/Jon.jpg"),
    name: "Jonanthan Ong",
    Background: "Software Engineering and Industrial Engineering",
    role: ["Research & Development", "Project Coordination"],
  },
  {
    pic: require("../assets/Tochi.jpg"),
    name: "Tochi Oramasionwu",
    Background: "Mechanical Engineering and Software Engineering",
    role: ["Full-Stack Development", "Musical Subject Matter Expert"],
  },
  {
    pic: require("../assets/Deep.png"),
    name: "Jaydeep",
    Background: "Data Engineering",
    role: ["Data Engineering", "Audio Engineering"],
  },
];

const About = () => {
  const [member, setMember] = useState(-1);

  useEffect(() => {
    if (member !== -1) {
      document.querySelector(".generic")?.classList.add("inactive");
    } else {
      document.querySelector(".generic")?.classList.remove("inactive");
    }

    const group = document.querySelectorAll(".member");
    const descs = document.querySelectorAll(".info");

    group.forEach((person, i) => {
      person?.classList.remove("active");
      descs[i]?.classList.remove("active");
      if (i === member) {
        person?.classList.add("active");
        descs[i]?.classList.add("active");
      }

      if (member > -1 && i !== member) {
        person?.classList.add("darkened");
      } else {
        person?.classList.remove("darkened");
      }
    });
  }, [member]);

  const scroll = () => {
    const desc = document.querySelector(".desc-win");
    desc.scrollIntoView({ behavior: "smooth" });
  };

  return (
    <div className="main-padding py-28">
      <div className="md:mx-16 mx-1 bg-white/50 backdrop-blur-md rounded-xl md:px-32 sm:px-14 px-5">
        <div className="pb-28">
          <div className="py-20 mx-auto text-center">
            <h3>Team</h3>
            <div
              to="/"
              className="flex text-white items-baseline justify-center"
            >
              <h2 className="h-fit">star</h2>
              <h1 className="italic text-proj_blue">SCREAM</h1>
            </div>
          </div>
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
            ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
            aliquip ex ea commodo consequat. Duis aute irure dolor in
            reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
            pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
            culpa qui officia deserunt mollit anim id est laborum.
          </p>
        </div>

        <div className="relative pb-[650px]">
          <h2 className="pb-16 text-center text-proj_blue">Team Members</h2>
          <div className="flex justify-around gap-8 flex-wrap">
            {info.map((member, i) => (
              <div
                key={i}
                className="group cursor-pointer member"
                onClick={() => {
                  setMember(i);
                  scroll();
                }}
              >
                <img
                  src={member.pic}
                  alt={member.name}
                  className="rounded-xl w-64 h-72 object-cover group-hover:scale-110 duration-300"
                />
                <h4 className="w-64 text-center py-6">{member.name}</h4>
              </div>
            ))}
          </div>

          <div className="mt-10 desc-win">
            <div className="generic flex flex-col justify-center">
              <h4 className="md:w-1/3 sm:w-full text-center mx-auto">
                Click on a member of the team to learn about them
              </h4>
            </div>

            {info.map((info, i) => (
              <div key={i} className="info">
                <h2>{info.name}</h2>
                <div>
                  <h4 className="pb-3">Background:</h4>
                  <p>{info.background}</p>
                </div>
                <div>
                  <h4 className="pb-3">Project Role:</h4>
                  <p>{` - ${info.role[0]} - `}</p>
                  <p>{` - ${info.role[1]} - `}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default About;
