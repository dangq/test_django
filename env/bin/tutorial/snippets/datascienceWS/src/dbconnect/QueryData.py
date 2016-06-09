from _mysql_exceptions import Error

import ConnectionInformation as connInfo
import src.dbconnect.SQLQueries as query
from pandas import DataFrame as df
import pandas.io.sql as psql

# from mysql.connector import MySQLConnection, Error
import MySQLdb
from DBConnection import read_db_config

def query_fortune_company(company_name):
    rs = 0
    try:
        """ Connect to MySQL database """
        db_config = read_db_config("vsource")
        conn = MySQLdb.connect(host=connInfo.host_dadb,
                               user=connInfo.user_dadb,
                               passwd=connInfo.password_dadb,
                               db=connInfo.dbname_dadb)
        if (conn):
            print "Connect successful"
        else :
            print "Connect Failed"
        #Create a cursor
        cursor = conn.cursor()
        aquery = query.query_fortune_company % company_name
        cursor.execute(aquery)
        rs = cursor.fetchone()[0]

    except Error as error:
        print error

    finally:
        cursor.close
        conn.close
        print('Connection closed.')
    return int(rs)

def query_candidate_info_by_employer(candidate_email, employer_name):
    rs = 0
    start_date = None
    end_date = None
    try:
        """ Connect to MySQL database """
        db_config = read_db_config("vsource")
        conn = MySQLdb.connect(host=connInfo.host_vsource,
                               user=connInfo.user_vsource,
                               passwd=connInfo.password_vsource,
                               db=connInfo.dbname_vsource)
        if (conn):
            print "Connect successful"
        else:
            print "Connect Failed"
        # Create a cursor
        cursor = conn.cursor()
        # a = query.query_candidate_data_by_email_employer % (candidate_email, employer_name)
        # cursor.execute(a)
        # rs = cursor.fetchall()
        rs = psql.read_sql_query(query.query_candidate_data_by_email_employer, con= conn,
                                 params= {"can_email":candidate_email, "can_emp_name": employer_name})

    except Error as error:
        print error

    finally:
        cursor.close
        conn.close
        print('Connection closed.')
    return rs
# if __name__ == '__main__':
#     query_fortune_company()