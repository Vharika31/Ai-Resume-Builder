import { useState } from "react";
import { generateResume } from "../utils/api";

export default function ResumeGenerator() {
  const [resume, setResume] = useState(null);
  const [userData, setUserData] = useState({ name: "", experience: "", skills: "" });

  const handleGenerate = async () => {
    const result = await generateResume(userData);
    setResume(result.resume);
  };

  return (
    <div>
      <h2>Generate AI-Powered Resume</h2>
      <input type="text" placeholder="Name" onChange={(e) => setUserData({ ...userData, name: e.target.value })} />
      <input type="text" placeholder="Experience" onChange={(e) => setUserData({ ...userData, experience: e.target.value })} />
      <input type="text" placeholder="Skills (comma separated)" onChange={(e) => setUserData({ ...userData, skills: e.target.value.split(",") })} />
      <button onClick={handleGenerate}>Generate</button>
      {resume && <pre>{resume}</pre>}
    </div>
  );
}
