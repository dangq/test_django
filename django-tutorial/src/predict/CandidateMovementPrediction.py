# Author: Loan Huynh
# Date : 22- May- 2016
# Desc: this file contains functions to calculate prediction result for candidate movement based on model which is defined in "model" folder

import pandas as pd
import numpy as numpy
import src.const.TemplateData as templData
from sklearn.linear_model import LogisticRegression

class CandidateMovementPrediction():
    def __init__(self, model, _file_predicted_data,_file_name):
        self._file_name=_file_name
        self.model = model
        self._file_predicted_data=_file_predicted_data
        try:
            self._file_input_data = pd.read_csv(_file_predicted_data, sep=',')
            #print self._file_input_data
        except IOError:
            print "Error:\t File doesnot exist "
        except AttributeError:
            print "Error: \t Missing attributes"
        print "create instance for CandidateMovement"

    # function to calculate the probability of movement prediction
    def calProbMovementPrediction(self):
        try:
            #print self._file_input_data[templData.cols_dep_var]
            # if (isinstance(dataInput, ndarray)):
            # predicted_probability = self.model.predict_proba(self._file_input_data[templData.cols_dep_var])[:, 1]
            predicted_probability = self.model.predict_proba(self._file_input_data[templData.cols_dep_var])[:,1]
            #print predicted_probability[1]
            #print predicted_probability
            self._file_input_data[templData.temp_col_Predicted] = pd.DataFrame(data=predicted_probability[0:])
            #print self._file_input_data[templData.temp_col_Predicted]
            self.save_csv(predicted_probability,self._file_name)
        except ValueError:
            print "Error: \t wrong input data. DataInput [candidate_email,Employer, Type, Company credit, " \
                  "Current job years, Average time, Seniority] should be a dataframe.\n"
        except AttributeError:
            print "Error: \t wrong attribute errors. Please check correct input Model  and datatype"
        return self._file_input_data

    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "destroyed"

    def save_csv(self,predicted_prob,file_name):
        with open(self._file_predicted_data,'r') as f:
            file_csv=f.readlines()
            print file_csv
            with open(file_name,'wb') as g:
                i=0
                for line in file_csv:
                    if i==0:
                        #file_csv.insert(i,'Predicted')
                        new_line=line.strip()+',Predicted'+'\n'
                        i=i+1
                        g.writelines(new_line)
                    elif line:
                        new_line=line.strip()+','+str(predicted_prob[i-1])+'\n'
                        i=i+1
                        g.writelines(new_line)