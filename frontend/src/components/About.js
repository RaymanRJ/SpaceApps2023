import { useState, useEffect } from "react";
import DocumentMeta from "react-document-meta";

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
    name: "Jonathan Ong",
    Background: "Software Engineering and Industrial Engineering",
    role: ["Research & Development", "Project Coordination"],
  },
  {
    pic: require("../assets/Tochi.jpg"),
    name: "Tochi Oramasionwu",
    Background: "Mechanical Engineering and Software Engineering",
    role: ["Full-Stack Development", "Content Production"],
  },
  {
    pic: require("../assets/Deep.png"),
    name: "Jaydeep Mistry",
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
    <div>
      <DocumentMeta {...meta}>
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
              We are passionate developers with diverse backgrounds excited to take on this challenge. 
              We created a method of sonifying 3D NASA fly-through photos. 
              <br/>
              From teaching English overseas to different engineering professions to software development, 
              our experiences vary greatly but solving problems is what brings us together.
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
      </DocumentMeta>
    </div>
  );
};

export default About;
