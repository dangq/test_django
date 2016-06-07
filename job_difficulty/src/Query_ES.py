import connInfo
import elasticsearch
#print connInfo.esHost


def getCompanyTypeAndSizeByES(profile_name):
    # result = []
    profile_skill = []
    #company_size = None
    try :
        es = elasticsearch.Elasticsearch([{'host': connInfo.esHost, 'port': connInfo.esPort}])
        #print (es.info)
        query = {"query": {
                            "multi_match": {
                            "query" :  ,
                            "fields": ["full_name"]
                                            }
                            }
                }
        results = es.search(body=query, index= 'vsprofile', doc_type= connInfo.es_type_profile)['hits']['hits']

        print results[0]
        for i in range(0,len(results)):
            #print results[i]
            #if result:
            #print result['_source']
            profile_skill.append(results[i]['_source']['skills'])
                #company_size = result[0]['_source']['size']
        # print company_type
        # print company_size
    except Exception as err:
        print err
    return str(profile_skill)\
        #, str(company_size)\

getCompanyTypeAndSizeByES('James')