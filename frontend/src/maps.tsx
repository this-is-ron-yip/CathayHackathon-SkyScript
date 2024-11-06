import React from "react";
import ReactDOM from "react-dom/client";
import "../index.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import {
  APIProvider,
  Map,
  MapCameraChangedEvent,
} from "@vis.gl/react-google-maps";
import exp from "constants";

const Maps = () => {
    return(
        <APIProvider
            apiKey={''}
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
};

export default Maps;

