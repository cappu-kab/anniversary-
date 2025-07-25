from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/puzzle')
def puzzle():
    return render_template('page2_puzzle.html')

@app.route('/memory')
def memory():
    return render_template('page3_memory.html')

@app.route('/message1')
def message1():
    return render_template('page4_message1.html')

@app.route('/message2')
def message2():
    return render_template('page5_message2.html')

@app.route('/likes')
def likes():
    like_list = [
        "You always make me smile 😊",
        "Your hugs feel like home 🤗",
        "You never give up on me ❤️",
        "Your silly jokes make my day 😂",
        "You're kind and thoughtful 🥰",
        "You listen — really listen 🎧",
        "You're my safe place 🌈",
        "You support my dreams ✨",
        "You care deeply and genuinely 💕",
        "You're just YOU — and that’s perfect 💖"
    ]
    return render_template("page5_5_likes.html", likes=like_list)


@app.route('/final')
def final():
    return render_template('page6_final.html')

if __name__ == '__main__':
    app.run(debug=True)
