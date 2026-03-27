export default function Features() {
  const data = [
    {
      title: "AI Safety Scoring",
      desc: "Machine learning model analyzes multiple safety factors for every route segment."
    },
    {
      title: "Street Lighting Data",
      desc: "Real-time assessment of lighting conditions along your walking path."
    },
    {
      title: "Crowd Analysis",
      desc: "Evaluates foot traffic and crowd density to recommend safer routes."
    },
    {
      title: "Nearby Safe Points",
      desc: "Identifies police stations, hospitals, and safe places nearby."
    },
    {
      title: "Emergency Alerts",
      desc: "One-tap SOS with instant location sharing to emergency contacts."
    },
    {
      title: "Time-Aware Routes",
      desc: "Safety scores adjust based on time of day for optimal routes."
    }
  ];

  return (
    <div className="features-section">
      <h2>Safety, <span>reimagined</span></h2>
      <p>
        Advanced algorithms combine multiple data sources to keep you on the safest path.
      </p>

      <div className="features-grid">
        {data.map((item, index) => (
          <div className="feature-card" key={index}>
            <div className="icon">🛡️</div>
            <h3>{item.title}</h3>
            <p>{item.desc}</p>
          </div>
        ))}
      </div>
    </div>
  );
}