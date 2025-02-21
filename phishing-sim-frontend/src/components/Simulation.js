import React, { useState } from "react";

const Simulation = () => {
  const [email, setEmail] = useState("");

  const startSimulation = async () => {
    const token = localStorage.getItem("token");
    if (!token) {
      alert("Please log in first");
      return;
    }

    const response = await fetch("http://127.0.0.1:5000/simulate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${token}`,
      },
      body: JSON.stringify({ email }),
    });

    const data = await response.json();
    alert(data.message);
  };

  return (
    <div>
      <h2>Start Phishing Simulation</h2>
      <input type="email" placeholder="Target Email" onChange={(e) => setEmail(e.target.value)} />
      <button onClick={startSimulation}>Send Phishing Email</button>
    </div>
  );
};

export default Simulation;
