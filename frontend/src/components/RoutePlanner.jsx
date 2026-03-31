// import { useState } from "react";

// export default function RoutePlanner({ setRoute }) {
//   const [startLat, setStartLat] = useState("");
//   const [startLon, setStartLon] = useState("");
//   const [endLat, setEndLat] = useState("");
//   const [endLon, setEndLon] = useState("");

//   const handleRoute = () => {
//     const dummy = [
//       { lat: parseFloat(startLat), lon: parseFloat(startLon) },
//       { lat: 28.55, lon: 77.17 },
//       { lat: 28.57, lon: 77.18 },
//       { lat: parseFloat(endLat), lon: parseFloat(endLon) }
//     ];
//     setRoute(dummy);
//   };

//   return (
//     <div className="planner">
//       <h2>Plan Your Route</h2>

//       <input placeholder="Start Latitude" onChange={(e) => setStartLat(e.target.value)} />
//       <input placeholder="Start Longitude" onChange={(e) => setStartLon(e.target.value)} />
//       <input placeholder="End Latitude" onChange={(e) => setEndLat(e.target.value)} />
//       <input placeholder="End Longitude" onChange={(e) => setEndLon(e.target.value)} />

//       <button onClick={handleRoute}>Find Safest Route</button>
//     </div>
//   );
// }
// import { useState } from "react";
// import axios from "axios"; // ✅ ADD THIS

// export default function RoutePlanner({ setRoute }) {
//   const [startLat, setStartLat] = useState("");
//   const [startLon, setStartLon] = useState("");
//   const [endLat, setEndLat] = useState("");
//   const [endLon, setEndLon] = useState("");

//   const handleRoute = async () => {
//     try {
//       const res = await axios.get("http://localhost:8000/route", {
//         params: {
//           start_lat: parseFloat(startLat),
//           start_lon: parseFloat(startLon),
//           end_lat: parseFloat(endLat),
//           end_lon: parseFloat(endLon),
//         },
//       });

//       // ✅ Use safest route from backend
//       setRoute(res.data.safest_route);

//     } catch (err) {
//       console.error(err);
//       alert("Backend not working!");

//       // 🔁 fallback (optional but good)
//       const dummy = [
//         { lat: parseFloat(startLat), lon: parseFloat(startLon) },
//         { lat: 28.55, lon: 77.17 },
//         { lat: 28.57, lon: 77.18 },
//         { lat: parseFloat(endLat), lon: parseFloat(endLon) }
//       ];
//       setRoute(dummy);
//     }
//   };

//   return (
//     <div className="planner">
//       <h2>Plan Your Route</h2>

//       <input
//         placeholder="Start Latitude"
//         onChange={(e) => setStartLat(e.target.value)}
//       />
//       <input
//         placeholder="Start Longitude"
//         onChange={(e) => setStartLon(e.target.value)}
//       />
//       <input
//         placeholder="End Latitude"
//         onChange={(e) => setEndLat(e.target.value)}
//       />
//       <input
//         placeholder="End Longitude"
//         onChange={(e) => setEndLon(e.target.value)}
//       />

//       <button onClick={handleRoute}>
//         Find Safest Route
//       </button>
//     </div>
//   );
// }

import { useState } from "react";
import axios from "axios";

export default function RoutePlanner({ setRoute }) {
  const [startPlace, setStartPlace] = useState("");
  const [endPlace, setEndPlace] = useState("");

  // 🔥 Convert place → coordinates
  const getCoordinates = async (place) => {
    const res = await fetch(
      `https://nominatim.openstreetmap.org/search?format=json&q=${place}`
    );
    const data = await res.json();

    if (data.length === 0) {
      throw new Error("Location not found");
    }

    return {
      lat: parseFloat(data[0].lat),
      lon: parseFloat(data[0].lon),
    };
  };

  const handleRoute = async () => {
    try {
      // 🔥 Step 1: Convert names → coords
      const start = await getCoordinates(startPlace);
      const end = await getCoordinates(endPlace);

      // 🔥 Step 2: Call backend (same as before)
      const res = await axios.get("http://localhost:8000/route", {
        params: {
          start_lat: start.lat,
          start_lon: start.lon,
          end_lat: end.lat,
          end_lon: end.lon,
        },
      });

      setRoute(res.data.safest_route);

    } catch (err) {
      console.error(err);
      alert("Location not found or backend error!");
    }
  };

  return (
    <div className="planner">
      <h2>Plan Your Route</h2>

      {/* ✅ NEW INPUTS */}
      <input
        placeholder="Enter Start Location (e.g. JNU)"
        onChange={(e) => setStartPlace(e.target.value)}
      />

      <input
        placeholder="Enter Destination (e.g. India Gate)"
        onChange={(e) => setEndPlace(e.target.value)}
      />

      <button onClick={handleRoute}>
        Find Safest Route
      </button>
    </div>
  );
}