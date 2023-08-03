# SongToAI

SongToAI is a project that takes a song name as input, retrieves its lyrics, and generates AI-generated images for each line of the song. The generated images are saved in separate directories, making it easy to explore and share the unique artwork created for each line.

## How It Works

1. **Input:** Run the program and provide the name of the song you want to explore.

2. **Lyrics Retrieval:** The program uses the Genius API to search for the lyrics of the given song. It then processes the lyrics to remove unnecessary content and prepares the lines for AI generation.

3. **Image Generation:** For each line of the song, the program utilizes the OpenAI API to generate four AI images related to the text. These images will capture the artistic interpretation of the song's lines.

4. **Image Storage:** The generated images are saved in a new directory named after the song, replacing spaces with underscores to ensure a valid path. Each line of the song has its own directory containing the four corresponding AI-generated images.

## Setup

To run the SongToAI project, you need to obtain API keys from both OpenAI and Genius. Place your API keys in a JSON file named `secret.json` with the following structure:

```json
{
  "OPENAI_KEY": "your_openai_api_key",
  "GENIUS_KEY": "your_genius_api_key"
}
```
## Ensure you have the required libraries installed:

```pip install openai lyricsgenius requests```

# Usage

1. Clone the repository: git clone https://github.com/maikerudev/SongToAI.git
2. Navigate to the project directory: cd SongToAI
3. Run the script: python main.py
4. Follow the prompts to enter the song name and artist.

The program will retrieve the lyrics, generate AI images for each line, and save them in the appropriate directories.
