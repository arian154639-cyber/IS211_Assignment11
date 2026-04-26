"""
Python Information: I utilized the resources from week 11 for this, and my RegEx approach was similar to 
my week 3 approach because although the normal version was simple enough, I find my version easier to 
understand.

HTML/CSS Information: I revisited our materials from week 9 to build the HTML and CSS script, while also
using our week 11 materials. I only used "tr/td", because although I knew about "th", I wanted to stick 
to the tutorial style.
"""

from flask import Flask, render_template, redirect, request
import re

app = Flask(__name__)

to_do_items = []

@app.route('/')
def main_controller():
    return render_template("index.html", to_do_items=to_do_items)

@app.route('/submit', methods=['POST'])
def submit_controller():
    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']

    characters = r"\w+"
    at_symbol = "@"
    period = r"\."

    email_structure = characters + at_symbol + characters + period + characters
    email_regex = re.compile(email_structure)

    valid_email = email_regex.search(email) is not None
    valid_priority = priority in ["low", "medium", "high"]

    if valid_email and valid_priority:
        to_do_items.append({
            "task": task,
            "email": email,
            "priority": priority
        })
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear_controller():
    to_do_items.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run()


