🌍 WanderAI — Intelligent Tourist System

An AI-powered tourism recommendation web application that helps users discover destinations across India based on their travel preferences and budget.

# Overview

WanderAI is a mini-project built with Flask, Python, SQLite, Pandas, and Scikit-learn.
The application asks users for their preferred travel category and budget, then analyzes destination information using a content-based recommendation approach with TF-IDF and cosine similarity.
The goal is to make destination discovery simple, personalized, and budget-aware.

# Features

*AI-based recommendations using TF-IDF and cosine similarity
*Multiple travel categories such as Beaches, Nature, Historical Places, Adventure,Wildlife,Spiritual, Shopping, and Food
*Budget-based filtering to avoid destinations above the user's selected budget
*Destination ratings displayed on recommendation cards
*Google Maps links for available destinations
*Destination images stored locally in the application
*Responsive interface designed for desktop and mobile screens
*Try Another Search flow for making a new recommendation request
*Search history stored in SQLite


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


# The interface is designed to work across:

💻 Desktop

💻 Laptop

📱 Mobile

📲 Tablet

The recommendation cards automatically adjust their layout for smaller screens.

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
📊 Recommendation analytics dashboard
☁️ Persistent production database


B.Sc. Computer Science / AI & Data Science Student

This project was developed as a practical mini-project to explore Flask web development, machine learning-based recommendation systems, databases, and deployment.
