import type { Study } from "../api/studies";

interface Props {
  study: Study;
}

export function StudyPage({ study }: Props) {
  return (
    <main>
      <h1>Study</h1>

      <p>{formatStatus(study.status)}</p>

      <section>
        <h2>Observation</h2>
        <p>{study.observation}</p>
      </section>

      <section>
        <h2>Timeline</h2>

        <ol>
          {study.timeline.map((event) => (
            <li key={`${event.type}-${event.occurred_at}`}>
              <strong>{formatEventType(event.type)}</strong>
              <time>
                {new Date(event.occurred_at).toLocaleString()}
              </time>
            </li>
          ))}
        </ol>
      </section>
    </main>
  );
}

function formatStatus(status: string): string {
  return status
    .replaceAll("_", " ")
    .replace(/\b\w/g, (character) => character.toUpperCase());
}

function formatEventType(type: string): string {
  return type
    .replace(/([A-Z])/g, " $1")
    .trim();
}
