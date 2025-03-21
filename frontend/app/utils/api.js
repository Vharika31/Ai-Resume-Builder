export const fetchLinkedInData = async (linkedinId) => {
    const response = await fetch("/api/linkedin", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ linkedin_id: linkedinId }),
    });
    return response.json();
  };
  
  export const getRecommendations = async (skills, experience) => {
    const response = await fetch("/api/recommendations", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ skills, experience }),
    });
    return response.json();
  };
  
  export const generateResume = async (userData) => {
    const response = await fetch("/api/resume/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(userData),
    });
    return response.json();
  };

  export async function fetchUserResumes() {
    try {
      const response = await fetch("/api/resumes");
      return await response.json();
    } catch (error) {
      console.error("Error fetching resumes:", error);
      return [];
    }
  }
  
  