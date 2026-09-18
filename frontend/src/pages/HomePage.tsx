import { useEffect, useState } from "react";

import {
  createStudy,
  listStudies,
} from "../api/studies";
import type { Study } from "../api/studies";
import { ObservationForm } from "../components/ObservationForm";

interface Props {
  onStudyCreated: (study: Study) => void;
  onStudySelected: (study: Study) => void;
}

export function HomePage({
  onStudyCreated,
  onStudySelected,
}: Props) {
  const [studies, setStudies] = useState<Study[]>([]);

  useEffect(() => {
    listStudies().then(setStudies);
  }, []);

  async function handleCreate(observation: string) {
    const study = await createStudy(observation);

    setStudies((current) => [study, ...current]);
    onStudyCreated(study);
  }

  return (
    <main>
      <h1>QTLab</h1>

      <p>Research begins with curiosity.</p>

      <ObservationForm onSubmit={handleCreate} />

      {studies.length > 0 && (
        <section>
          <h2>Studies</h2>

          {studies.map((study) => (
            <button
              key={study.id}
              onClick={() => onStudySelected(study)}
            >
              {study.observation}
            </button>
          ))}
        </section>
      )}
    </main>
  );
}
