import os 
import datahelper

DIR_WORKING = os.path.dirname(__file__)
SETTINGS_FILE = os.path.join(DIR_WORKING, 'settings.csv')
DIR_APPEND_DEMO = os.path.join(DIR_WORKING, 'AppendCsvDemoFiles')
APPEND_DEMO_FILE = os.path.join(DIR_APPEND_DEMO, "AppendedFile", "settings_combined.csv")
SQLITE_DEMO_DB = os.path.join(DIR_WORKING, 'Sqlite_Demo', "demo_db.db")

def main():
    #pass
    #settings = pandas.read_csv(SETTINGS_FILE, header=None, dtype={0: str}).set_index(0).squeeze().to_dict()
    # datahelper.appendAllCsv(DIR_APPEND_DEMO, APPEND_DEMO_FILE)
    # datahelper.csvToSqlLite(APPEND_DEMO_FILE, "settings", SQLITE_DEMO_DB)
    datahelper.readSqliteTable(SQLITE_DEMO_DB, "settings")

if __name__ == "__main__":
    main()
