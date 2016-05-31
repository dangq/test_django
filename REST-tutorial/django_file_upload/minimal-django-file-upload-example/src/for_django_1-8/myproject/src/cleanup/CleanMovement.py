# Author: Loan Huynh
# Date : 23-05-2016
# Desc: this file process to clean factors of Movement: start_date, end_date...
import pandas as pd
from datetime import date
from datetime import datetime as dt
import src.const.TemplateData as templData
from src.cleanup.CleanupDateTime import CleanupDateTime
from src.util.DateProcessing import convertStrDateToDate as strToDate

class CleanMovement(object):

    # This function to get Start Date and End Date of Movement based on data loading from Database
    def get_start_end_date_of_curr_movement_db(self, employer_name, list_employers_of_candidate):
        # index_start_date_movement = 0
        # index_end_date_movement = 0
        cleanDate = CleanupDateTime()
        new_start_date = None
        new_end_date = None
        try :
            if (not isinstance(list_employers_of_candidate, pd.DataFrame)):
                raise AttributeError
            new_end_date = cleanDate.validateDateTime(list_employers_of_candidate.get_value(0, templData.db_col_end_date))
            for row_index, row in  list_employers_of_candidate.iterrows():
                if (list_employers_of_candidate.get_value(row_index, templData.db_col_employer_name).upper() == employer_name.upper()):
                    start_date_curr = cleanDate.validateDateTime(list_employers_of_candidate.get_value(row_index, templData.db_col_start_date))
                    end_date_past = cleanDate.validateDateTime(list_employers_of_candidate.get_value(row_index + 1, templData.db_col_end_date))
                    if (not None in (start_date_curr, end_date_past)):
                        diff_date = (strToDate(start_date_curr) - strToDate(end_date_past)).days
                        if diff_date >= 45 :
                            # index_start_date_movement = row_index
                            new_start_date = start_date_curr
                            break
                    else:
                        # index_start_date_movement = row_index
                        new_start_date = start_date_curr
                        break

        except AttributeError as err:
            print err
            print "Input  Employers_data_of_candidate  is a dataframe"
        except ValueError as err:
            print err

        return (str(new_start_date), str(new_end_date))
