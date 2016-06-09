# Author: Loan Huynh
# Date : 22- May- 2016
# Desc: this file contains functions to calculate prediction result for candidate predict based on model which is defined in "model" folder

import pandas as pd
import numpy as numpy
import src.const.TemplateData as templData
from sklearn.linear_model import LogisticRegression
from src.util import DataProcessing as dt
from src.process.PrepareDataForPrediction import DataForCandidateMovement

class CandidateMovementPrediction():
    def __init__(self, model, _file_predicted_data,_file_name,):
        self._file_name=_file_name
        self.model = model
        self._file_predicted_data=_file_predicted_data

        try:
            loaded_data = pd.read_csv(_file_predicted_data, sep=',')
            preparedData = DataForCandidateMovement()
            self._file_input_data = preparedData.process_input_data(loaded_data)
            # print self._file_input_data
        except IOError:
            print "Error:\t File doesnot exist "
        except AttributeError:
            print "Error: \t Missing attributes"
        # print "create instance for CandidateMovement"

    # function to calculate the probability of predict prediction
    def calProbMovementPrediction(self):
        json_str =[]
        try:
            # predicted_probability = self.model.predict_proba(self._file_input_data[templData.cols_dep_var])[:, 1]
            predicted_probability = self.model.predict_proba(self._file_input_data[templData.cols_dep_var])[:,1]
            self._file_input_data[templData.temp_col_Predicted] = pd.DataFrame(data=predicted_probability[0:])
            json_str = dt.save_df_json(self._file_input_data)
        except ValueError as err:
            # if numpy.any(numpy.isnan(self._file_input_data)):
            #     pass
            print "Error: \t wrong input data. DataInput [candidate_email,Employer, Type, Company credit, " \
                  "Current job years, Average time, Seniority] should be a dataframe.\n"
            pass
        except AttributeError:
            print "Error: \t wrong attribute errors. Please check correct input Model  and datatype"
        # return self._file_input_data,self._file_csv
        return self._file_input_data, json_str

    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "destroyed"



    # Author: An Dang
    # save dataframe to csv
    def save_csv(self,predicted_prob,file_name):
        with open(self._file_predicted_data,'r') as f:
            file_csv=f.readlines()
            file=[]
            with open(file_name,'wb') as g:
                i=0
                for line in file_csv:
                    if i==0:
                        #file_csv.insert(i,'Predicted')
                        new_line=line.strip()+',Predicted'+'\n'
                        file.append(new_line)
                        i=i+1
                        g.writelines(new_line)
                    elif line:
                        new_line=line.strip()+','+str(predicted_prob[i-1])+'\n'
                        i=i+1
                        file.append(new_line)
                        g.writelines(new_line)
        return file

    def __unicode__(self):
        return unicode(self.some_field) or u''