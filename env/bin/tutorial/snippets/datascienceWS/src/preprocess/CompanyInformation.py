# Author: LoanHuynh
# Date:
# Desc: this script calculate company factors for prediction

import src.dbconnect.ConnectionInformation as connInfo
# from elasticsearch import Elasticsearch
import elasticsearch
from elasticquery import ElasticQuery, Query
from src.dbconnect.QueryData import query_fortune_company as fortune_company
import src.util.DataProcessing as dp

class CompanyCreditAndType:

    def __init__(self, company_name):
        self.company_name = company_name

    def calculateCompanyCreditAndType(self):
        # Step 1: Search Company in fortune
        # Fortune top: 2, Size>1000 : 1, Other : 0
        company_credit = 0
        es_company_type, es_company_size = self.getCompanyTypeAndSizeByES(self.company_name)
        print es_company_size
        print es_company_type
        print type(es_company_type)
        company_type = self.covertCompanyTypeToDepedentValueInModel(es_company_type)
        if (fortune_company(self.company_name) >= 1):
            company_credit = 2
        else :
            company_credit = self.covertCompanySizeToDepedentValueInModel(es_company_size)
        return company_credit, company_type

    
    def getCompanyTypeAndSizeByES(self, company_name):
        # result = []
        company_type = None
        company_size = None
        try :
            es = elasticsearch.Elasticsearch([{'host': connInfo.esHost, 'port': connInfo.esPort}])
            print (es.info)
            query = {"query": {
                                    "multi_match": {
                                        "query" : company_name,
                                        "fields": ["name"]
                                    }
                                }}
            result = es.search(body=query, index= 'vsprofile', doc_type= connInfo.es_type_company)['hits']['hits']
            if result:
                company_type = result[0]['_source']['type']
                company_size = result[0]['_source']['size']
                # print company_type
                # print company_size

        except Exception as err:

            print err

        return str(company_type), str(company_size)

    # Convert Company Size to Dependent Variable
    # Size > 1000 = 1; Other : 0
    def covertCompanySizeToDepedentValueInModel(self, company_size):
        if company_size == "" or company_size is None:
            return 0
        if not (dp.isStringContainNumber(company_size)):
            return 0
        str_company_size = company_size[company_size.find("-")+1:company_size.find(" ")]
        str_company_size = str_company_size.split("+", 1)
        int_company_size = int(str_company_size[0])
        # print int_company_size
        if int_company_size >= 1000:
            return 1
        else:
            return 0

    # Convert Company Type to Dependent Variable
    # TypeOfCompany:  Other(2) ; Public(0) ; Private(1)
    def covertCompanyTypeToDepedentValueInModel(self, company_type):
        company_type = company_type.upper()
        if company_type.find("PUBLIC"):
            return 0
        else :
            if company_type.find("PRIVATE"):
                return 1
            else :
                return 2