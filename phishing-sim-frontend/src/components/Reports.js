import React, { useState, useEffect } from "react";
import axios from "axios";

function Reports() {
    const [users, setUsers] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            const response = await axios.get("http://127.0.0.1:5000/get-tracking");
            setUsers(response.data);
        };
        fetchData();
    }, []);

    return (
        <div>
            <h2>User Actions Report</h2>
            {users.map((user, index) => (
                <div key={index}>
                    <p>{user.email} - Clicked: {user.clicked ? "✅" : "❌"} - Submitted: {user.submitted_data ? "✅" : "❌"}</p>
                </div>
            ))}
        </div>
    );
}

export default Reports;
