import React from "react";
import { useLocation } from "react-router-dom";
import "../index.css";
import {
  APIProvider,
  Map,
  MapCameraChangedEvent,
  Marker
} from "@vis.gl/react-google-maps";

const Maps = () => {
  const location = useLocation();
  const routeData = location.state?.routeData;

  console.log("Route Data: ", routeData);

  const routeDataFlattened = routeData.flat();
  console.log("Route Data Flattened: ", routeDataFlattened);

  // You can now use routeData to display markers, plans, etc.

  return (
    <APIProvider
      apiKey={''}  // Make sure to insert your actual API key here
      onLoad={() => console.log("Maps API has loaded.")}
      libraries={['marker']}
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
        gestureHandling={"greedy"}
        disableDefaultUI
      >
        {routeDataFlattened.map((item, index) => {
            const destination = item.destination;
            const position = destination?.geometry?.location;
        
            if (!position) {
                return null;
            }
        
            const lat = position.lat;
            const lng = position.lng;
            const title = destination.name;

            return (
                <Marker
                    key={index}
                    position={{ lat, lng }}
                    title={title}
                    clickable={true}
                    onClick={() => alert(`Marker ${index + 1} clicked!`)}
                />
            );
        })}
        {/* Use routeData here, e.g., to display markers */}
      </Map>
    </APIProvider>
  );
};

export default Maps;
