import React, { useState } from "react";
import axios from "axios";

function Dashboard() {
    const [email, setEmail] = useState("");
    const [message, setMessage] = useState("");

    const sendPhishingEmail = async () => {
        try {
            const response = await axios.post("http://127.0.0.1:5000/send-phishing", { email });
            setMessage(response.data.message);
        } catch (error) {
            setMessage("Error sending email");
        }
    };

    return (
        <div>
            <h2>Phishing Simulation Dashboard</h2>
            <input type="email" placeholder="Enter Email" onChange={(e) => setEmail(e.target.value)} />
            <button onClick={sendPhishingEmail}>Send Phishing Email</button>
            {message && <p>{message}</p>}
        </div>
    );
}

export default Dashboard;
