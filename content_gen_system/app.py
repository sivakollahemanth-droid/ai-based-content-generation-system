"""
app.py
-------
Flask web application for the AI-Based Content Generation System.

Run with:
    pip install -r requirements.txt
    python app.py

Then open http://127.0.0.1:5000 in your browser.
"""

from flask import Flask, render_template, request, jsonify

from content_generator import ContentGenerationSystem
from corpus.data import TOPICS

app = Flask(__name__)

# Initialize the content generation system and train it on each topic corpus.
engine = ContentGenerationSystem()
for topic_name, corpus_text in TOPICS.items():
    engine.add_topic(topic_name, corpus_text, order=2)


@app.route("/")
def index():
    return render_template("index.html", topics=engine.available_topics())


@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json(force=True)
    topic = data.get("topic", "")
    content_type = data.get("content_type", "article")
    length = data.get("length", "medium")

    try:
        content = engine.generate_content(topic, content_type, length)
        return jsonify({"success": True, "content": content})
    except ValueError as e:
        return jsonify({"success": False, "error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
