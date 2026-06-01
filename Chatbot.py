print("Welcome to Simple Chatbot!")
print("Type 'bye' to exit.\n")

while True:

    user_message = input("You: ").lower()

    if user_message == "hello":
        print("Bot: Hi!")

    elif user_message == "how are you":
        print("Bot: I'm fine, thanks!")

    elif user_message == "what is your name":
        print("Bot: I am a simple chatbot.")

    elif user_message == "who created you":
        print("Bot: ABC created me.")

    elif user_message == "what can you do":
        print("Bot: I can chat with you.")

    elif user_message == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")