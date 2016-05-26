# Author : Loan Huynh
# Reference document : ttp://nbviewer.jupyter.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter08_ml/02_titanic.ipynb
# Desc : Create prediction model in Python
import pandas as pd
import numpy as numpy
from sklearn.linear_model import LogisticRegression
from sklearn import cross_validation as cv
import sklearn.metrics as metric
import src.const.TemplateData as templData


class CandidateMovementModel(object):
    def __init__(self, _file_training_data):
        try:
            self.training_data = pd.read_csv(_file_training_data, sep=',')
        except IOError:
            print "Error:\t File doesnot exist "
        except AttributeError:
            print "Error: \t Please input csv file"

    # this Class create data model from training set
    def createCandidateMovementModel(self):
        # Logis Regression Model
        model = LogisticRegression()
        model.fit(self.training_data[templData.cols_dep_var], self.training_data[templData.temp_col_Moving])
        return model

    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "destroyed"


