import React from "react";
import { createRoot } from "react-dom/client";
import {
  APIProvider,
  Map,
  MapCameraChangedEvent,
} from "@vis.gl/react-google-maps";

const App = () => (
  <APIProvider
    apiKey={"GOOGLE_MAP_API_KEY"}
    onLoad={() => console.log("Maps API has loaded.")}
  >
    <Map
      defaultZoom={13}
      defaultCenter={{ lat: 22.396428, lng: 114.109497 }}
      onCameraChanged={(ev: MapCameraChangedEvent) =>
        console.log(
          "camera changed:",
          ev.detail.center,
          "zoom:",
          ev.detail.zoom
        )
      }
    ></Map>
  </APIProvider>
);

const root = createRoot(document.getElementById("app"));
root.render(<App />);

export default App;
