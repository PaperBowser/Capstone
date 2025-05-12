
# global settings
random_state = 66
test_size = 0.2
stratify = True  # Whether to stratify during train/test split

# wandb settings
wandb_project = "nba-all-star"
wandb_entity = None  # Set to your W&B username/org if needed
wandb_tracking = True

# random forest settings
rf_params = {
    "n_estimators": 100,
    "max_depth": None,
    "min_samples_split": 2,
    "min_samples_leaf": 1,
    "max_features": "auto",
    "class_weight": None,
    "random_state": random_state
}

# RandomizedSearchCV settings for random forest
rf_param_dist = {
    "n_estimators": [100, 200, 300],
    "max_depth": [None, 10, 20, 30],
    "min_samples_split": [2, 5, 10],
    "min_samples_leaf": [1, 2, 4],
    "max_features": ["auto", "sqrt", "log2"],
    "class_weight": [None, "balanced"]
}
search_cv_params = {
    "n_iter": 20,
    "cv": 5,
    "scoring": "f1",
    "verbose": 1,
    "n_jobs": -1,
    "random_state": random_state
}

# logistic regression settings
logreg_params = {
    "solver": "lbfgs",
    "max_iter": 1000,
    "class_weight": None,
    "random_state": random_state
}
