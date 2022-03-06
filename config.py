databaseConnectionForSQLite = 'Drone.db'

ComponentConfig = { 
                   "Motor":{ "codeName":"TEXT", "weight":"INTEGER", "cost" : "INTEGER" },
                   "Propeller":{ "codeName":"Text", "weight":"INTEGER", "pitch":"REAL", "diameter":"REAL" },
                   "Battery":{ "":"",  }
                   }













"""
INTEGER. The value is a signed integer, stored in 0, 1, 2, 3, 4, 6, or 8 bytes depending on the magnitude of the value.
eg:-(1,20,50,65889)


REAL. The value is a floating point value, stored as an 8-byte IEEE floating point number.
eg:-(0.1,21.0,555.26)


TEXT. The value is a text string, stored using the database encoding (UTF-8, UTF-16BE or UTF-16LE).
eg:-(my name, is, oh wait i , FORGOT !!!)

"""