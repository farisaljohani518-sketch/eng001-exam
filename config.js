// =========================================================================
// ENG001 Platform Configuration & Audio Settings
// =========================================================================
const APP_CONFIG = {
  // Course & Assessment Info
  syllabus: {
    course: "ENG001 - English I",
    scope: "Quiz 1",
    units: "Units 3, 4, 5",
    quizDate: "2026-09-27",
    totalQuestions: 70
  },

  // ElevenLabs Voice Configuration
  elevenlabs: {
    // API Key provided by user
    apiKey: "sk_5c26d519055085833ff478d1f2d178ad45daf979e9dd7b3d",

    // Voice ID: You can easily change this anytime without modifying script.js
    // Default: Rachel (Clear, natural academic female instructor)
    // Alternative Male: "pNInz6obpgDQGcFmaJgB" (Adam)
    voiceId: "21m00Tcm4TlvDq8ikWAM",

    // Studio Model & Settings for Academic Realism
    modelId: "eleven_multilingual_v2",
    voiceSettings: {
      stability: 0.48,          // Natural human variance
      similarity_boost: 0.82,   // High clarity & vocal consistency
      style: 0.20,              // Natural inflection and expressive cadence
      use_speaker_boost: true   // Richness and presence
    },

    outputFormat: "mp3_44100_128"
  },

  // Listening Exam Rules
  listening: {
    maxAllowedPlays: 2,         // Strict exam rule: 2 plays maximum
    audioFolder: "audio"        // Folder containing pre-rendered track1.mp3, track2.mp3
  }
};
