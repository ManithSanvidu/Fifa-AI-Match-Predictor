# Fifa-AI-Match-Predictor
# ⚽ FIFA World Cup 2026 AI Match Outcome Predictor

An AI-powered football match prediction system that predicts FIFA World Cup 2026 match outcomes, scorelines, and win probabilities using multiple machine learning algorithms. The project provides an interactive Streamlit dashboard and a FastAPI backend for real-time predictions.

---

## 📌 Features

- Predict match winner (Home Win / Draw / Away Win)
- Predict expected scoreline using Poisson Regression
- Win probability prediction
- Confidence percentage for predictions
- Random Forest classifier
- XGBoost classifier
- Neural Network classifier
- Ensemble prediction system
- FastAPI REST API
- Interactive Streamlit dashboard
- Feature engineering from football statistics
- Model evaluation and comparison

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- FastAPI
- Streamlit
- Joblib
- Matplotlib

---

## 📂 Project Structure

```text
fifa-ai-predictor/
│
├── app/
│   └── streamlit_app.py
│
├── api/
│   └── main.py
│
├── data/
│   ├── matches.csv
│   ├── rankings.csv
│   └── players.csv
│
├── models/
│   ├── rf_model.pkl
│   ├── xgb_model.pkl
│   ├── nn_model.pkl
│   ├── poisson_home.pkl
│   └── poisson_away.pkl
│
├── src/
│   ├── config.py
│   ├── utils.py
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── train_rf.py
│   ├── train_xgb.py
│   ├── neural_network.py
│   ├── poisson_model.py
│   ├── confidence.py
│   ├── predict.py
│   └── evaluate.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Dataset

This project uses football datasets containing:

- Historical international match results
- Team rankings
- Player ratings
- Goals scored and conceded
- Team performance statistics
- Head-to-head records

Example datasets:

- FIFA Match Results
- FIFA Team Rankings
- EA Sports FC Player Ratings

---

## ⚙️ Installation

Clone the repository.

```bash
git clone https://github.com/your-username/fifa-ai-predictor.git
```

Move into the project directory.

```bash
cd fifa-ai-predictor
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate the virtual environment.

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Project

### 1. Preprocess the dataset

```bash
python src/data_preprocessing.py
```

### 2. Generate features

```bash
python src/feature_engineering.py
```

### 3. Train the Random Forest model

```bash
python src/train_rf.py
```

### 4. Train the XGBoost model

```bash
python src/train_xgb.py
```

### 5. Train the Neural Network

```bash
python src/neural_network.py
```

### 6. Train the Poisson Regression model

```bash
python src/poisson_model.py
```

### 7. Start the FastAPI server

```bash
uvicorn api.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger documentation:

```
http://127.0.0.1:8000/docs
```

### 8. Launch the Streamlit application

```bash
streamlit run app/streamlit_app.py
```

---

## 🤖 Machine Learning Models

| Model | Purpose |
|--------|---------|
| Random Forest | Match outcome classification |
| XGBoost | Match outcome classification |
| Neural Network | Match outcome prediction |
| Poisson Regression | Goal prediction |
| Ensemble Model | Final prediction using combined probabilities |

---

## 📈 Prediction Output

The application predicts:

- Match Winner
- Win Probability
- Draw Probability
- Away Win Probability
- Expected Home Goals
- Expected Away Goals
- Prediction Confidence

---

## 📷 Future Improvements

- FIFA World Cup 2026 tournament simulator
- Knockout bracket prediction
- Live FIFA rankings integration
- Team comparison dashboard
- Interactive visualizations
- Cloud deployment
- Real-time football data integration

---

## 👨‍💻 Author

**Manith**

Final Year Artificial Intelligence / Machine Learning Project

---

## 📄 License

This project is intended for educational and academic purposes.
