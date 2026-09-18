import { useState } from "react";

import type { Study } from "./api/studies";
import { HomePage } from "./pages/HomePage";
import { StudyPage } from "./pages/StudyPage";

export default function App() {
  const [study, setStudy] = useState<Study | null>(null);

  if (study) {
    return (
      <StudyPage study={study} />
    );
  }

  return (
    <HomePage
      onStudyCreated={setStudy}
      onStudySelected={setStudy}
    />
  );
}
