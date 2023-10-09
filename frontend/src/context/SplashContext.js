import { createContext } from "react";

const SplashContext = createContext({
  splashScreen: "",
  setSplashScreen: (splashScreen) => {},
});

export default SplashContext;
