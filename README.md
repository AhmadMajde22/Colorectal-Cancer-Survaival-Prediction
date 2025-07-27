
# Colorectal Cancer Survival Prediction

This project predicts the survival probability of colorectal cancer patients using machine learning and MLOps best practices. It includes data ingestion, preprocessing, model training, evaluation, deployment, and pipeline automation.

## Background

Colorectal cancer is one of the most common cancers worldwide. Predicting patient survival can help clinicians make informed decisions and improve patient outcomes. This project leverages clinical data and machine learning to build a robust survival prediction system, integrating MLOps tools for reproducibility and scalability.

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
  - [Dataset](#dataset)
  - [Model Details](#model-details)
  - [Deployment](#deployment)
  - [Troubleshooting](#troubleshooting)
  - [References](#references)

---

## Project Overview

This repository provides an end-to-end solution for predicting colorectal cancer survival using clinical data. It leverages Python, scikit-learn, MLflow, and Kubeflow for reproducible machine learning workflows and deployment.

## Dataset

The dataset used for this project is located at `artifacts/raw/data.csv`. It contains anonymized clinical features relevant to colorectal cancer survival, such as age, tumor stage, treatment type, and outcome. Data preprocessing includes handling missing values, encoding categorical variables, and feature scaling.

## Features

- Data ingestion and preprocessing
- Feature engineering and scaling
- Model training and evaluation
- MLflow experiment tracking
- Kubeflow pipeline for automation
- Web app for predictions (Flask)
- Docker support for containerization
- Configurable via YAML/JSON files

## Model Details

The main models used are RandomForestClassifier and XGBoostClassifier, chosen for their performance on tabular clinical data. Hyperparameter tuning is performed using grid search and cross-validation. Model metrics include accuracy, F1 score, precision, recall, and ROC AUC. The best model is saved as `artifacts/models/model.pkl`.

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

## Pipeline Steps

1. **Data Ingestion:** Loads raw data from CSV.
2. **Preprocessing:** Cleans data, encodes categorical features, scales numerical features.
3. **Feature Engineering:** Creates new features if needed.
4. **Model Training:** Trains and tunes ML models.
5. **Evaluation:** Calculates metrics and logs results to MLflow.
6. **Artifact Saving:** Stores models, encoders, and scalers for deployment.
7. **Deployment:** Serves predictions via Flask web app or Docker container.

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

## Deployment

You can deploy the model as a REST API using Flask (`app.py`) or as a Docker container. For cloud deployment, consider using Azure, AWS, or GCP. The web app allows users to input patient data and receive survival predictions instantly.

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

## Troubleshooting

- If you encounter missing package errors, ensure all dependencies in `requirements.txt` are installed.
- For MLflow issues, verify the tracking server is running and accessible.
- For Docker issues, check Docker installation and permissions.
- For pipeline errors, review logs in the `logs/` directory.

## ML Pipeline

- **Data Ingestion:** Loads raw data from `artifacts/raw/data.csv`.
- **Preprocessing:** Cleans, encodes, and scales features.
- **Model Training:** Trains ML models (e.g., RandomForest, XGBoost).
- **Evaluation:** Computes metrics (Accuracy, F1, Precision, Recall, ROC AUC).
- **Artifacts:** Saves models, encoders, scalers for deployment.

## References

- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [MLflow Documentation](https://mlflow.org/docs/latest/index.html)
- [Kubeflow Pipelines](https://www.kubeflow.org/docs/components/pipelines/)
- [XGBoost Documentation](https://xgboost.readthedocs.io/en/stable/)

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
