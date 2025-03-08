import os

class AizaAssistant:
    def __init__(self):
        self.commands = {
            "hello": self.greet,
            "bye": self.farewell,
            # Add more commands here
        }

    def greet(self):
        return "Hello! How can I assist you today?"

    def farewell(self):
        return "Goodbye! Have a great day!"

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

    def run(self):
        print("Aiza AI Assistant is running")
        while True:
            user_command = input("Enter a command: ")
            if user_command.lower() == "exit":
                print("Exiting Aiza AI Assistant.")
                break
            response = self.handle_command(user_command)
            print(response)

if __name__ == "__main__":
    assistant = AizaAssistant()
    assistant.run()
