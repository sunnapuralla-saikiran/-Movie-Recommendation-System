# Movie Recommendation System

A Machine Learning-based Movie Recommendation System that suggests movies to users based on their interests and viewing preferences. The system analyzes movie metadata and similarity scores to provide personalized movie recommendations through an interactive web application.

 **Tech Stack: Python, Pandas, Scikit-learn, Streamlit**

## ✨ Features

🎬 **Movie Recommendation Engine** — recommends similar movies based on user-selected movies.

📊 **Content-Based Filtering** — uses movie genres, keywords, cast, and overview information to calculate similarity between movies.

🧠 **Machine Learning Integration** — utilizes feature extraction and cosine similarity to generate accurate recommendations.

🔍 **Movie Search Functionality** — allows users to search and select movies from the dataset.

⭐ **Top Similar Movie Suggestions** — instantly displays the most relevant movie recommendations.

🖥️ **Interactive Streamlit UI** — simple and user-friendly interface for selecting movies and viewing recommendations.

⚡ **Fast Processing** — precomputed similarity matrix enables quick recommendation generation.

📁 Folder Structure

movie-recommendation-system/

├── app.py                     # Streamlit web application

├── recommendation.py          # Recommendation engine logic

├── movies.csv                 # Movie dataset

├── requirements.txt

├── README.md

├── data/

│   └── movies.csv

├── docs/

│   └── Project_Report.pdf

└── assets/

```
└── screenshots/
```

## ⚙️ Setup & Installation

### 1. Clone the Repository

git clone https://github.com/<your-username>/movie-recommendation-system.git

cd movie-recommendation-system

### 2. Create a Virtual Environment (Recommended)

python -m venv venv

source venv/bin/activate

On Windows:

venv\Scripts\activate

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Run the Application

streamlit run app.py

## ▶️ How to Use

1. Launch the Streamlit application.
2. Select a movie from the dropdown menu.
3. Click the "Recommend" button.
4. View the list of recommended movies similar to your selected movie.
5. Explore multiple recommendations by selecting different movies.

## 🧮 How the Recommendation System Works

### Step 1: Data Preprocessing

* Movie metadata is cleaned and processed.
* Relevant features such as genres, cast, keywords, and movie descriptions are extracted.

### Step 2: Feature Extraction

* Textual information is converted into numerical vectors using feature extraction techniques.

### Step 3: Similarity Calculation

* Cosine Similarity is used to measure similarity between movies.

### Step 4: Recommendation Generation

* When a user selects a movie, the system retrieves movies with the highest similarity scores.
* Top matching movies are displayed as recommendations.

## 🛠️ Tech Stack

**Programming Language:** Python 3.9+

**Data Processing:** Pandas, NumPy

**Machine Learning:** Scikit-learn

**Recommendation Technique:** Content-Based Filtering

**Similarity Measure:** Cosine Similarity

**Web Framework:** Streamlit

**Dataset:** Movie Metadata Dataset

## 🚀 Future Scope

* Hybrid Recommendation System combining content-based and collaborative filtering.
* User authentication and personalized profiles.
* Movie ratings and reviews integration.
* Real-time movie information using external APIs.
* Recommendation history tracking.
* Deployment on Streamlit Community Cloud, Render, or AWS.

## 📄 License

This project was created for academic and educational purposes as part of a CRT Mini Project submission. Free to use and modify for learning purposes.
