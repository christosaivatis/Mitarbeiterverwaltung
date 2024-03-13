import sqlite3
import os.path


# Verbindung mit Datenbank erstellen bzw. die Datenbank zuerst erstellen 
connection = sqlite3.connect("mitarbeiterverwaltung.db")


try:
    cursor = connection.cursor()

    clean_up = "DROP TABLE IF EXISTS Abteilung;"
    sql_statement = """
    CREATE TABLE Abteilung
    (
        Abt_ID INTEGER NOT NULL,
        Abt_Bezeichnung TEXT,
	
        PRIMARY KEY (Abt_ID)
    );
    """
    cursor.execute(sql_statement)
    connection.commit()

    clean_up = "DROP TABLE IF EXISTS Bsv;"
    sql_statement = """
    CREATE TABLE Bsv
    (
        Bsv_ID INTEGER NOT NULL,
        Bsv_Bezeichnung TEXT,
	
        PRIMARY KEY (Bsv_ID)
    );
    """
    cursor.execute(sql_statement)
    connection.commit()

    clean_up = "DROP TABLE IF EXISTS Wohnort;"
    sql_statement = """
    CREATE TABLE Wohnort
    (
        Ort_ID TEXT NOT NULL,
        Ort_Bezeichnung TEXT,
	
        PRIMARY KEY (Ort_ID)
    );
    """
    cursor.execute(sql_statement)
    connection.commit()

    clean_up = "DROP TABLE IF EXISTS Mitarbeiter;"
    sql_statement = """
    CREATE TABLE Mitarbeiter
    (
        MA_ID INTEGER NOT NULL,
        Nachname TEXT,
        Vorname TEXT,
        Geburtsdatum DATE,
        Strasse TEXT,
        Telefonnummer TEXT,
        Gehalt REAL,
        StKlasse INTEGER,
            
        Wohnort_Ort_ID TEXT,
        Abteilung_Abt_ID INTEGER,
        Bsv_Bsv_ID INTEGER,
            
        PRIMARY KEY (MA_ID),
            
        CONSTRAINT Verbindung_Mitarbeiter_Wohnort
            FOREIGN KEY (Wohnort_Ort_ID)
                REFERENCES Wohnort(Ort_ID),

        CONSTRAINT Verbindung_Mitarbeiter_Abteilung
            FOREIGN KEY (Abteilung_Abt_ID)
                REFERENCES Abteilung(Abt_ID),

        CONSTRAINT Verbindung_Mitarbeiter_Bsv
            FOREIGN KEY (Bsv_Bsv_ID)
                REFERENCES Bsv(Bsv_ID)
    );
    """
    cursor.execute(sql_statement)
    connection.commit()

except Exception as e:
    print("Es ist folgender Fehler aufgetreten: \n" + e.args[0])

finally:
    connection.close()
