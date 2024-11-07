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
  const routeData = location.state?.routeData || [];

  console.log("Route Data: ", routeData);

  // Flatten the routeData array if it's nested
  const routeDataFlattened = routeData.flat();
  console.log("Route Data Flattened: ", routeDataFlattened);

  return (
    <>
      {/* Title Bar */}
      <div className="bg-teal-500 text-white p-4 font-bold text-2xl text-center">
        GatherGo 集遊
      </div>
      <div className="flex flex-row">
          {/* Map and Destinations Container */}
        {/* Map Component */}
        <div className="flex-1">
        <APIProvider
          mapContainerStyle={{ width: "50%" }}
          apiKey={''} // Replace with your actual Google Maps API key
          onLoad={() => console.log("Maps API has loaded.")}
          libraries={['marker']}
        >
          <Map
            mapContainerStyle={{ height: "400px", width: "100%" }}
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
              const title = destination.name || `Location ${index + 1}`;

              return (
                <Marker
                  key={index}
                  position={{ lat, lng }}
                  title={title}
                  clickable={true}
                  onClick={() => alert(`${title}`)}
                />
              );
            })}
          </Map>
        </APIProvider>
        </div>

        {/* Destinations List */}
        <div className="p-4 flex-1">
          <h2 className="text-2xl font-bold mb-4">Destinations</h2>
          {routeDataFlattened.map((item, index) => {
            const destination = item.destination;
            const name = destination.name || `Destination ${index + 1}`;
            const address = destination.formatted_address || 'Address not available';
            const startTime = item.time?.start || 'N/A';
            const endTime = item.time?.end || 'N/A';

            return (
              <div
                key={index}
                className="border-b border-gray-300 py-4 flex items-start"
              >
                <div className="mr-4">
                  <div className="w-8 h-8 bg-teal-500 text-white rounded-full flex items-center justify-center">
                    {index + 1}
                  </div>
                </div>
                <div>
                  <h3 className="text-xl font-semibold">{name}</h3>
                  <p className="text-gray-600">{address}</p>
                  <p className="text-gray-500">
                    Time: {startTime} - {endTime}
                  </p>
                </div>
              </div>
            );
          })}
        </div>
        </div>
    </>
  );
};

export default Maps;
