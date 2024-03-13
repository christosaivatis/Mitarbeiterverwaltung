import sqlite3
import os.path


# Verbindung mit Datenbank erstellen bzw. die Datenbank zuerst erstellen 
connection = sqlite3.connect("mitarbeiterverwaltung.db")


try:
    cursor = connection.cursor()

    sql_statement = """
    INSERT INTO Abteilung (Abt_Bezeichnung)
	VALUES ("Buchhaltung"),
               ("Marketing"),
	       ("Versand"),
	       ("Einkauf");
    """
    cursor.execute(sql_statement)
    connection.commit()

    sql_statement = """
    INSERT INTO Bsv (Bsv_Bezeichnung)
	VALUES ("Freiberufler"),
               ("Teilzeitangestellte"),
               ("Vollzeitangestellte"),
               ("Azubis");
    """
    cursor.execute(sql_statement)
    connection.commit()

    sql_statement = """
    INSERT INTO Wohnort (Ort_ID, Ort_Bezeichnung)
	VALUES ("10117", "Berlin"),
               ("10123", "Berlin"),
               ("49076", "Osnabrück"),
               ("50667", "Köln"),
               ("59494", "Soest"),
               ("33602", "Bielefeld"),
               ("44137", "Dortmund"),
               ("20457", "Hamburg"),
               ("56077", "Koblenz");
    """
    cursor.execute(sql_statement)
    connection.commit()

    sql_statement = """
    INSERT INTO Mitarbeiter (Vorname, Nachname, Geburtsdatum, Strasse, Telefonnummer, Gehalt, StKlasse, Wohnort_Ort_ID, Abteilung_Abt_ID, Bsv_Bsv_ID)
	VALUES ("Peter",     "Willen", 		     "1982-12-12", "Ahornstrasse 15", 	     "0152 02525253",  2200, 3, "10117", 3, 1),
               ("Hans",      "Miller", 		     "1969-01-23", "Am Berg 36", 	     "0157 82654566",  1400, 3, "10123", 1, 2),
               ("Franz",     "Müller", 		     "1957-05-10", "Große Strasse 66", 	     "0151 16526482",  2400, 3, "49076", 1, 3),
               ("Din",       "Schäfer", 	     "1987-05-21", "Ahornstrasse 15", 	     "0153 15645895",  1090, 1, "50667", 4, 4),
               ("Des",       "Aster", 		     "1982-12-12", "Amselstrasse 45", 	     "0152 01236548",  2800, 4, "59494", 2, 3),
               ("Carl",      "von Carlovitschovski", "1999-03-31", "An der Ohe 12", 	     "0152 02525253",  2200, 3, "10117", 3, 1),
               ("Vera",      "Peponopoulopoulou",    "2003-07-15", "Münsterstrasse 14",      "0152 02641985",  1090, 1, "59494", 1, 4),
               ("Christian", "Graf",                 "2002-10-03", "Berlinerstrasse 2",      "0152 03564823",   990, 1, "33602", 3, 4),
               ("Alex",      "Hills",                "1995-01-22", "Kölnerstrasse 88", 	     "0152 04585658",  2200, 1, "44137", 3, 1),
               ("Dominic",   "Willner",              "1958-12-12", "Soesterstrasse 37",      "0152 06524586",  1200, 5, "20457", 3, 2),
               ("Georgia",   "Ippendorf",            "1960-11-11", "Dortmunderstrasse 55",   "0154 84592658",  1200, 5, "56077", 2, 2),
               ("Holger",    "Lutz",                 "1988-06-15", "Reuterstrasse 65", 	     "0152 15265456",  2500, 3, "10123", 1, 1),
               ("Luiqwe",     "Nemann",              "1990-08-14", "Klingenhagen 1", 	     "0152 65485685",  3000, 1, "10117", 2, 1),
               ("Marta",     "Niemann",              "1993-11-22", "Düsseldorferstrasse 22", "0152 45684548",  2200, 3, "10117", 3, 1),
               ("Katharina", "Grave",                "1958-12-14", "Münchenerstrasse 86",    "0150 54464685",  1200, 5, "10117", 4, 1),
               ("Gregor",    "Tapke",                "1999-01-25", "Bremerstrasse 75", 	     "0157 58415646",  2200, 3, "10123", 3, 1),
               ("Arno",      "Winter",               "1994-05-17", "Oldenburgerstrasse 43",  "0157 54678546",  1200, 5, "10123", 3, 1),
               ("Julia",     "Schulz",               "1976-04-23", "Meckenheimer Allee 101", "01525 4783409",  2300, 3, "10123", 4, 3),
               ("Michael",   "Michailovitsch",       "1983-02-01", "Bonner Str. 1",          "0172 843526648", 1200, 5, "10117", 2, 2),
               ("Maria",     "Skotolowski",          "1975-01-02", "Kölner Str. 2",          "0153 035622342", 2200, 4, "10117", 3, 1),
               ("Andreas",   "Kaiser",               "1965-09-28", "Wuppertaler Str. 3",     "0174 23452226",  1400, 3, "20457", 1, 2);
    """
    cursor.execute(sql_statement)
    connection.commit()

except Exception as e:
    print("Es ist folgender Fehler aufgetreten: \n" + e.args[0])

finally:
    connection.close()
