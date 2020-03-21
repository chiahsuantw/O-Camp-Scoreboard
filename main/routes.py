#路徑模組
from flask import render_template
from main import app
from main.models import User, Staff, Event

@app.route('/')
def home():
    return render_template  ('layout.html', title='title')

@app.route('/team')
def team():
    return 'team'

@app.route('/rank')
def rank():
    return 'rank'

@app.route('/info')
def roommate():
    return render_template('info.html', title='活動資訊')

@app.route('/bulletinboard')
def bulletin_board():
    return 'bulletin board'

@app.route('/chat')
def chat():
    return 'chat'

@app.route('/thanks')
def thanks():
    return 'thanks'

@app.route('/logout')
def logout():
    return 'logout'
