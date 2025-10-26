# 🤖 JARVIS - Voice-Activated Personal Assistant

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()

<div align="center">
  <img src="image_preview.jpg" alt="JARVIS Voice Assistant" width="600"/>
</div>

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage Instructions](#usage-instructions)
- [Example Commands](#example-commands)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## 🌟 Overview

**JARVIS** (Just A Rather Very Intelligent System) is a sophisticated Python-based voice-activated personal assistant designed to streamline your daily computing tasks. Inspired by the AI assistant from Iron Man, this project leverages cutting-edge speech recognition and text-to-speech technologies to provide an intuitive, hands-free interaction experience.

The assistant can perform a wide range of tasks including web searches, application launching, system control, and information retrieval—all through simple voice commands. Whether you need to quickly search Wikipedia, play your favorite music, or control your system, JARVIS is here to help.

## ✨ Features

### 🎤 Core Capabilities

- **Advanced Voice Recognition**: Utilizes Google Speech Recognition API for accurate command interpretation
- **Natural Text-to-Speech**: Converts responses into natural-sounding speech using pyttsx3 engine
- **Context-Aware Greetings**: Intelligently greets users based on the time of day (morning, afternoon, evening)

### 🌐 Web & Information Services

- **Wikipedia Integration**: Instantly fetch and summarize information from Wikipedia
- **Smart Web Browsing**: Quick access to popular websites:
  - YouTube
  - Google Search
  - Instagram
  - Stack Overflow
  - GitHub
- **Web Search**: Perform custom web searches directly through voice commands

### 🎵 Media & Entertainment

- **Local Music Playback**: Play music from your designated music directory
- **Random Song Selection**: Automatically selects and plays random tracks from your collection

### 💻 System Integration

- **Application Launcher**: Open installed applications (e.g., Visual Studio Code, browsers)
- **Time & Date Inquiry**: Get current time and date information on demand
- **System Control Commands**:
  - Shutdown system
  - Restart computer
  - Sleep mode activation
  - Application termination

### 🛡️ Additional Features

- **Error Handling**: Robust exception handling for uninterrupted operation
- **Command Retry Logic**: Automatically prompts for command repetition on recognition failures
- **Exit Commands**: Multiple exit phrases for convenient shutdown ("exit", "goodbye", "quit")

## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|------------|----------|
| **Language** | Python 3.x | Core programming language |
| **Speech Recognition** | SpeechRecognition | Voice command interpretation |
| **Text-to-Speech** | pyttsx3 | Voice response generation |
| **Information Retrieval** | wikipedia-api | Wikipedia content access |
| **Web Browser Control** | webbrowser | Opening URLs and web searches |
| **System Operations** | os, datetime, random | File system and system control |

## 📥 Installation

### Prerequisites

- **Python 3.6 or higher** installed on your system
- **Microphone** for voice input
- **Speakers/Headphones** for audio output
- **Internet connection** for web-based features

### Step-by-Step Installation Guide

1. **Clone the Repository**
   ```bash
   git clone https://github.com/arpanpramanik2003/jarvis-voice-assistant.git
   cd jarvis-voice-assistant
   ```

2. **Install Required Dependencies**
   ```bash
   pip install pyttsx3 SpeechRecognition wikipedia-api pyaudio
   ```

   **Note**: On Linux/macOS, you may need to install additional audio libraries:
   ```bash
   # For Ubuntu/Debian
   sudo apt-get install python3-pyaudio portaudio19-dev
   
   # For macOS
   brew install portaudio
   ```

3. **Configure Music Directory** (Optional)
   - Update the `music_path` variable in `jarvis_2.0.py` with your music folder path
   - Default: `"D:\\Music"`

4. **Verify Installation**
   ```bash
   python jarvis_2.0.py
   ```

## 🚀 Usage Instructions

### Starting the Assistant

1. Navigate to the project directory
2. Run the main script:
   ```bash
   python jarvis_2.0.py
   ```
3. Wait for the greeting message
4. Start speaking your commands after hearing "How can I help you?"

### Command Structure

Commands should be spoken clearly and can be phrased naturally. JARVIS understands various command formats:

- **Direct Commands**: "Open YouTube"
- **Conversational Phrases**: "Can you search Wikipedia for Python programming"
- **Question Format**: "What time is it?"

### Exiting the Application

Speak any of the following:
- "Exit"
- "Goodbye"
- "Quit"

## 💬 Example Commands

### Information Retrieval
```
"Search Wikipedia for Artificial Intelligence"
"Wikipedia Machine Learning"
```

### Web Navigation
```
"Open YouTube"
"Open Google"
"Open Instagram"
"Open Stack Overflow"
"Open GitHub"
```

### System Operations
```
"What time is it?"
"Tell me the time"
"What's today's date?"
"Shutdown system"
"Restart computer"
"Put the system to sleep"
```

### Media Control
```
"Play music"
"Play a song"
```

### Application Control
```
"Open Visual Studio Code"
"Close Jarvis" or "Exit"
```

## 📁 Project Structure

```
jarvis-voice-assistant/
│
├── jarvis_2.0.py          # Main application file
├── README.md              # Project documentation
├── image_preview.jpg      # Preview image (optional)
└── LICENSE               # License file (if applicable)
```

### Code Organization

- **`speak(text)`**: Converts text to speech output
- **`wishme()`**: Greets user based on time of day
- **`takecommand()`**: Captures and processes voice input
- **`main()`**: Core logic and command routing

## ⚙️ Configuration

### Customizing Voice Properties

Modify the following in `jarvis_2.0.py`:

```python
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Change index for different voice
engine.setProperty('rate', 150)  # Adjust speech rate
```

### Adding Custom Commands

Extend the command logic in the main function:

```python
elif 'your custom command' in query:
    # Your custom action here
    speak("Executing custom command")
```

### Setting Music Directory

```python
music_path = "YOUR_MUSIC_DIRECTORY_PATH"
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the Repository**
2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit Your Changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the Branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Contribution Guidelines

- Follow PEP 8 style guidelines for Python code
- Add comments for complex logic
- Update documentation for new features
- Test thoroughly before submitting

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👏 Acknowledgments

- **Author**: Arpan Pramanik
- **Inspiration**: JARVIS from Marvel's Iron Man
- **Speech Recognition**: Google Speech Recognition API
- **Community**: Thanks to all contributors and the open-source community

### Special Thanks To

- The Python community for excellent libraries
- Contributors to pyttsx3 and SpeechRecognition projects
- All users providing feedback and suggestions

---

<div align="center">
  
  **Made with ❤️ by Arpan Pramanik**
  
  If you found this project helpful, please consider giving it a ⭐️!
  
</div>

## 🐛 Known Issues & Troubleshooting

### Microphone Not Working
- Check system microphone permissions
- Ensure PyAudio is properly installed
- Test microphone with other applications

### Recognition Errors
- Speak clearly and at a moderate pace
- Reduce background noise
- Check internet connection (required for Google Speech Recognition)

### Voice Not Playing
- Verify audio output device
- Check pyttsx3 installation
- Ensure system volume is not muted

## 🔮 Future Enhancements

- [ ] Add support for more languages
- [ ] Implement calendar and reminder features
- [ ] Email integration
- [ ] Weather information retrieval
- [ ] Smart home device control
- [ ] Machine learning for better command understanding
- [ ] GUI interface option
- [ ] Mobile application integration

---

**Version**: 2.0  
**Last Updated**: October 2025  
**Status**: Active Development
