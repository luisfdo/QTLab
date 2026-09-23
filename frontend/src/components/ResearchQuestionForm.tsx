import { useState } from "react";

import type { Study } from "../api/studies";
import { defineResearchQuestion } from "../api/studies";

interface Props {
  study: Study;
  onStudyUpdated: (study: Study) => void;
}

export function ResearchQuestionForm({
  study,
  onStudyUpdated,
}: Props) {
  const [text, setText] = useState(
    study.research_question ?? "",
  );

  const [saving, setSaving] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function handleSubmit(
    event: React.FormEvent,
  ) {
    event.preventDefault();

    if (!text.trim()) {
      return;
    }

    setSaving(true);
    setError(null);

    try {
      const updatedStudy = await defineResearchQuestion(
        study.id,
        text.trim(),
      );

      onStudyUpdated(updatedStudy);
    } catch {
      setError("Failed to save research question.");
    } finally {
      setSaving(false);
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="research-question">
        What do you want to investigate?
      </label>

      <textarea
        id="research-question"
        value={text}
        onChange={(event) => setText(event.target.value)}
        rows={4}
        disabled={saving}
      />

      <button
        type="submit"
        disabled={saving || !text.trim()}
      >
        {saving ? "Saving..." : "Define research question"}
      </button>

      {error && <p>{error}</p>}
    </form>
  );
}