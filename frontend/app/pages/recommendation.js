import { useState } from "react";
import { getRecommendations } from "../utils/api";

export default function AIRecommendations() {
  const [data, setData] = useState(null);
  const [skills, setSkills] = useState("");
  const [experience, setExperience] = useState("");

  const handleFetch = async () => {
    const result = await getRecommendations(skills.split(","), experience);
    setData(result);
  };

  return (
    <div>
      <h2>AI Job & Skill Recommendations</h2>
      <input type="text" placeholder="Skills (comma separated)" onChange={(e) => setSkills(e.target.value)} />
      <input type="text" placeholder="Experience (years)" onChange={(e) => setExperience(e.target.value)} />
      <button onClick={handleFetch}>Get Recommendations</button>
      {data && <pre>{JSON.stringify(data, null, 2)}</pre>}
    </div>
  );
}
