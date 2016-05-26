# Author: LoanHuynh
# Date : 23 May 2016
# Desc: this class calculates currentTime and AverageTime of each movement

from datetime import datetime as dt
from src.cleanup.CleanupDateTime import CleanupDateTime
from src.util.DateProcessing import convertStrDateToDate as strToDate
import src.const.TemplateData as templData
import pandas as pd
import numpy as numpy

class WorkingTimeCalculation():

    # Calculate current time of movement.
    # Input: start_date and end_date with format "%Y-%m%d"
    def cal_curr_time_movement(self, start_date, end_date):
        try:
            start_date = strToDate(start_date)
            end_date = strToDate(end_date)
            diff_date = round((end_date-start_date).days/365.5,2)
        except AttributeError as err:
            print  err
            print "Please input date by format '%Y-%m-%d'"
        return diff_date

    # This function calculate Average Time for Each Movement based on data loading in Database
    def cal_avg_time_movement_db(self, list_employers_of_candidate):
        new_data = list_employers_of_candidate
        try :
            cleanDate = CleanupDateTime()
            # Clean up Data
            cleaned_data  = cleanDate.cleanDateTimeOfDBRawData(list_employers_of_candidate)
            # Calculate current time of each employer
            new_data = self.cal_curr_time_employer_db(cleaned_data)
            new_Avg_data= new_data.groupby(templData.db_col_candidate_id, as_index= False).agg({
                templData.temp_col_current_job_years: numpy.mean})
            new_Avg_data = new_Avg_data.rename(columns={templData.temp_col_current_job_years:templData.temp_col_avg_time})
            new_data = pd.merge(new_data, new_Avg_data, how='left', on=[templData.db_col_candidate_id, templData.db_col_candidate_id])
        except AttributeError as err:
            print err

        return new_data

    def cal_curr_time_employer_db(self, list_employers_of_candidate):
        try:
            list_employers_of_candidate[templData.temp_col_current_job_years] = 0
            for row_index, row in list_employers_of_candidate.iterrows():
                curr_date = self.cal_curr_time_movement(list_employers_of_candidate.get_value(row_index, templData.db_col_start_date),
                                                        list_employers_of_candidate.get_value(row_index, templData.db_col_end_date))
                list_employers_of_candidate.set_value(row_index, templData.temp_col_current_job_years, curr_date)
        except AttributeError as err:
            print err
        except ValueError as err:
            print err

        return list_employers_of_candidate

    def __setitem__(self, key, value):
        self.values[key] = value





