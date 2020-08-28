from application import app, chatbot
from flask import render_template, request, send_from_directory, abort, session

@app.route("/")
@app.route("/index")
@app.route("/homepage")
def index():
    chatbot.chatbot.clear_uservars() # To reset bot to initial chat point
    session['chatData'] = {'topic': 'random'}
    return render_template("homepage.html")

@app.route("/get")
def chat():
    # Loading the chat state data to the current bot
    chatbot.chatbot.set_uservars("user", session['chatData'])
    user_msg = request.args.get('msg')
    bot_response_msg = chatbot.Chat(user_msg)
    # Storing the chat state data for loading in future requests on the same session
    session['chatData'] = chatbot.chatbot.get_uservars("user")
    return str(bot_response_msg)

# Downloads route
@app.route("/getpdf/<pdf_id>")
def getpdf(pdf_id):
    return "https://github.com/AhmedAbdEl-Nasser/beta-test/raw/master/application/static/client/pdf/" + pdf_id

    # Used during develpment
    """
    app.config["CLIENT_PDF"] = "C:\AI\My Virtual Env\Project\application\static\client\pdf"
    filename = f"{pdf_id}.pdf"
    try:
        return send_from_directory(app.config["CLIENT_PDF"], filename=filename, as_attachment=True)
    except FileNotFoundError:
        abort(404)
    """
