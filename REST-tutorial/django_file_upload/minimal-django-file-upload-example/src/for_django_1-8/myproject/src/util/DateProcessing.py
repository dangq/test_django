from datetime import  datetime as dt

def convertStrDateToDate(_date):
    if (isinstance(_date, basestring)):
        return dt.strptime(_date, "%Y-%m-%d").date()
    else :
        return _date