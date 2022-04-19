import sqlalchemy 
import pandas
import os

def appendAllCsv(directoryPath, outputCsv, headers = None):
    csvFiles = []

    if os.path.exists(directoryPath):
         for file in os.scandir(directoryPath):
             if file.name.endswith('.csv'):
                 csvFiles.append(file.path)
    
    appendedCsv = pandas.concat([pandas.read_csv(csv, header = headers) for csv in csvFiles])
    appendedCsv.to_csv(outputCsv, index = False, header = headers)

    return appendedCsv

def csvToSqlLite(csv, tableName, dbPath, headers = None):
    engine = sqlalchemy.create_engine(getformattedSqlitePath(dbPath), echo=False)
    csvDf = pandas.read_csv(csv, header = headers) 
    csvDf.to_sql(tableName, con=engine)


def readSqliteTable(dbPath, tableName):
    engine = sqlalchemy.create_engine(getformattedSqlitePath(dbPath), echo=False)
    print(engine.execute("SELECT * FROM " + tableName).fetchall())


def getformattedSqlitePath(dbPath):
    return r'sqlite:///' + dbPath