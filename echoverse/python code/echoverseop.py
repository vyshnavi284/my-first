import os
from typing import List, Dict

# Simulated AI voice library
AI_VOICES = [
    {"id": 1, "name": "Emma", "gender": "Female", "age": "Adult", "accent": "British", "tone": "Cheerful"},
    {"id": 2, "name": "Liam", "gender": "Male", "age": "Adult", "accent": "American", "tone": "Serious"},
    {"id": 3, "name": "Aarav", "gender": "Male", "age": "Adult", "accent": "Indian", "tone": "Dramatic"},
    # Add more voices as needed
]

class EchoVerseAI:
    def __init__(self):
        self.projects = {}

    def create_project(self, project_name: str):
        if project_name in self.projects:
            print(f"Project '{project_name}' already exists.")
            return
        self.projects[project_name] = {
            "manuscript": None,
            "chapters": [],
            "character_voices": {},
            "audio_files": []
        }
        print(f"Project '{project_name}' created.")

    def import_manuscript(self, project_name: str, manuscript_text: str):
        # Simple chapter splitting by "Chapter" keyword
        chapters = [ch.strip() for ch in manuscript_text.split("Chapter") if ch.strip()]
        self.projects[project_name]["manuscript"] = manuscript_text
        self.projects[project_name]["chapters"] = chapters
        print(f"Imported manuscript with {len(chapters)} chapters into project '{project_name}'.")

    def list_voices(self, filters: Dict = None):
        voices = AI_VOICES
        if filters:
            for key, value in filters.items():
                voices = [v for v in voices if v.get(key, "").lower() == value.lower()]
        print("Available voices:")
        for v in voices:
            print(f"ID: {v['id']}, Name: {v['name']}, Gender: {v['gender']}, Accent: {v['accent']}, Tone: {v['tone']}")
        return voices

    def assign_voice_to_character(self, project_name: str, character_name: str, voice_id: int):
        voice = next((v for v in AI_VOICES if v["id"] == voice_id), None)
        if not voice:
            print(f"Voice ID {voice_id} not found.")
            return
        self.projects[project_name]["character_voices"][character_name] = voice
        print(f"Assigned voice '{voice['name']}' to character '{character_name}' in project '{project_name}'.")

    def generate_audio(self, project_name: str):
        # Simulate TTS generation per chapter
        chapters = self.projects[project_name]["chapters"]
        audio_files = []
        for i, chapter in enumerate(chapters, start=1):
            filename = f"{project_name}_chapter_{i}.mp3"
            # Simulate audio generation
            print(f"Generating audio for Chapter {i}...")
            # In real app, call TTS API here with character voices and text
            audio_files.append(filename)
        self.projects[project_name]["audio_files"] = audio_files
        print(f"Generated {len(audio_files)} audio files for project '{project_name}'.")

    def export_audio(self, project_name: str, export_format: str = "mp3"):
        audio_files = self.projects[project_name]["audio_files"]
        if not audio_files:
            print("No audio files to export. Please generate audio first.")
            return
        export_folder = f"{project_name}_export"
        os.makedirs(export_folder, exist_ok=True)
        for file in audio_files:
            # Simulate export by creating empty files
            filepath = os.path.join(export_folder, file)
            with open(filepath, "w") as f:
                f.write(f"Simulated audio content for {file}")
        print(f"Exported audio files to folder '{export_folder}' in {export_format} format.")

# Example usage
if __name__ == "__main__":
    echo = EchoVerseAI()
    echo.create_project("MyFirstAudiobook")

    sample_manuscript = """
    Chapter 1
    This is the beginning of the story. Alice said, "Hello there!"
    Chapter 2
    The adventure continues. Bob replied, "Let's go!"
    """

    echo.import_manuscript("MyFirstAudiobook", sample_manuscript)
    echo.list_voices(filters={"accent": "British"})
    echo.assign_voice_to_character("MyFirstAudiobook", "Alice", 1)
    echo.assign_voice_to_character("MyFirstAudiobook", "Bob", 2)
    echo.generate_audio("MyFirstAudiobook")
    echo.export_audio("MyFirstAudiobook")