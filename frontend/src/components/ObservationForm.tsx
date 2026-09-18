import { FormEvent, useState } from "react";

interface Props {
  onSubmit: (observation: string) => void;
}

export function ObservationForm({ onSubmit }: Props) {
  const [observation, setObservation] = useState("");

  function handleSubmit(event: FormEvent) {
    event.preventDefault();

    if (!observation.trim()) {
      return;
    }

    onSubmit(observation.trim());
  }

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="observation">
        What did you notice?
      </label>

      <textarea
        id="observation"
        value={observation}
        onChange={(event) => setObservation(event.target.value)}
        rows={6}
        autoFocus
      />

      <button type="submit">
        Start Study
      </button>
    </form>
  );
}
