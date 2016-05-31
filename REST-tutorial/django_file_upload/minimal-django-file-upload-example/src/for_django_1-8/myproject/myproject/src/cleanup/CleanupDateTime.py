import datetime as dt
import pandas as pd
import src.const.TemplateData as templData

class CleanupDateTime():

    def cleanDateTimeOfDBRawData(self, db_raw_data):
        try:
            if (not isinstance(db_raw_data, pd.DataFrame)):
                raise AttributeError
            for row_index, row in db_raw_data.iterrows():
                start_date = self.validateDateTime(db_raw_data.get_value(row_index, templData.db_col_start_date))
                end_date = self.validateDateTime(db_raw_data.get_value(row_index, templData.db_col_end_date))
                db_raw_data.set_value(row_index, templData.db_col_start_date, start_date)
                db_raw_data.set_value(row_index, templData.db_col_end_date, end_date)
        except AttributeError as err:
            print err
        except ValueError as err:
            print err
        return db_raw_data



    def validateDateTime(self, date_text):
        dateFormats = (
        '%Y', '%b %d, %Y', '%b %d, %Y', '%B %d, %Y', '%B %d %Y', '%m/%d/%Y', '%m/%d/%y', '%b %Y', '%B%Y', '%b %d,%Y', '%Y-%m-%d'
        , '%Y-%m')

        if (not isinstance(date_text, basestring)):
            return ""

        _date = date_text

        if (date_text.upper() == "Present".upper()):
            _date = dt.datetime.now()

        for fmt in dateFormats:
            try:
                _date = dt.datetime.strptime(date_text,fmt)
                break
            except ValueError as err:
                pass

        try:
            _date = _date.date()
        except AttributeError as err:
            print err
            return None
        return _date




