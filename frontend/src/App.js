import "./App.css";

import { Routes, Route, BrowserRouter as Router } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./components/Home";
import Project from "./components/Project";
import About from "./components/About";
import Son from "./components/Son";
import BKG from "./components/BKG";

function App() {
  return (
    <Router>
      <BKG />
      <Navbar />
      <main>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/project" element={<Project />} />
          <Route path="/about-us" element={<About />} />
          <Route path="/sonifications" element={<Son />} />
        </Routes>
      </main>
    </Router>
  );
}

export default App;
