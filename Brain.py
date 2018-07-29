import tensorflow as tf 
import pandas
import csv

class Brain:
    def __init__(self):
        data = pandas.read_csv('./colors.csv')
        class_names = ['Red', 'Green', 'Blue']
        print(data.iloc[0:3])