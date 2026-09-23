export interface TimelineEvent {
  type: string;
  occurred_at: string;
}

export interface Study {
  id: string;
  observation: string;
  research_question: string | null;
  status: string;
  created_at: string;
  updated_at: string;
  timeline: TimelineEvent[];
}

const API_URL = "http://localhost:8080";

export async function createStudy(
  observation: string,
): Promise<Study> {
  const response = await fetch(`${API_URL}/studies`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ observation }),
  });

  if (!response.ok) {
    throw new Error("Failed to create study");
  }

  const { id } = await response.json();

  return getStudy(id);
}

export async function getStudy(id: string): Promise<Study> {
  const response = await fetch(`${API_URL}/studies/${id}`);

  if (!response.ok) {
    throw new Error("Failed to load study");
  }

  return response.json();
}

export async function listStudies(): Promise<Study[]> {
  const response = await fetch(`${API_URL}/studies`);

  if (!response.ok) {
    throw new Error("Failed to load studies");
  }

  return response.json();
}

export async function defineResearchQuestion(id: string, text: string): Promise<Study> {
  const response = await fetch(`${API_URL}/studies/${id}/research-question`,
    {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text }),
    },
  );

  if (!response.ok) {
    throw new Error("Failed to define research question");
  }

  return response.json();
}
