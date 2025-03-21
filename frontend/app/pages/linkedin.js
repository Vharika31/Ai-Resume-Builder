import { useState } from "react";
import { fetchLinkedInData } from "../utils/api";

export default function LinkedInFetch() {
  const [linkedinId, setLinkedinId] = useState("");
  const [data, setData] = useState(null);

  const handleFetch = async () => {
    const result = await fetchLinkedInData(linkedinId);
    setData(result);
  };

  return (
    <div>
      <h2>Fetch LinkedIn Data</h2>
      <input type="text" placeholder="LinkedIn ID" onChange={(e) => setLinkedinId(e.target.value)} />
      <button onClick={handleFetch}>Fetch</button>
      {data && <pre>{JSON.stringify(data, null, 2)}</pre>}
    </div>
  );
}
