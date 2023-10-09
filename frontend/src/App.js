import "./App.css";

import { useState } from "react";
import { Routes, Route, BrowserRouter as Router } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./components/Home";
import Project from "./components/Project";
import About from "./components/About";
import BKG from "./components/BKG";
import SplashContext from "./context/SplashContext";
import Splash from "./components/Splash";

function App() {
  const [splashScreen, setSplashScreen] = useState(true);

  return (
    <Router>
      <BKG />
      <Navbar />
      <SplashContext.Provider value={{ splashScreen, setSplashScreen }}>
        <Splash />
        <main>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/project" element={<Project />} />
            <Route path="/about-us" element={<About />} />
          </Routes>
        </main>
      </SplashContext.Provider>
    </Router>
  );
}

export default App;
