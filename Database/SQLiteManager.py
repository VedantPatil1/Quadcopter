import sqlite3

from sqlalchemy import column
#from ..config import databaseConnectionForSQLite, ComponentConfig


databaseConnection = "Database/Drone.db"  # databaseConnectionForSQLite  #
#TableConfig = ComponentConfig


class Database:
    def __init__(self):
        self.Name = databaseConnection
        self.Tables = {
            "Motor":   {"codeName": "TEXT", "weight": "INTEGER", "cost": "INTEGER"},
            "Propeller":   {"codeName": "Text", "weight": "INTEGER", "pitch": "REAL", "diameter": "REAL"},
            "ESC":   {"codeName": "TEXT", "weight": "INTEGER", "cost": "INTEGER"},
            "Battery":   {"codeName": "TEXT", "weight": "INTEGER", "cost": "INTEGER"},
            "Flight Controller":   {"codeName": "TEXT", "weight": "INTEGER", "cost": "INTEGER"},
            "PDM":   {"codeName": "TEXT", "weight": "INTEGER", "cost": "INTEGER"},
            "Frame":   {"codeName": "TEXT", "weight": "INTEGER", "cost": "INTEGER"},
            "Reciever":   {"codeName": "TEXT", "weight": "INTEGER", "cost": "INTEGER"},
            "Transmitter":   {"codeName": "TEXT", "weight": "INTEGER", "cost": "INTEGER"},
            "GPS":   {"codeName": "TEXT", "weight": "INTEGER", "cost": "INTEGER"},
            "Camera":   {"codeName": "TEXT", "weight": "INTEGER", "cost": "INTEGER"},
            "Sprinkler":   {"codeName": "TEXT", "weight": "INTEGER", "cost": "INTEGER"}
        }    # Holds objects of the class Table in the database
        conn = sqlite3.connect(self.Name)
        self.cur = conn.cursor()

    class Table:
        # name of table and names of column in {"name":"type"}
        def __init__(self, tableName, columns):
            self.tableName = tableName
            self.columns = columns
            self.Rows = {}  # Holds objects of class Row in the table

        def CreateTableInSqliteCommand(self):
            command = "CREATE TABLE IF NOT EXISTS " + self.tableName + " ("
            for column in self.columns:
                command = command + column + " " + self.columns[column] + ", "
            command = command + ")"
            return command

        class Row:
            def __init__(self, record):
                for elementKey in record:
                    setattr(self, elementKey, record[elementKey])

        def AddRecord(self, RowId, record):
            self.Rows[RowId] = self.Row(record)

    def CreateTable(self, tableName, columns):
        self.Tables[tableName] = (self.Table(tableName, columns))

    def RunInitialConfig(self):
        for table in self.Tables:
            print(table)
            self.CreateTable(table, self.Tables[table])
            table.Create
