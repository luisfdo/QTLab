import { useState } from "react";
import { defineResearchQuestion } from "../api/studies";
import type { Study } from "../api/studies";

interface StudyDetailsProps {
  study: Study;
  onStudyUpdated: (study: Study) => void;
}

export function StudyDetails({
  study,
  onStudyUpdated,
}: StudyDetailsProps) {
  const [researchQuestion, setResearchQuestion] = useState(
    study.research_question ?? "",
  );

  const [saving, setSaving] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function handleDefineResearchQuestion() {
    setSaving(true);
    setError(null);

    try {
      const updatedStudy = await defineResearchQuestion(
        study.id,
        researchQuestion,
      );

      onStudyUpdated(updatedStudy);
    } catch {
      setError("Could not save research question.");
    } finally {
      setSaving(false);
    }
  }

  return (
    <section>
      <h2>Research question</h2>

      <textarea
        value={researchQuestion}
        onChange={(event) => setResearchQuestion(event.target.value)}
        rows={4}
        placeholder="What do you want to investigate?"
      />

      <button
        onClick={handleDefineResearchQuestion}
        disabled={saving || !researchQuestion.trim()}
      >
        {saving ? "Saving..." : "Define research question"}
      </button>

      {error && <p>{error}</p>}
    </section>
  );
}