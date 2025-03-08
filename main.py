import os
import speech_recognition as sr
import pyttsx3

class AizaAssistant:
    def __init__(self):
        self.commands = {
            "hello": self.greet,
            "bye": self.farewell,
            "what's your name": self.introduce,
            "how are you": self.how_are_you,
            "can you listen to me": self.listen_command,
        }
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # Speed of speech

    def greet(self):
        return "Hello! How can I assist you today?"

    def farewell(self):
        return "Goodbye! Have a great day!"

    def introduce(self):
        return "My name is Aiza, your AI Assistant."

    def how_are_you(self):
        return "I'm doing great, thank you! How can I assist you today?"

    def listen_command(self):
        return "Yes, I can listen to you. Please speak your command."

    def handle_command(self, command):
        """
        Handle the given command and return the response.

        Args:
            command (str): The command input by the user.

        Returns:
            str: The response from the AI Assistant.
        """
        return self.commands.get(command.lower(), self.unknown_command)()

    def unknown_command(self):
        return "I didn't understand that command."

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.speak("Listening...")
            audio = self.recognizer.listen(source)

        try:
            command = self.recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            return "I didn't catch that."
        except sr.RequestError:
            return "Sorry, my speech service is down."

    def run(self):
        print("Aiza AI Assistant is running")
        self.speak("Aiza AI Assistant is running")
        while True:
            # Uncomment the following line to use speech recognition
            # user_command = self.listen()
            user_command = input("Enter a command: ")
            if user_command.lower() == "exit":
                print("Exiting Aiza AI Assistant.")
                self.speak("Exiting Aiza AI Assistant.")
                break
            response = self.handle_command(user_command)
            print(response)
            self.speak(response)

if __name__ == "__main__":
    assistant = AizaAssistant()
    assistant.run()
