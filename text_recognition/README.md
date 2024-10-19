# Sentiment Analysis Project

This project is focused on building and training models for binary sentiment classification based on text messages. The main objective is to develop an optimal model capable of accurately recognizing emotions in text.

## Relevance

Emotion recognition in text is becoming an increasingly important task in today's world, especially with the growing use of chatbots and virtual assistants. For instance, banking chatbots, despite their widespread use, often struggle to understand the emotional state of a client. This results in unsatisfactory responses, reduced customer service quality, and ultimately, client attrition.

The primary goal of this project is to create a model that could be integrated into such chatbots, allowing them to interact more effectively by recognizing customer emotions and responding accordingly.

## Workflow

The following steps were taken during the development of this project:

- Searching and analyzing datasets with sufficient information and necessary parameters (e.g., text length distribution and labels).
- Selecting the best dataset among the analyzed ones and preparing it for use.
- Data preprocessing: cleaning unnecessary symbols, testing hypotheses on stemming and lemmatization.
- Training multiple models to compare their performance and find the best one.
- Hyperparameter optimization for the best models.
- Selecting the top-3 models and determining the best one after optimization.
- Testing the final model on independent examples.

As a result, the main goal of the project was achieved — the creation of a model that shows high accuracy in binary sentiment classification of text.

## Project Structure

The folder `text_recognition` contains the following key files:
1. **model_parameters.pickle** – Parameters of the models optimized through Optuna.
2. **result_model_pipeline.pickle** – The final sentiment classification model, which is the product of this project.
3. **text_recognition_code** – The code used for research and model development.
4. **test_model.py** – A script for testing the final model through the command line.

## Installation Instructions

To clone and use this project locally, follow these steps:

### 1. Clone the repository
```bash
git clone https://github.com/egrsid/sentiment_analysis.git
```

### 2. Navigate to the `text_recognition` folder
```bash
cd sentiment_analysis/text_recognition
```

### 3. Install the required dependencies
```bash
pip install -r requirements.txt
```


## Testing the Model
Once the environment is set up, you can test the model using the test_model.py script. The testing is done via the command line, using the following format:

```bash
!python test_model.py --text 'your text'
```
Replace 'your text' with the text message you want to classify

## Libraries Used
The project was implemented using the following libraries:
- [scikit-learn](https://scikit-learn.org/)
- [Optuna](https://optuna.org/)
- [matplotlib](https://matplotlib.org/)
- [NumPy](https://numpy.org/)
- [Pandas](https://pandas.pydata.org/)
- [Pickle](https://docs.python.org/3/library/pickle.html)
- [Seaborn](https://seaborn.pydata.org/)
- [tqdm](https://tqdm.github.io/)
- [re (Regular Expressions)](https://docs.python.org/3/library/re.html)
- [WordCloud](https://github.com/amueller/word_cloud)
- [string (String Operations)](https://docs.python.org/3/library/string.html)
- [nltk (Natural Language Toolkit)](https://www.nltk.org/)
- [CatBoost](https://catboost.ai/)
- Custom framework [ml_tools](https://github.com/egrsid/ml_tools)
