# Shakespeare Bayes Classifier

This project implements a Naive Bayes Classifier to identify which Shakespearean play a given sentence most likely belongs to. The classifier uses word frequencies from the text of Shakespeare's plays to calculate probabilities and make predictions.

## Features

- **Classification**: Classifies a given sentence into one of Shakespeare's plays.
- **Probability Estimates**: Provides probability estimates for each play (available in `full_estimates.py`).

## Usage

### Running the Classifier

1. Ensure all play text files (e.g., `romeo.txt`, `hamlet.txt`) are in the same directory as the scripts.
2. Run the `classifier.py` script to classify a sentence:
   ```bash
   python classifier.py
   Enter a sentence when prompted, and the script will output the play it most likely belongs to.
3. Run the full_estimates.py script to get probability estimates for each play:
    ```bash
   python full_estimates.py
   Enter a sentence when prompted, and the script will output the probabilities for all plays.
