# Video Summarizer

Video Summarizer is a Django web application that allows users to upload video files, transcribe the audio using AssemblyAI, and generate useful notes from the transcription using Gemini. Users can sign up, log in, save their notes, and view them later.

## Features

- User authentication (sign up, log in)
- Video file upload
- Audio transcription using AssemblyAI
- Note generation from transcription using Gemini
- Save and view notes
- User-friendly interface

## Technologies Used

- Django (Python web framework)
- AssemblyAI (Speech-to-Text API)
- Gemini (Text Summarization API)
- HTML, CSS, JavaScript (Front-end)
- PostgreSQL (Database hosted on fl0.com)

## Installation

1. Clone the repository:

```
git clone https://github.com/eshanpandey/Video_Summarizer.git
```

2. Navigate to the project directory:

```
cd video-summarizer
```

3. Create a virtual environment and activate it:

```
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```

4. Install the required dependencies:

```
pip install -r requirements.txt
```

5. Set up the necessary environment variables for AssemblyAI and Gemini API keys, as well as the PostgreSQL database connection details (hosted on fl0.com).

6. Run the Django development server:

```
python manage.py runserver
```

7. Open your web browser and navigate to `http://localhost:8000` to access the Video Summarizer app.

## Usage

1. Sign up for a new account or log in with your existing credentials.
2. Click the "Upload Video" button and select a video file from your local machine.
3. Wait for the video to be processed. The audio will be transcribed using AssemblyAI, and the transcription will be summarized into useful notes using Gemini.
4. View the generated notes and optionally save them for future reference.
5. Access your saved notes by clicking the "Saved Notes" link in the navigation menu.

## Use Cases

- **Educational Purposes**: Students and educators can utilize the Video Summarizer to quickly generate summarized notes from lengthy educational videos or lectures. This can help in studying efficiently by condensing the key points and concepts covered in the video.

- **Professional Research**: Professionals working in fields such as market research, journalism, or academia can use the Video Summarizer to extract essential information from interviews, conferences, or research presentations. This allows them to save time and focus on analyzing the extracted insights.

- **Content Creation**: Content creators, including YouTubers, podcasters, and bloggers, can leverage the Video Summarizer to generate summaries of their own videos or podcasts. These summaries can be used as additional content for social media posts, newsletters, or as teaser snippets to attract viewers.

- **Legal and Compliance**: Legal professionals can utilize the Video Summarizer to extract key points from legal proceedings, depositions, or court hearings. This can aid in preparing briefs, summaries, or reports for clients or internal use.

- **Personal Productivity**: Individuals can use the Video Summarizer to efficiently consume online courses, webinars, or instructional videos by generating summarized notes. This enables them to grasp the main ideas without having to watch the entire video, thus saving time and increasing productivity.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [AssemblyAI](https://www.assemblyai.com/) for their Speech-to-Text API
- [Gemini](https://www.gemini.com/) for their Text Summarization API
- [Django](https://www.djangoproject.com/) for the web framework