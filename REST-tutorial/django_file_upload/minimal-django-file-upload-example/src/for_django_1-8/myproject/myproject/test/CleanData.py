from src.cleanup.CleanupDateTime import CleanupDateTime
from src.cleanup.CleanMovement import CleanMovement
import  pandas as pd
import src.const.TemplateData as templData
import src.process.WorkingTimeCalculation as w

cl = CleanupDateTime()
test_data = "../data/test/data_test_group_by_employer.csv"
sample_data = pd.read_csv(test_data)
print "111"
# print sample_data
# print  sample_data[templData.col_start_date][1]
# a = cl.cleanDateTimeOfRawData(sample_data)
# a = cl.validateDateTime("1995-05-01")
# print a
cm = CleanMovement()
# employer_name = "Epson Electronics America"
# # employer_data = a.ix[employer_name]
# b = cm.get_start_end_date_of_curr_movement_db(employer_name, sample_data)
# print b

a = w.WorkingTimeCalculation()
print type(sample_data)
test = a.cal_avg_time_movement_db(sample_data)
print test



