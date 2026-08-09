🌍 WanderAI — Intelligent Tourist System

An AI-powered tourism recommendation web application that helps users discover destinations across India based on their travel preferences and budget.

# Overview

WanderAI is a mini-project built with Flask, Python, SQLite, Pandas, and Scikit-learn.
The application asks users for their preferred travel category and budget, then analyzes destination information using a content-based recommendation approach with TF-IDF and cosine similarity.
The goal is to make destination discovery simple, personalized, and budget-aware.

# Features

• AI-based travel recommendations
• TF-IDF and cosine similarity
• Multiple travel categories
• Budget-based destination filtering
• Destination ratings
• Google Maps links
• Destination images
• Mobile-friendly responsive design
• Try Another Search option
• Search history using SQLite


# The recommendation engine uses a simple content-based filtering pipeline:

Destination category and description are combined into text.

TfidfVectorizer converts destination text into numerical vectors.

Cosine similarity calculates similarity between destinations.

Destinations are filtered according to the selected category and maximum budget.

The highest-similarity matching destinations are returned.

Up to 5 recommendations are displayed.

# Tech Stack

Python :Core programming language

Flask :Web application framework

Pandas :Data handling

Scikit-learn :TF-IDF and cosine similarity

SQLite :Database

HTML :Page structure

CSS :Styling and responsive design

JavaScript :Frontend interactions

Git & GitHub :Version control and hosting


# Responsive Design

The interface is designed to work across:

💻 Desktop

💻 Laptop

📱 Mobile

📲 Tablet

The recommendation cards automatically adjust their layout for smaller screens.

## 🌐 Live Demo

🚀 [Try WanderAI Live]([YOUR_RENDER_URL](https://intelligent-tourist-system.onrender.com))

# Project Scope

This is a mini-project / academic project demonstrating a practical recommendation system.

The recommendation engine currently uses a content-based approach based mainly on destination category and description. It does not use real-time tourism data, live availability, or a large-scale production recommendation model.

# Future Improvements

Possible future enhancements include:

📍 Location-aware recommendations

🗓️ Personalized itinerary generation

🌦️ Weather-aware recommendations

🧠 More advanced recommendation models

👤 User profiles and preference history

🗺️ Interactive maps

🏨 Hotel and restaurant recommendations

💬 AI travel assistant/chatbot



B.Sc. Computer Science / AI & Data Science Student

This project was developed as a practical mini-project to explore Flask web development, machine learning-based recommendation systems, databases, and deployment.
