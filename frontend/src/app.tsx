import React from "react";
import ReactDOM from "react-dom/client";
import "../index.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Chat from "./chat";
import Maps from "./maps";

const App = () => (

  <BrowserRouter>
    <Routes>
      <Route path="/chat" element={<Chat />} />
      <Route path="/maps" element={<Maps />} />
    </Routes>
  </BrowserRouter>

);

const root = ReactDOM.createRoot(document.getElementById("app"));
root.render(<App />);

export default App;
