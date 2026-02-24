# AI Voice Assistant Using Python

This project implements a command-line based AI Voice Assistant using the Python programming language. The objective of the project is to demonstrate the use of speech recognition, text-to-speech conversion, API integration, and automation through voice commands. The assistant interacts with the user through spoken language, processes voice commands, and performs various tasks accordingly.

The assistant uses a microphone to capture the user’s voice input and converts the speech into text using the SpeechRecognition library. Based on the recognized command, the assistant executes predefined actions such as opening websites, telling the current time and date, searching Wikipedia, telling jokes, performing basic calculations, fetching weather information, and opening system applications like Notepad. The responses are provided both as text output in the terminal and as spoken audio using the pyttsx3 text-to-speech engine.

For weather information, the project integrates the OpenWeatherMap API, allowing the assistant to fetch real-time weather data for a specified city. The assistant also uses external libraries such as Wikipedia for information retrieval and PyJokes for generating jokes. Web automation is handled using the webbrowser module, while system-level operations are performed using the os module.

The entire application runs in a continuous loop, enabling the assistant to listen for commands until the user explicitly asks it to stop or exit. The project does not require a graphical user interface and runs completely through the terminal, making it lightweight and easy to execute on systems with Python installed.

To run this project, Python must be installed along with the required libraries: speechrecognition, pyttsx3, wikipedia, pyjokes, and requests. A working microphone and an active internet connection are required for voice recognition, online searches, and weather updates. The OpenWeatherMap API key must be added in the source code to enable weather functionality. The program can be executed using the command `python assistant.py`.

This project is suitable for academic submissions and internships as it demonstrates practical knowledge of Python, voice-based interaction, API usage, and automation. It can be further enhanced by adding features such as improved error handling, support for more commands, integration with desktop applications, or a graphical user interface.

Author: Amrutha Reddy
