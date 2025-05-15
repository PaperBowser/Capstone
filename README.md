# NBA All-Star Prediction

This project uses season-level NBA player and team data to predict whether a player will be selected as an All-Star. It 
applies Logistic Regression and random forest models, evaluates model performance, and selects the best model based on 
F1 score.

## Project Structure

- `data/`: Contains raw, processed, and reference datasets.
- `docs/`: Contains submissions for each WGU task. Stored for centralization and context, not for use in the project.
- `models/`: Stores the final saved model and any associated scalers.
- `notebooks/`: Contains Jupyter notebooks for data preparation, model comparison, and evaluation.
- `config.py`: Stores project settings and hyperparameters.
- `requirements.txt`: Project dependencies.

## Notebooks

- **`data_prep.ipynb`**: Cleans and merges raw datasets and outputs modeling-ready data.
- **`model_comparison.ipynb`**: Trains baseline and tuned models, compares performance, and selects a final model.
- **`model_evaluation.ipynb`**: Loads the final model, evaluates it on the test set, and provides visual interpretation.

## Final Model

The final model is a Logistic Regression classifier selected for its strong F1 score and balanced performance on the 
minority class (All-Star players).

## Getting Started

1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
