import { MapContainer, TileLayer, Polyline, Marker } from "react-leaflet";

export default function MapView({ route }) {
  return (
    <MapContainer center={[28.61, 77.20]} zoom={12} className="map">
      <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />

      {route.length > 0 && (
        <Polyline positions={route.map(p => [p.lat, p.lon])} />
      )}

      {route.length > 0 && (
        <>
          <Marker position={[route[0].lat, route[0].lon]} />
          <Marker position={[route[route.length - 1].lat, route[route.length - 1].lon]} />
        </>
      )}
    </MapContainer>
  );
}