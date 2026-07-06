# AI-Based Content Generation System

A simple, self-contained web application that automatically generates
original text content (blog posts, social media captions, product
descriptions, and articles) using a Markov Chain based AI text-generation
engine trained on topic-specific text corpora.

This project works completely **offline** — no API keys or internet
connection required — making it ideal as a base/starter project that can
later be extended with a real large-language-model API (OpenAI, Anthropic,
etc.) by swapping out the `MarkovGenerator` class in `content_generator.py`.

## Features

- Generate content for 4 built-in topics: Technology, Health, Business, Education
- 4 content types: Article, Blog Post, Social Media Caption, Product Description
- 3 length options: Short, Medium, Long
- Clean, responsive web interface
- Modular architecture — easy to add new topics or plug in a real AI API

## Project Structure

```
content_gen_system/
├── app.py                  # Flask web server & routes
├── content_generator.py    # Core AI engine (Markov Chain generator)
├── corpus/
│   └── data.py              # Training text for each topic
├── templates/
│   └── index.html            # Web UI
├── static/
│   └── style.css              # Styling
└── requirements.txt
```

## Setup & Run

1. (Recommended) create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   python app.py
   ```

4. Open your browser at **http://127.0.0.1:5000**

## How It Works

1. On startup, the app trains a separate Markov Chain model for each topic
   using the sample text in `corpus/data.py`.
2. When you select a topic, content type, and length in the UI and click
   **Generate Content**, the browser sends a request to the `/generate`
   API endpoint.
3. The `ContentGenerationSystem` picks the matching topic model, generates
   a sequence of words based on learned word-transition probabilities, and
   formats it according to the chosen content type (e.g. adding a title for
   blog posts, a hashtag for social captions).

## Extending the Project

- **Add a new topic:** add an entry to the `TOPICS` dictionary in
  `corpus/data.py` and it will automatically appear in the dropdown.
- **Improve output quality:** add more/larger training text per topic, or
  increase the Markov `order` parameter (in `app.py`) for more coherent
  (but less varied) sentences.
- **Upgrade to a real LLM:** replace the body of
  `ContentGenerationSystem.generate_content()` with a call to an LLM API
  (e.g. the Anthropic or OpenAI API) using the topic/content_type/length
  as prompt parameters — the rest of the app (routes, UI) needs no changes.

## Tech Stack

- **Backend:** Python, Flask
- **AI Technique:** Markov Chain text generation (N-gram probabilistic model)
- **Frontend:** HTML, CSS, vanilla JavaScript (fetch API)
