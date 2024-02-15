# Interactive Voice-Enabled Text Interaction Project

This project demonstrates an innovative approach to interacting with text documents using voice commands and receiving responses in audio format, powered by AI. It integrates a range of technologies and libraries to create a seamless user experience. Below is an overview of the tech stack, languages, and libraries utilized across two main components of the project.

### Sample Audio

Listen to the sample output:

<audio controls>
  <source src="https://github.com/PeterP22/LLM-RAG-DOC-CHATTER/raw/main/foxy.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>


### Output Screenshot

![Output Screenshot](https://github.com/PeterP22/LLM-RAG-DOC-CHATTER/raw/main/output%20screenshot.png)


## Project Components

The project is divided into two main notebooks:

1. **Chroma Notebook**: Focuses on processing the text file, interacting with it through OpenAI, and receiving audio responses.
2. **Local RAG Notebook**: Enhances the interaction by leveraging local models for generating responses and converting them into audio.

## Technologies and Libraries Used

### Languages

- **Python**: The primary programming language used for both notebooks.

### Chroma Notebook Libraries

- **OpenAI Libraries**: `openai`, `ChatOpenAI`, `OpenAIEmbeddings` for interfacing with OpenAI's API for processing and generating text responses.
- **Audio Processing**: `pydub`, `gTTS` (Google Text-to-Speech), `elevenlabs` for audio file manipulation and generating speech from text.
- **Utility and Data Management**: `os`, `chromadb` for file and database operations.
- **Text Processing**: `RecursiveCharacterTextSplitter`, `unstructured` for handling and structuring text data.
- **LangChain**: `langchain` for leveraging language models in a chain of operations.
- **Miscellaneous**: `tiktoken`, `DirectoryLoader`, `Chroma`, `Generate`, `load_qa_chain`, `set_api_key`, `Audio,` for various other functionalities including setting up the environment, loading data, and initializing models.

### Local RAG Notebook Libraries

- **Audio and Voice Processing**: `whisper` for voice recognition, `sounddevice` for capturing audio input, `gradio` for creating a web interface for the application.
- **Text and Data Processing**: `RecursiveCharacterTextSplitter`, `FAISS` (Facebook AI Similarity Search) for efficient similarity search in large datasets.
- **OpenAI Libraries**: Similar to the Chroma notebook, `OpenAIEmbeddings`, `langchain`, and direct usage of `OpenAI`'s API.
- **Utility and Management**: `os`, `time`, `DirectoryLoader`, along with the use of a git repository (`git+https://github.com/openai/whisper.git`) for installing the Whisper library.

## Conclusion

This project showcases the power of integrating various AI and machine learning libraries to create a voice-enabled text interaction system. By leveraging OpenAI's API, audio processing libraries, and custom data management solutions, it provides a unique way to interact with text documents audibly.
