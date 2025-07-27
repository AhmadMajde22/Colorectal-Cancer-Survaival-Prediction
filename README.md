
# Colorectal Cancer Survival Prediction

This project predicts the survival probability of colorectal cancer patients using machine learning and MLOps best practices. It includes data ingestion, preprocessing, model training, evaluation, deployment, and pipeline automation.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [ML Pipeline](#ml-pipeline)
- [Kubeflow Integration](#kubeflow-integration)
- [Model Tracking with MLflow](#model-tracking-with-mlflow)
- [Web Application](#web-application)
- [Configuration](#configuration)
- [Artifacts](#artifacts)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview

This repository provides an end-to-end solution for predicting colorectal cancer survival using clinical data. It leverages Python, scikit-learn, MLflow, and Kubeflow for reproducible machine learning workflows and deployment.

## Features

- Data ingestion and preprocessing
- Feature engineering and scaling
- Model training and evaluation
- MLflow experiment tracking
- Kubeflow pipeline for automation
- Web app for predictions (Flask)
- Docker support for containerization
- Configurable via YAML/JSON files

## Project Structure

```
.
├── app.py, application.py         # Flask web app
├── pipeline/                     # Training pipeline scripts
├── kubeflow_pipeline/            # Kubeflow pipeline definition
├── src/                          # Core ML modules (data, model, logger, exceptions)
├── config/                       # YAML/JSON configs
├── artifacts/                    # Saved models, encoders, scalers, datasets
├── mlruns/                       # MLflow experiment logs
├── static/, templates/           # Web app assets
├── requirements.txt, setup.py    # Dependencies
├── Dockerfile                    # Containerization
├── README.md                     # Project documentation
└── notebook/                     # Jupyter notebook for exploration
```

## Setup & Installation

1. **Clone the repository:**

   ```powershell
   git clone https://github.com/AhmadMajde22/Colorectal-Cancer-Survaival-Prediction.git
   cd Colorectal-Cancer-Survaival-Prediction
   ```

2. **Create and activate a Python environment:**

   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```powershell
   pip install -r requirements.txt
   ```

4. **(Optional) Set up MLflow tracking server:**

   ```powershell
   mlflow ui
   ```

5. **(Optional) Build Docker image:**

   ```powershell
   docker build -t cancer-survival-app .
   ```

## Usage

### 1. Train the Model

Run the training pipeline:

```powershell
python pipeline/training_pipeline.py
```

### 2. Run the Web Application

Start the Flask app:

```powershell
python app.py
```

Access the web interface at `http://localhost:5000`.

### 3. Use Kubeflow Pipeline

Define and run the pipeline:

```powershell
python kubeflow_pipeline/pipeline.py
```

(Requires Kubeflow setup)

## ML Pipeline

- **Data Ingestion:** Loads raw data from `artifacts/raw/data.csv`.
- **Preprocessing:** Cleans, encodes, and scales features.
- **Model Training:** Trains ML models (e.g., RandomForest, XGBoost).
- **Evaluation:** Computes metrics (Accuracy, F1, Precision, Recall, ROC AUC).
- **Artifacts:** Saves models, encoders, scalers for deployment.

## Kubeflow Integration

Automates the ML workflow using Kubeflow pipelines. See `kubeflow_pipeline/pipeline.py` for details.

## Model Tracking with MLflow

Tracks experiments, parameters, and metrics in `mlruns/`. View results with `mlflow ui`.

## Web Application

- User-friendly interface for predictions.
- Input patient data and get survival probability.
- See `templates/index.html` and `static/style.css` for UI.

## Configuration

- **YAML/JSON files:** Control paths, credentials, and pipeline settings.
  - `config/config.yaml`
  - `config/credentials.json`
  - `colorectal_cancer_pipeline.yaml`

## Artifacts

- **Models:** `artifacts/models/model.pkl`
- **Encoders/Scalers:** `artifacts/processed/`
- **Datasets:** `artifacts/raw/`, `artifacts/processed/`

## Testing

- Unit tests and notebook exploration in `notebook/notebook.ipynb`.
- Logs available in `logs/`.

## Contributing

Contributions are welcome! Please fork the repo and submit a pull request.

## License

This project is licensed under the MIT License.

---
