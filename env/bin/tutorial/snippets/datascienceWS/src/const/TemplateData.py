# Author : Loan Huynh
# Desc: This file defines constant variable for column name of input data as well as training data

# location of training dataset
loc_training_data = 'data/trainingdata/dataset_07_Apr.csv'

# column's name
temp_col_candidate_id = 'candidate_id'
temp_col_candidate_email = 'candidate_email'
temp_col_employer = 'Employer'
temp_col_company_type = 'Type'
temp_col_company_credit = 'Company credit'
temp_col_current_job_years = 'Current job years'
temp_col_avg_time = 'Average time'
temp_col_seniority = 'Seniority'
temp_col_degree = 'Degree'
temp_col_gender = 'Gender'
temp_col_enthicity = 'Enthicity'
temp_col_Moving = 'Moving'
temp_col_Predicted = 'Predicted'

# columns name in database
db_col_start_date  = "c_employment_job_start"
db_col_end_date = "c_employment_job_end"
db_col_employer_name = "c_employment_employer_name"
db_col_candidate_id = "candidate_id"

# list of dependent columns for prediction model
cols_dep_var = [temp_col_company_type, temp_col_company_credit, temp_col_current_job_years, temp_col_avg_time, temp_col_seniority]