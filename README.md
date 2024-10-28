# Diabetes Prediction API

This is a Machine Learning model deployed as a REST API using FastAPI. The model predicts the likelihood of diabetes in a patient based on specific health parameters.

## Project Overview

This project uses a trained model to classify whether a patient is likely to have diabetes based on inputs like blood pressure, BMI, age, and other factors. The API provides an easy-to-use endpoint for predictions, making it suitable for healthcare applications and integrations.

## Model Features

- **Inputs**: The model expects the following features:
  - Pregnancies
  - Glucose
  - Blood Pressure
  - Skin Thickness
  - Insulin
  - BMI (Body Mass Index)
  - Diabetes Pedigree Function
  - Age
- **Output**: Predicts whether the person is diabetic or not.

## Getting Started

### Prerequisites

- Python 3.7 or above
- FastAPI
- Scikit-Learn
- Uvicorn (for running the FastAPI server)


