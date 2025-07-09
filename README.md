🏠 House Price Prediction – ML-Powered Web App
An interactive full-stack application that predicts house prices based on location, square footage, bathrooms, and BHK using a trained machine learning model. Built with Flask, Scikit-learn, and a sleek Streamlit frontend, it gives fast and accurate predictions backed by real housing data.

🚀 Features

🧠 Trained ML model using Linear Regression
📍 Location-aware predictions (one-hot encoding)
🧮 Inputs: Location, Total Sqft, Bathrooms, BHK
🔗 REST API using Flask (predict & fetch locations)
🖥️ Clean UI via Streamlit for real-time interaction


⚙️ Tech Stack

Flask – Backend API for prediction and data handling
Streamlit – Web UI interface
Scikit-learn – Model training (regression)
Pandas + NumPy – Data preprocessing
Pickle + JSON – Model and metadata serialization

💻 How to Run Locally

1. Clone the Repository
git clone https://github.com/vishnuvardhan30/housepriceprediction.git
cd housepriceprediction

2.
Install Dependices
pip install -r requirements.txt

4. Install Dependencies

pip install -r requirements.txt
4. Start the Flask Backend
bash
Copy
Edit
cd backend
python app.py
5. Start the Streamlit Frontend (in a new terminal)
bash
Copy
Edit
cd frontend
streamlit run frontend.py

📁 Project Structure
housepriceprediction/
├── backend/
│   ├── app.py                # Flask API
│   ├── columns.json          # Encoded feature list
│   ├── price_prediction.pkl  # Trained regression model
│   └── price_prediction.ipynb # Jupyter notebook for training
│
├── frontend/
│   └── frontend.py           # Streamlit app
├── requirements.txt
├── README.md


📬 API Overview

Accepts JSON input:

json
Copy
Edit
{
  "location": "Indira Nagar",
  "total_sqft": 1000,
  "bath": 2,
  "bhk": 3
}
Returns:

json
Copy
Edit
{
  "prediction": 85.75
}

🤝 Contributions
Contributions, suggestions, and forks are welcome! Add more features like map integration, model comparison, or even deploy on cloud platforms.

📄 License
MIT License – free for personal and commercial use.

🙋‍♂️ Author
Made with ❤️ by Vishnu Vardhan
