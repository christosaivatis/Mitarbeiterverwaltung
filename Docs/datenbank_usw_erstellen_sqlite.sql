DROP DATABASE
	IF EXISTS Mitarbeiterverwaltung;

CREATE DATABASE Mitarbeiterverwaltung
	DEFAULT CHARACTER SET utf8mb4;
	

CREATE TABLE Abteilung
(
	Abt_ID INTEGER NOT NULL,
	Abt_Bezeichnung TEXT,
	
	PRIMARY KEY (Abt_ID)
);


-- Bsv = Beschaeftigungsverhaeltnis --
CREATE TABLE Bsv 
(
	Bsv_ID INTEGER NOT NULL,
	Bsv_Bezeichnung TEXT,
	
	PRIMARY KEY (Bsv_ID)
);


CREATE TABLE Wohnort
(
	Ort_ID TEXT NOT NULL,
	Ort_Bezeichnung TEXT,
	
	PRIMARY KEY (Ort_ID)
);


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
		FOREIGN KEY (Bsv_Bsv_ID )
			REFERENCES Bsv(Bsv_ID)
);


INSERT INTO Abteilung (Abt_Bezeichnung)
	VALUES ("Buchhaltung"),
		   ("Marketing"),
		   ("Versand"),
		   ("Einkauf");


INSERT INTO Bsv (Bsv_Bezeichnung)
	VALUES ("Freiberufler"),
		   ("Teilzeitangestellte"),
		   ("Vollzeitangestellte"),
		   ("Azubis");


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


INSERT INTO Mitarbeiter (Vorname, Nachname, Geburtsdatum, Strasse, Telefonnummer, Gehalt, StKlasse, Wohnort_Ort_ID, Abteilung_Abt_ID, Bsv_Bsv_ID)
	VALUES ("Peter",     "Willen", 				 "1982-12-12", "Ahornstrasse 15", 		 "0152 02525253",  2200, 3, "10117", 3, 1),
		   ("Hans",      "Miller", 				 "1969-01-23", "Am Berg 36", 			 "0157 82654566",  1400, 3, "10123", 1, 2),
		   ("Franz",     "Müller", 				 "1957-05-10", "Große Strasse 66", 		 "0151 16526482",  2400, 3, "49076", 1, 3),
		   ("Din",       "Schäfer", 			 "1987-05-21", "Ahornstrasse 15", 		 "0153 15645895",  1090, 1, "50667", 4, 4),
		   ("Des",       "Aster", 				 "1982-12-12", "Amselstrasse 45", 		 "0152 01236548",  2800, 4, "59494", 2, 3),
		   ("Carl",      "von Carlovitschovski", "1999-03-31", "An der Ohe 12", 		 "0152 02525253",  2200, 3, "10117", 3, 1),
		   ("Vera",      "Peponopoulopoulou",    "2003-07-15", "Münsterstrasse 14", 	 "0152 02641985",  1090, 1, "59494", 1, 4),
		   ("Christian", "Graf",                 "2002-10-03", "Berlinerstrasse 2", 	 "0152 03564823",   990, 1, "33602", 3, 4),
		   ("Alex",      "Hills",                "1995-01-22", "Kölnerstrasse 88", 		 "0152 04585658",  2200, 1, "44137", 3, 1),
		   ("Dominic",   "Willner",              "1958-12-12", "Soesterstrasse 37", 	 "0152 06524586",  1200, 5, "20457", 3, 2),
		   ("Georgia",   "Ippendorf",            "1960-11-11", "Dortmunderstrasse 55", 	 "0154 84592658",  1200, 5, "56077", 2, 2),
		   ("Holger",    "Lutz",                 "1988-06-15", "Reuterstrasse 65", 		 "0152 15265456",  2500, 3, "10123", 1, 1),
		   ("Luiqwe",     "Nemann",               "1990-08-14", "Klingenhagen 1", 		 "0152 65485685",  3000, 1, "10117", 2, 1),
		   ("Marta",     "Niemann",              "1993-11-22", "Düsseldorferstrasse 22", "0152 45684548",  2200, 3, "10117", 3, 1),
		   ("Katharina", "Grave",                "1958-12-14", "Münchenerstrasse 86", 	 "0150 54464685",  1200, 5, "10117", 4, 1),
		   ("Gregor",    "Tapke",                "1999-01-25", "Bremerstrasse 75", 		 "0157 58415646",  2200, 3, "10123", 3, 1),
		   ("Arno",      "Winter",               "1994-05-17", "Oldenburgerstrasse 43",  "0157 54678546",  1200, 5, "10123", 3, 1),
		   ("Julia",     "Schulz",               "1976-04-23", "Meckenheimer Allee 101", "01525 4783409",  2300, 3, "10123", 4, 3),
		   ("Michael",   "Michailovitsch",       "1983-02-01", "Bonner Str. 1",          "0172 843526648", 1200, 5, "10117", 2, 2),
		   ("Maria",     "Skotolowski",          "1975-01-02", "Kölner Str. 2",          "0153 035622342", 2200, 4, "10117", 3, 1),
		   ("Andreas",   "Kaiser",               "1965-09-28", "Wuppertaler Str. 3",     "0174 23452226",  1400, 3, "20457", 1, 2);


