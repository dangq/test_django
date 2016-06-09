# Author: LoanHuynh
# Date : 23 May 2016
# Desc: this class calculates currentTime and AverageTime of each predict

from datetime import datetime as dt
from src.cleanup.CleanupDateTime import CleanupDateTime
from src.util.DataProcessing import convertStrDateToDate as strToDate
import src.const.TemplateData as templData
import pandas as pd
import numpy as numpy

class WorkingTimeCalculation():
    # Calculate current time of predict.
    # Input: start_date and end_date with format "%Y-%m%d"
    def cal_curr_time_movement(self, start_date, end_date):
        try:
            start_date = strToDate(start_date)
            end_date = strToDate(end_date)
            diff_date = round((end_date-start_date).days/365.5,2)
            # print "Current_time"
            # print diff_date
        except AttributeError as err:
            print  err
            print "Please input date by format '%Y-%m-%d'"
        return diff_date

    # This function calculate Average Time for Each Candidate based on data loaded from Database
    # @return: a new_data_frame contains average time
    def cal_avg_time_candidate_db(self, list_employers_of_candidate):
        new_data = list_employers_of_candidate
        avg_time = 0
        try :
            cleanDate = CleanupDateTime()
            # Clean up Data
            cleaned_data  = cleanDate.cleanDateTimeOfDBRawData(list_employers_of_candidate)
            # Calculate current time of each employer
            new_data = self.cal_curr_time_employer_db(cleaned_data)
            new_Avg_data= new_data.groupby(templData.db_col_candidate_id, as_index= False).agg({
                templData.temp_col_current_job_years: numpy.mean}) # result of Avg_time is saved in Current_time column
            new_Avg_data = new_Avg_data.rename(columns={templData.temp_col_current_job_years:templData.temp_col_avg_time}) # Rename column
            new_data = pd.merge(new_data, new_Avg_data, how='left', on=[templData.db_col_candidate_id, templData.db_col_candidate_id])
            avg_time = new_Avg_data.get_value(0, templData.temp_col_avg_time)
        except AttributeError as err:
            print err
        return new_data, avg_time

    def get_avg_time_value(self, list_employers_of_candidate ):
        new_data, avg_time = self.cal_avg_time_candidate_db(list_employers_of_candidate)
        return avg_time

    # This function calculate current time of employer
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

    # def get_start_end_time_for_movement(self, list_employers_of_candidates):
    #     try :
    #         for row_index, row in list_employers_of_candidates.iterrows():
    #
    #     except AttributeError as err:
    #         print err
    #     except ValueError as err:
    #         print err

    def __setitem__(self, key, value):
        self.values[key] = value





