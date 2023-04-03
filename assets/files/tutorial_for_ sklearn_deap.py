import random
import numpy as np
from sklearn.datasets import load_boston
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn_deap import DEAPSearchCV

# Load movie ratings dataset
ratings_data = load_boston()

# Split the dataset into features and target
X, y = ratings_data.data, ratings_data.target

# Define a pipeline for the linear regression model
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('regressor', LinearRegression())
])

# Define the search space for hyperparameters
search_space = {
    'regressor__fit_intercept': [True, False],
    'regressor__normalize': [True, False],
}

# Define the fitness function to optimize
def fitness_function(individual):
    pipeline.set_params(**individual)
    score = np.mean(cross_val_score(pipeline, X, y, cv=5, n_jobs=-1))
    return score,

# Create the genetic algorithm for optimizing hyperparameters
genetic_algorithm = DEAPSearchCV(
    estimator=pipeline,
    params=search_space,
    cv=5,
    verbose=1,
    n_jobs=-1,
    scoring='neg_mean_squared_error',
    population_size=50,
    generations_number=10,
    tournament_size=3,
    crossover_probability=0.5,
    mutation_probability=0.2,
    elitism=True,
    random_state=random.seed(42)
)

# Fit the genetic algorithm to the data
genetic_algorithm.fit(X, y)

# Print the best hyperparameters and corresponding score
print('Best hyperparameters:', genetic_algorithm.best_params_)
print('Best score:', -genetic_algorithm.best_score_)
