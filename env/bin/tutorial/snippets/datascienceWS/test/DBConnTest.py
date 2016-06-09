import src.const.TemplateData as templData
import src.dbconnect.DBConnection as conn
from src.preprocess.CompanyInformation import CompanyCreditAndType
# a = com.CompanyInformation()
# com_name = "Glandore"
# b = a.getCompanyTypeAndSizeByES(com_name)
# print b
#
# # company_size = "10,001+ employees" #1-10 employees
# # company_size ="1-10 employees"
# company_size = ""
# print a.covertCompanySizeToDepedentValueInModel(company_size)

# import src.dbconnect.python_mysql_dbconfig as pyconn

import src.dbconnect.QueryData as queryData
#
# a = queryData.query_fortune_company("Google")
# print a
#
# candidate_email = "mazunguu@gmail.com"
# employer = "Epson Electronics America"
#
# b = queryData.query_candidate_info_by_employer(candidate_email, employer)
# from src.preprocess.CompanyInformation import CompanyCreditAndType
#
a = CompanyCreditAndType("Kings College Hospital")

b = a.calculateCompanyCreditAndType()
print b
# print type(b)
# print b[templData.db_col_employer_name]
import re