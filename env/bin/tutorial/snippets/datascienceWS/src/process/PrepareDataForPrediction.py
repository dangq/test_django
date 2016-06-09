# Author: Loan Huynh
# Date: 31 May 2016
# Description: process Input Data to get information for prediction
import src.const.TemplateData as templData
from src.preprocess.WorkingTimeCalculation import WorkingTimeCalculation
from src.preprocess.CompanyInformation import CompanyCreditAndType
import src.dbconnect.QueryData as queryData
from src.cleanup.CleanMovement import CleanMovement
import pandas as pd
import numpy as numpy

class DataForCandidateMovement:

    def process_input_data(self, inputData):
        try :
            if (templData.temp_col_company_type in inputData.columns) and \
                    (templData.temp_col_avg_time in inputData.columns) and \
                    (templData.temp_col_company_credit in inputData.columns) and \
                    (templData.temp_col_current_job_years in inputData.columns):
                return inputData

            workTime = WorkingTimeCalculation()
            cleanmove = CleanMovement()
            inputData[templData.temp_col_avg_time] = 0.0
            inputData[templData.temp_col_current_job_years] = 0.0
            inputData[templData.temp_col_company_type] = 0
            inputData[templData.temp_col_company_credit] = 0
            for row_index, row in inputData.iterrows():
                employer = inputData.get_value(row_index, templData.temp_col_employer)
                candidate_email = inputData.get_value(row_index, templData.temp_col_candidate_email)
                comInfo = CompanyCreditAndType(employer)
                comp_credit, comp_type = comInfo.calculateCompanyCreditAndType()
                employer_data = queryData.query_candidate_info_by_employer(candidate_email, employer)
                curr_time =  None
                avg_time = None
                if not employer_data.empty :
                    start_date, end_date = cleanmove.get_start_end_date_of_curr_movement_db(employer_name= employer,
                                                                                                 list_employers_of_candidate= employer_data)
                    curr_time = workTime.cal_curr_time_movement(start_date, end_date)
                    avg_time= workTime.get_avg_time_value(employer_data)
                inputData.set_value(row_index, templData.temp_col_current_job_years, curr_time)
                inputData.set_value(row_index, templData.temp_col_avg_time, avg_time)
                inputData.set_value(row_index, templData.temp_col_company_credit, comp_credit)
                inputData.set_value(row_index, templData.temp_col_company_type, comp_type)

        except AttributeError as err:
            print err

        return self.removeNaNValue(inputData)

    def removeNaNValue(self, dataframe):
        return dataframe.dropna()




