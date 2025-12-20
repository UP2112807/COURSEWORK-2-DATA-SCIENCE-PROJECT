# COURSEWORK-2-DATA-SCIENCE-PROJECT
Advanced Computational Techniques Coursework github

This project looks at the Palmer Penguins Dataset Extended datset which can be found at https://www.kaggle.com/datasets/samybaladram/palmers-penguin-dataset-extended?select=palmerpenguins_extended.csv.
This dataset contains the information about 3 penguin species. Inclusing information about the penguins species,	island,	health info and	year of data collection.
I chose this dataset as it contained over 3000 entries compared to the original Palmer Penguins Dataset because this would be useful when training/testing a neural network and to a lesser extent when making a descion tree model.
Additionaly this dataset contained 11 collumns of info on each penguin which meant that even if multiple features arent relevent to the target of the model being made I would still have features to use.

This project goes over 3 questions looking at the species of penguins
- Q1: traditional - non neural network approach
- Q2: Neural Network approach
- Q3: How does pre-training (and epochs and batches) affect the performance of a neural network? 

Motivation for Q3 is after initially craeting a neural network in Q2 I found that the accuracy of predictions plateaued after it went pasts a certain number of epochs and I wanted to find what impact changing this would have on my neural network
Run each file run top to bottom making sure that you have the functions.py file one directory above the question .ipynb files.
Dependencies are contained with the dependencies.txt file
