from rivescript import RiveScript

chatbot = RiveScript(utf8 = True)

chatbot.prepare_brain_transplant()
chatbot.load_directory("application/bot_brain")
chatbot.sort_replies()

def Chat(user_msg):
    if user_msg == "":
        return  "Please type a message"
    else:
        response = chatbot.reply("user", user_msg)
    if response:
        return  response
    else:
        return "No reply, please try again"