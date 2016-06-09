from datetime import  datetime as dt
import re

def convertStrDateToDate(_date):
    if (_date =='None') or (_date is None) :
        return dt.now().date()
    if (isinstance(_date, basestring)):
        return dt.strptime(_date, "%Y-%m-%d").date()
    else :
        return _date

def save_df_json(df_data):
    json_str = []
    try:
        json_str = df_data.to_json(orient="records")
    except AttributeError as err:
        print err
    return json_str

def isStringContainNumber(string):
    return any(i.isdigit() for i in string)

def convertDataFrameIntoLists(dataframe):
    l = map(list, dataframe.values)
    return l

def convertAListIntoDataFrame(list):
    print "dataframe"