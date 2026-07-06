"""
content_generator.py
---------------------
Core AI engine for the AI-Based Content Generation System.

This module implements a Markov Chain based text generator — a simple,
classic, and fully offline (no external API key required) approach to
automated content generation. It builds a probabilistic model of word
sequences from a training corpus and then generates new, original text
by sampling from that model.

The design is intentionally modular so the underlying generation engine
(MarkovGenerator) can later be swapped out for a call to a large language
model API (e.g. OpenAI, Anthropic) without changing the rest of the app.
"""

import random
import re
from collections import defaultdict


class MarkovGenerator:
    """A simple N-gram Markov Chain text generator."""

    def __init__(self, order: int = 2):
        """
        Args:
            order: number of previous words used as the 'state' to
                   predict the next word. Higher order -> more coherent
                   but less varied text.
        """
        self.order = order
        self.model = defaultdict(list)
        self.starts = []  # valid sentence-starting states

    @staticmethod
    def _tokenize(text: str):
        """Split raw text into cleaned, lowercase-preserving word tokens."""
        text = re.sub(r"\s+", " ", text.strip())
        # keep sentence punctuation attached to words for natural output
        tokens = re.findall(r"[A-Za-z0-9']+[.,!?]?|[.,!?]", text)
        return tokens

    def train(self, text: str):
        """Train (or extend the training of) the model on a block of text."""
        tokens = self._tokenize(text)
        if len(tokens) <= self.order:
            return

        for i in range(len(tokens) - self.order):
            state = tuple(tokens[i:i + self.order])
            next_word = tokens[i + self.order]
            self.model[state].append(next_word)

            # Treat the very first n-gram, and any n-gram following a
            # sentence-ending token, as a valid starting point.
            if i == 0 or tokens[i - 1][-1:] in ".!?":
                self.starts.append(state)

        if not self.starts:
            self.starts.append(tuple(tokens[:self.order]))

    def generate(self, max_words: int = 150) -> str:
        """Generate new text up to approximately max_words long."""
        if not self.model:
            return "The model has not been trained yet. Please add training data first."

        state = random.choice(self.starts)
        result = list(state)

        while len(result) < max_words:
            next_words = self.model.get(state)
            if not next_words:
                # dead end -> restart from a fresh valid starting state
                state = random.choice(self.starts)
                result.extend(state)
                continue

            next_word = random.choice(next_words)
            result.append(next_word)
            state = tuple(result[-self.order:])

            # Stop gracefully at a sentence boundary once we're near the target length
            if len(result) >= max_words and next_word[-1:] in ".!?":
                break

        text = " ".join(result)
        text = re.sub(r"\s+([.,!?])", r"\1", text)  # tidy punctuation spacing
        return self._finalize(text)

    @staticmethod
    def _finalize(text: str) -> str:
        """Capitalize sentence starts and ensure the text ends cleanly."""
        sentences = re.split(r"(?<=[.!?])\s+", text)
        sentences = [s[0].upper() + s[1:] if s else s for s in sentences]
        text = " ".join(sentences)
        if text and text[-1] not in ".!?":
            text += "."
        return text


class ContentGenerationSystem:
    """
    High-level facade that ties together multiple topic-specific
    Markov models and exposes a simple generate() API used by the
    Flask web application.
    """

    def __init__(self):
        self.generators = {}  # topic -> MarkovGenerator

    def add_topic(self, topic: str, corpus_text: str, order: int = 2):
        gen = MarkovGenerator(order=order)
        gen.train(corpus_text)
        self.generators[topic] = gen

    def available_topics(self):
        return list(self.generators.keys())

    def generate_content(self, topic: str, content_type: str, length: str) -> str:
        if topic not in self.generators:
            raise ValueError(f"Unknown topic '{topic}'.")

        length_map = {"short": 60, "medium": 150, "long": 300}
        max_words = length_map.get(length, 150)

        body = self.generators[topic].generate(max_words=max_words)

        if content_type == "blog":
            title = f"{topic.title()}: An In-Depth Look"
            return f"# {title}\n\n{body}"
        elif content_type == "social":
            hashtag = "#" + topic.replace(" ", "")
            return f"{body}\n\n{hashtag}"
        elif content_type == "product":
            return f"Introducing our latest solution for {topic}.\n\n{body}"
        else:  # plain / article
            return body
