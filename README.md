# AI-Poet
A Natural Language Model focused on creating poems based on input text.

<img width="600px" src="https://user-images.githubusercontent.com/29586111/175834964-7257fbd9-b9d8-4064-96f0-332794c2c7a8.png" />

## Model
The model is a version of a Bidirectional LSTM model trained on a dataset of around 400-600 poems. \
Below are the layers used in this model. \
* Embedding (For Dictionary)
* Bidirectional LSTM
* Dropout (For Generalization / Reducing Overfitting)
* LSTM (For Generalization)
* Dense


## Usage
An online version can be found at https://poet.lynnlo.tech/

To host it locally for personal use, follow these steps\
1. Download the repository on your local machine
2. Either use Poetry or Pip/Conda to install the dependencies \
  a. For Poetry `poetry install` \
  b. For Pip `pip install -r requirements.txt`
3. Use python (3.7.5 or 3.8) to run `python3 server.py`
4. Go to localhost:4000
