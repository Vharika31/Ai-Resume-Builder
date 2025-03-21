import { useState, useEffect } from "react";
import Navbar from "../components/Navbar";
import { fetchUserResumes } from "../utils/api";

export default function Dashboard() {
  const [resumes, setResumes] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadResumes() {
      const userResumes = await fetchUserResumes();
      setResumes(userResumes);
      setLoading(false);
    }
    loadResumes();
  }, []);

  return (
    <div className="min-h-screen bg-gray-100">
      <Navbar />
      <div className="max-w-4xl mx-auto py-10">
        <h2 className="text-3xl font-semibold text-gray-900 mb-4">Your Resumes</h2>
        <button className="bg-green-600 text-white px-4 py-2 rounded-lg mb-6 hover:bg-green-700">
          Generate New Resume
        </button>
        {loading ? (
          <p>Loading...</p>
        ) : resumes.length > 0 ? (
          <ul className="bg-white p-4 rounded-lg shadow-md">
            {resumes.map((resume, index) => (
              <li key={index} className="border-b last:border-none p-2">
                <span className="font-semibold">{resume.title}</span> - {resume.date}
              </li>
            ))}
          </ul>
        ) : (
          <p>No resumes found. Generate a new one!</p>
        )}
      </div>
    </div>
  );
}
