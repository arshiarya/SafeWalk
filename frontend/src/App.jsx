// import { useState } from "react";
// import { MapContainer, TileLayer, Polyline, Marker } from "react-leaflet";
// import "leaflet/dist/leaflet.css";
// import "./App.css";

// function App() {
//   const [startLat, setStartLat] = useState("");
//   const [startLon, setStartLon] = useState("");
//   const [endLat, setEndLat] = useState("");
//   const [endLon, setEndLon] = useState("");
//   const [route, setRoute] = useState([]);

//   const handleRoute = () => {
//     // Dummy route for now
//     const dummy = [
//       { lat: parseFloat(startLat), lon: parseFloat(startLon) },
//       { lat: 28.55, lon: 77.17 },
//       { lat: 28.57, lon: 77.18 },
//       { lat: parseFloat(endLat), lon: parseFloat(endLon) }
//     ];

//     setRoute(dummy);
//   };

//   return (
//     <div className="container">
//       <h1>🛡️ SafeWalk AI</h1>

//       <div className="card">
//         <div className="inputs">
//           <input placeholder="Start Latitude" onChange={(e) => setStartLat(e.target.value)} />
//           <input placeholder="Start Longitude" onChange={(e) => setStartLon(e.target.value)} />
//         </div>

//         <div className="inputs">
//           <input placeholder="End Latitude" onChange={(e) => setEndLat(e.target.value)} />
//           <input placeholder="End Longitude" onChange={(e) => setEndLon(e.target.value)} />
//         </div>

//         <button onClick={handleRoute}>Find Safest Route</button>
//       </div>

//       <MapContainer center={[28.61, 77.20]} zoom={12} className="map">
//         <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />

//         {route.length > 0 && (
//           <Polyline positions={route.map(p => [p.lat, p.lon])} />
//         )}

//         {route.length > 0 && (
//           <>
//             <Marker position={[route[0].lat, route[0].lon]} />
//             <Marker position={[route[route.length - 1].lat, route[route.length - 1].lon]} />
//           </>
//         )}
//       </MapContainer>
//     </div>
//   );
// }

// export default App;

import { useState } from "react";
import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import RoutePlanner from "./components/RoutePlanner";
import MapView from "./components/MapView";
import "leaflet/dist/leaflet.css";
import Features from "./components/Features";
import "./App.css";


function App() {
  const [route, setRoute] = useState([]);

  return (
    <>
      <Navbar />
      <Hero />
      <RoutePlanner setRoute={setRoute} />
      <MapView route={route} />

      {/* ADD THIS 👇 */}
      <Features />
    </>
  );
}
export default App;