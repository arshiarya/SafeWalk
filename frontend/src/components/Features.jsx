export default function Features() {
  const data = [
   {
    title: "AI Safety Scoring",
    desc: "Machine learning model analyzes multiple safety factors.",
    icon: "https://cdn-icons-png.flaticon.com/512/3064/3064197.png"
  },
  {
    title: "Street Lighting Data",
    desc: "Real-time lighting conditions.",
    icon: "https://cdn-icons-png.flaticon.com/512/1046/1046784.png"
  },
  {
    title: "Crowd Analysis",
    desc: "Analyzes crowd density.",
    icon: "https://cdn-icons-png.flaticon.com/512/1077/1077012.png"
  },
  {
    title: "Nearby Safe Points",
    desc: "Finds nearby safe places.",
    icon: "https://cdn-icons-png.flaticon.com/512/684/684908.png"
  },
  {
    title: "Emergency Alerts",
    desc: "SOS alerts system.",
    icon: "https://cdn-icons-png.flaticon.com/512/1827/1827392.png"
  },
  {
    title: "Time-Aware Routes",
    desc: "Time-based safety.",
    icon: "https://cdn-icons-png.flaticon.com/512/2088/2088617.png"
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
           <div className="icon">
  <img src={item.icon} alt="icon" />
</div>
            <h3>{item.title}</h3>
            <p>{item.desc}</p>
          </div>
        ))}
      </div>
    </div>
  );
}