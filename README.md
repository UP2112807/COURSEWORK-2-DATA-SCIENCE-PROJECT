# COURSEWORK-2-DATA-SCIENCE-PROJECT
Advanced Computational Techniques Coursework github

This project looks at the Palmer Penguins Dataset Extended datset which can be found at: https://www.kaggle.com/datasets/samybaladram/palmers-penguin-dataset-extended?select=palmerpenguins_extended.csv. <br>
This dataset contains the information about 3 penguin species. Inclusing information about the penguins species,	island,	health info and	year of data collection. 
I chose this dataset as it contained over 3000 entries compared to the original Palmer Penguins Dataset because this would be useful when training/testing a neural network and to a lesser extent when making a descion tree model. 
Additionaly this dataset contained 11 collumns of info on each penguin which meant that even if multiple features arent relevent to the target of the model being made I would still have features to use. <br>

This project goes over 3 questions looking at the species of penguins <br>
- Q1: traditional - non neural network approach <br>
      - Using a non neural network apporach to make a model to make prediction about the species of a penguin using the Palmer Penguins Dataset Extended <br>
- Q2: Neural Network approach <br>
      - Using aneural network apporach to make a model to make prediction about the species of a penguin using the Palmer Penguins Dataset Extended <br>
- Q3: How does pre-training (and epochs and batches) affect the performance of a neural network? <br>
      - Test how changing the number of epochs and the batch size can effect the accuracy of predictions made by the same neural network from Q2 <br>

Motivation for Q3 is after initially craeting a neural network in Q2 I found that the accuracy of predictions plateaued after it went pasts a certain number of epochs and I wanted to find what impact changing this would have on my neural network <br>
Run each file run top to bottom making sure that you have the functions.py file one directory above the question .ipynb files. <br>
Dependencies are contained with the dependencies.txt file <br>
