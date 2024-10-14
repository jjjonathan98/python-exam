class Message:
    # Constructor that initializes a Message object.
    def __init__(self, sender, recipient):
        self.sender = sender
        self.recipient = recipient
        self.message_content = ""

    # Gets name of the sender.
    def get_sender(self):
        return self.sender

    # Gets name of the recipient
    def get_recipient(self):
        return self.recipient

    # Appends/adds text to the message content.
    def append(self, txt):
        self.message_content += txt + "\n"

    # Converts the message object to a string.
    def __str__(self):
        return f"From: {self.sender}\nTo: {self.recipient}\n{self.message_content}"


# Main function to demonstrate an example of the use of the Message class.
def main():
    sender = input("Enter your mail: ")
    recipient = input("Enter the recipient's mail: ")

    # Create a new message Object
    new_message = Message(sender, recipient)

    # Message input
    print("Enter message or an empty line to finish.")
    while True:
        user_message = input("> ")
        if user_message:
            new_message.append(user_message)
        else:
            break

    print(new_message)


# Runs the code
main()


