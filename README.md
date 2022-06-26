<h1 align="center">Queerify</h1>
<img src="https://user-images.githubusercontent.com/83456083/175811980-fcb8eee8-e274-46ad-b7a1-2ccf9fed2ec5.png" align="center" />

## Introduction

Queerify is an app built using the Spotify API, Python and Jupyter Notebook that recommends songs so people can discover their new favourite artist easily

## How to use the recommendation model?

- The main model is in the models/model.py

- for .env file create a new project in developer spotify and get the cliend id and client secret from there

- Run all the python files from the root directory otherwise paths need to be changed

- In the current version data/test_playlist.csv is used for recommendataion of the new songs. test_playlist.csv needs to replaced by the user histroy for the project purpose

- The columns and format of the csv file to be formed with the user listening history is can be found is save_data() function of the notebooks/dataset.py after line 24 ie with open(file) command line. Please look into it to find the exact way to extract the data from spotify and save it in csv file.

- After saving the user history in csv format the data needs to be preprocessed using the models/data_preprocessing.py function. This produces the final dataset that can be used for recommendation purposes
