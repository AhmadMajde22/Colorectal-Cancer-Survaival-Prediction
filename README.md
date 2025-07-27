
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
Colorectal-Cancer-Survaival-Prediction/
├── app.py, application.py           # Main Flask web application for serving predictions
│   - Handles HTTP requests, loads trained model, and returns predictions
│   - Connects frontend (HTML/CSS) with backend ML logic
├── pipeline/
│   ├── __init__.py                  # Pipeline module initializer
│   └── training_pipeline.py         # Main script for orchestrating the ML pipeline
│       - Loads config, runs data ingestion, preprocessing, training, evaluation, and saves artifacts
├── kubeflow_pipeline/
│   ├── __init__.py                  # Kubeflow pipeline module initializer
│   └── pipeline.py                  # Kubeflow pipeline definition and orchestration
│       - Automates pipeline steps for scalable, reproducible ML workflows
├── src/
│   ├── __init__.py                  # Source module initializer
│   ├── custom_exception.py          # Custom exception handling for robust error management
│   ├── data_ingestion.py            # Loads raw data, validates schema, handles missing values
│   ├── data_processing.py           # Cleans, encodes, and scales features
│   ├── logger.py                    # Centralized logging for debugging and monitoring
│   ├── model_training.py            # Trains, tunes, and evaluates ML models
│   └── __pycache__/                 # Python cache files
├── config/
│   ├── __init__.py                  # Config module initializer
│   ├── config.yaml                  # Main configuration file (paths, parameters, model settings)
│   ├── credentials.json             # Credentials for external services (e.g., cloud, databases)
│   ├── path_config.py               # Utility for managing file paths
│   └── __pycache__/                 # Python cache files
├── artifacts/
│   ├── models/
│   │   └── model.pkl                # Trained model file (best performing model)
│   ├── processed/
│   │   ├── label_encoders.pkl       # Saved label encoders for categorical features
│   │   ├── scaler.pkl               # Saved scaler for feature normalization
│   │   ├── X_test.pkl               # Test features
│   │   ├── X_train.pkl              # Train features
│   │   ├── y_test.pkl               # Test labels
│   │   └── y_train.pkl              # Train labels
│   └── raw/
│       └── data.csv                 # Raw input dataset (clinical data)
├── mlruns/
│   └── ...                          # MLflow experiment tracking files and folders
│       - Stores runs, metrics, parameters, and artifacts for each experiment
├── static/
│   ├── background.jpg               # Web app background image
│   └── style.css                    # Web app CSS styles
├── templates/
│   └── index.html                   # Web app HTML template (user interface)
├── utils/
│   ├── __init__.py                  # Utils module initializer
│   └── common_functions.py          # Utility functions for data and model operations
│   └── __pycache__/                 # Python cache files
├── logs/
│   └── log_YYYY-MM-DD.log           # Log files for pipeline and app (debugging, audit trail)
├── requirements.txt                 # Python dependencies (all required packages)
├── setup.py                         # Project setup script (for packaging and distribution)
├── pyproject.toml                   # Project metadata and build system configuration
├── Dockerfile                       # Docker container specification (for deployment)
├── README.md                        # Project documentation (this file)
├── Cancer_Survival_Prediction.egg-info/
│   └── ...                          # Python package metadata (for distribution)
└── notebook/
    └── notebook.ipynb               # Jupyter notebook for exploration, EDA, and testing
```

**Project Organization Details:**

- **Web Application:**
  - `app.py` and `application.py` serve as the entry point for the Flask web app, allowing users to interact with the model via a browser.
  - Uses HTML templates and CSS for a user-friendly interface.

- **ML Pipeline:**
  - The `pipeline/` folder contains scripts for orchestrating the end-to-end ML workflow, from data ingestion to model deployment.
  - The pipeline is modular, allowing easy updates and experimentation.

- **Kubeflow Integration:**
  - The `kubeflow_pipeline/` folder enables scalable and automated ML workflows using Kubeflow.
  - Pipelines can be run locally or on cloud infrastructure.

- **Source Code:**
  - The `src/` folder contains all core logic for data handling, preprocessing, model training, and logging.
  - Custom exceptions and logging ensure robustness and traceability.

- **Configuration:**
  - The `config/` folder centralizes all configuration files and credentials, making the project flexible and secure.

- **Artifacts:**
  - The `artifacts/` folder stores all outputs from the pipeline, including trained models, encoders, scalers, and datasets.
  - Ensures reproducibility and versioning of results.

- **Experiment Tracking:**
  - The `mlruns/` folder is managed by MLflow, tracking all experiments, metrics, and parameters for model development.

- **Utilities:**
  - The `utils/` folder provides helper functions for common tasks, improving code reuse and maintainability.

- **Logs:**
  - The `logs/` folder contains log files for monitoring pipeline and app execution.

- **Testing and Exploration:**
  - The `notebook/` folder includes Jupyter notebooks for exploratory data analysis, prototyping, and testing.

- **Packaging and Deployment:**
  - `requirements.txt`, `setup.py`, `pyproject.toml`, and `Dockerfile` support installation, packaging, and containerization for local or cloud deployment.

- **Documentation:**
  - `README.md` provides comprehensive documentation for users and contributors.

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
