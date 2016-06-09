from  elasticsearch import Elasticsearch
import ConnectionInformation as connInfo

from mysql.connector import MySQLConnection, Error
from configparser import ConfigParser



    # def __init__(self, section):
    #     self.section = section
    #
    # def connect(self):
    #     """ Connect to MySQL database """
    #
    #     db_config = self.read_db_config(self.section)
    #     # conn = None
    #     try:
    #         print('Connecting to MySQL database...')
    #         conn = MySQLConnection(**db_config)
    #
    #         if conn.is_connected():
    #             print('connection established.')
    #         else:
    #             print('connection failed.')
    #
    #     except Error as error:
    #         print(error)
    #
    #     finally:
    #         conn.close()
    #         print('Connection closed.')


def read_db_config(section, filename=connInfo.configInfo):
    """ Read database configuration file and return a dictionary object
    :param filename: name of the configuration file
    :param section: section of database configuration
    :return: a dictionary of database parameters
    """
    # create parser and read ini configuration file
    parser = ConfigParser()
    parser.read(filename)

    # get section, default to mysql
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))
    return db