-- 1. Neuer Eintrag Abteilung --
INSERT INTO Abteilung (Abt_Bezeichnung)
	VALUES ("Führung");


-- 2. Neuer Eintrag Beschäftigungsverhältnis --
INSERT INTO Bsv (Bsv_Bezeichnung)
	VALUES ("Minijober");


-- 3. Neuer Eintrag Wohnort --
INSERT INTO Wohnort (Ort_ID, Ort_Bezeichnung)
	VALUES ("53123", "Bonn");


-- 4. Neuer Eintrag Mitarbeiter --
INSERT INTO Mitarbeiter (Vorname, Nachname, Geburtsdatum, Strasse, Telefonnummer, Gehalt, StKlasse, Wohnort_Ort_ID, Abteilung_Abt_ID, Bsv_Bsv_ID)
	VALUES ("Tester", "Testeropoulos", "1987-01-01", "Ahornweg 10", "0152 2222222", 2222, 3, "49076", 3, 1);
	

-- 5. Eintrag ändern Abteilung --
UPDATE Abteilung
	SET Abt_Bezeichnung = "Chefs"
		WHERE Abt_Bezeichnung = "Führung";
		

-- 6. Eintrag ändern Beschäftigungsverhältnis --
UPDATE Bsv
	SET Bsv_Bezeichnung = "Minijobbasis"
		WHERE Bsv_Bezeichnung = "Minijober";


-- 7. Eintrag ändern Wohnort --
UPDATE Wohnort
	SET Ort_Bezeichnung = "Bonn-Duisdorf"
		WHERE Ort_ID = "53123";


-- 8. Eintrag ändern Mitarbeiter --
UPDATE Mitarbeiter
	SET Nachname = "Karpouzopoulopoulou",
		Vorname = "Varvara",
		Geburtsdatum = "1985-02-20",
		Strasse = "Neue Str. 1",
		Telefonnummer = "01525 0123456",
		Gehalt = 2100,
		StKlasse = 5,
		
		Wohnort_Ort_ID = "49076",
		Abteilung_Abt_ID = 3,
		Bsv_Bsv_ID = 1
		WHERE MA_ID = 7;


-- 9. Eintrag in Abteilung löschen --
DELETE FROM Abteilung
	WHERE Abt_Bezeichnung = "Einkauf";


-- 10. Eintrag in Beschäftigungsverhältnis löschen --
DELETE FROM Bsv
	WHERE Bsv_Bezeichnung = "Minijobbasis";


-- 11. Eintrag in Wohnort löschen --
DELETE FROM Wohnort
	WHERE Ort_ID = "53123";


-- 12. Eintrag in Mitarbeiter löschen --
DELETE FROM Mitarbeiter
	WHERE MA_ID = 7;


-- Einträge, usw. abrufen --

-- Ausgabe der Mitarbeiter
SELECT  m.Nachname, m.Vorname, m.Gehalt FROM Mitarbeiter AS m
    ORDER BY m.Nachname ASC;

-- Mitarbeiter der Buchhaltung
SELECT m.Nachname, m.Vorname FROM Mitarbeiter AS m
    WHERE m.Abt_ID = 1 ORDER BY m.Nachname ASC;

-- Gehälter zwischen 2000 - 2500
SELECT m.Nachname, m.Gehalt FROM Mitarbeiter AS m
    WHERE m.Gehalt BETWEEN 2000 AND 2500 ORDER BY m.Gehalt DESC;

-- Nachnamen mit SCH
SELECT m.Nachname FROM Mitarbeiter AS m
    WHERE m.Nachname LIKE "Sch%";

-- Nachname mit mann
SELECT m.Nachname FROM Mitarbeiter AS m
    WHERE m.Nachname LIKE "%mann%";

-- Durchschnittsgehalt
SELECT AVG (m.Gehalt) AS "Durchschnittsgehalt" FROM Mitarbeiter AS m;