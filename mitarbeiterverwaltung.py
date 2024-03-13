# HANGMAN-SPIEL (GANGELMÄNNCHEN)
# made by Chris
# TODO: Sehr viel Refactoring notwendig,
#  da im Moment die "Clean Code"-Grundsätze verletzt werden!
#  (z.B. Code-Wiederholungen in gesonderten Funktionen auslagern)
# TODO: Verschiedene Fehleingaben abfangen.

import sqlite3


program_header = '''
{-------------------------------------------------------------}
{                                                             }
{                   mitarbeiterverwaltung.py                  }
{                                                             }
{-------------------------------------------------------------}
'''


error_header = '''
???????????????????????????????????????????????????????????
?                                                         ?
?           Da ist was schief gelaufen, sorry...          ?
?           Damit Sie den Fehler beheben können,          ?
?               wäre es vielleicht sinnvoll,              ?
?       wenn Sie anfangen, Programmierung zu lernen!      ?
?         Das Programm wird jetzt neu gestartet...        ?
?                                                         ?
???????????????????????????????????????????????????????????
'''


############################################################################
#                              EINTRAGEN Abteilung                         #
############################################################################

def newEntryAbt(name):    
    connection = sqlite3.connect("mitarbeiterverwaltung.db")
    try:
        cursor = connection.cursor()
        sql_statement = "INSERT INTO Abteilung (Abt_Bezeichnung) " \
                            "VALUES (" + '"' + name + '"' + ");"
        cursor.execute(sql_statement)
        connection.commit()
    except Exception as e:
        print("Es ist folgender Fehler aufgetreten: \n" + e.args[0])
    finally:
        connection.close()
        
    return ######################


############################################################################
#                    EINTRAGEN Beschäftigungsverhältnis                    #
############################################################################ 

def newEntryBsv(name): 
    connection = sqlite3.connect("mitarbeiterverwaltung.db")
    try:
        cursor = connection.cursor()
        sql_statement = "INSERT INTO Bsv (Bsv_Bezeichnung) " \
                            "VALUES (" + '"' + name + '"' + ");"
        cursor.execute(sql_statement)
        connection.commit()
    except Exception as e:
        print("Es ist folgender Fehler aufgetreten: \n" + e.args[0])
    finally:
        connection.close()
        
    return ######################

    
############################################################################
#                               EINTRAGEN Wohnort                          #
############################################################################ 

def newEntryOrt(plz, name):
    connection = sqlite3.connect("mitarbeiterverwaltung.db")
    try:
        cursor = connection.cursor()
        
        sql_statement = "INSERT INTO Wohnort (Ort_ID, Ort_Bezeichnung) " \
                            "VALUES (" + '"' + plz + '"' + ", " + '"' + name + '"' + ");"
        cursor.execute(sql_statement)
        connection.commit()
    except Exception as e:
        print("Es ist folgender Fehler aufgetreten: \n" + e.args[0])
    finally:
        connection.close()
        
    return ######################


############################################################################
#                            EINTRAGEN Mitarbeiter                         #
############################################################################ 
 
def newEntryMA(first_name, last_name, birth_date,
               street_and_no, tel_no, salary, st_class,
               wohnort_ort_id, abteilung_abt_id, bsv_bsv_id):
    
    connection = sqlite3.connect("mitarbeiterverwaltung.db")
    try:
        cursor = connection.cursor()
        
        sql_statement = "INSERT INTO Mitarbeiter (Vorname, Nachname, Geburtsdatum, Strasse, Telefonnummer, " \
                        "Gehalt, StKlasse, Wohnort_Ort_ID, Abteilung_Abt_ID, Bsv_Bsv_ID) " \
                            "VALUES (" + '"' + first_name + '"' + ", " + '"' + last_name + '"' + ", " + '"' + birth_date + '"' + ", " \
                            '"' + street_and_no + '"' + ", " + '"' + tel_no + '"' + ", " + '"' + salary + '"' + ", " \
                            '"' + st_class + '"' + ", " + '"' + wohnort_ort_id + '"' + ", " + '"' + abteilung_abt_id + '"' + ", " \
                            '"' + bsv_bsv_id + '"' + ");"
        cursor.execute(sql_statement)
        connection.commit()
    except Exception as e:
        print("Es ist folgender Fehler aufgetreten: \n" + e.args[0])
    finally:
        connection.close()
        
    return ######################


############################################################################
#                               ÄNDERN Abteilung                           #
############################################################################
 
def updateEntryAbt(name_old, name_new):
    
    connection = sqlite3.connect("mitarbeiterverwaltung.db")
    try:
        cursor = connection.cursor()
        
        sql_statement = "UPDATE Abteilung " \
                            "SET Abt_Bezeichnung = " + '"' + name_new + '" ' \
                                "WHERE Abt_Bezeichnung = " + '"' + name_old + '"' + ";"
        cursor.execute(sql_statement)
        connection.commit()
    except Exception as e:
        print("Es ist folgender Fehler aufgetreten: \n" + e.args[0])
    finally:
        connection.close()
        
    return ######################


############################################################################
#                      ÄNDERN Beschäftigungsverhältnis                     #
############################################################################
  
def updateEntryBsv(name_old, name_new):
    
    connection = sqlite3.connect("mitarbeiterverwaltung.db")
    try:
        cursor = connection.cursor()
        
        sql_statement = "UPDATE Bsv " \
                            "SET Bsv_Bezeichnung = " + '"' + name_new + '" ' \
                                "WHERE Bsv_Bezeichnung = " + '"' + name_old + '"' + ";"
        cursor.execute(sql_statement)
        connection.commit()
    except Exception as e:
        print("Es ist folgender Fehler aufgetreten: \n" + e.args[0])
    finally:
        connection.close()
        
    return ######################



############################################################################
#                                ÄNDERN Wohnort                            #
############################################################################

def updateEntryOrt(plz, name_new):
    
    connection = sqlite3.connect("mitarbeiterverwaltung.db")
    try:
        cursor = connection.cursor()
        
        sql_statement = "UPDATE Wohnort " \
                            "SET Ort_Bezeichnung = " + '"' + name_new + '" ' \
                                "WHERE Ort_ID = " + '"' + plz + '"' + ";"
        cursor.execute(sql_statement)
        connection.commit()
    except Exception as e:
        print("Es ist folgender Fehler aufgetreten: \n" + e.args[0])
    finally:
        connection.close()
        
    return ######################



############################################################################
#                              ÄNDERN Mitarbeiter                          #
############################################################################

def updateEntryMA(id_ma, first_name, last_name, birth_date,
                  street_and_no, tel_no, salary, st_class,
                  wohnort_ort_id, abteilung_abt_id, bsv_bsv_id):
    
    connection = sqlite3.connect("mitarbeiterverwaltung.db")
    try:
        cursor = connection.cursor()
        
        sql_statement = "UPDATE Mitarbeiter " \
                            "SET Nachname = " + '"' + last_name + '"' + ", " \
                                "Vorname = " + '"' + first_name + '"' + ", " \
                                "Geburtsdatum = " + '"' + birth_date + '"' + ", " \
                                "Strasse = " + '"' + street_and_no + '"' + ", " \
                                "Telefonnummer = " + '"' + tel_no+ '"' + ", " \
                                "Gehalt = " + '"' + salary + '"' + ", " \
                                "StKlasse = " + '"' + st_class + '"' + ", " \
                                "Wohnort_Ort_ID = " + '"' + wohnort_ort_id + '"' + ", " \
                                "Abteilung_Abt_ID = " + '"' + abteilung_abt_id + '"' + ", " \
                                "Bsv_Bsv_ID = " + '"' + bsv_bsv_id + '" ' \
                                    "WHERE MA_ID = " + '"' + id_ma + '"' + ";" 
        cursor.execute(sql_statement)
        connection.commit()
    except Exception as e:
        print("Es ist folgender Fehler aufgetreten: \n" + e.args[0])
    finally:
        connection.close()
        
    return ######################



############################################################################
#                             LÖSCHEN Abteilung                            #
############################################################################

def delEntryAbt(name):
    
    connection = sqlite3.connect("mitarbeiterverwaltung.db")
    try:
        cursor = connection.cursor()
        
        sql_statement = "DELETE FROM Abteilung " \
                            "WHERE Abt_Bezeichnung = " + '"' + name + '"' + ";"
        cursor.execute(sql_statement)
        connection.commit()
    except Exception as e:
        print("Es ist folgender Fehler aufgetreten: \n" + e.args[0])
    finally:
        connection.close()
        
    return ######################



############################################################################
#                     LÖSCHEN Beschäftigungsverhältnis                     #
############################################################################

def delEntryBsv(name):
    
    connection = sqlite3.connect("mitarbeiterverwaltung.db")
    try:
        cursor = connection.cursor()
        
        sql_statement = "DELETE FROM Bsv " \
                            "WHERE Bsv_Bezeichnung = " + '"' + name + '"' + ";"
        cursor.execute(sql_statement)
        connection.commit()
    except Exception as e:
        print("Es ist folgender Fehler aufgetreten: \n" + e.args[0])
    finally:
        connection.close()
        
    return ######################



############################################################################
#                             LÖSCHEN Wohnort                              #
############################################################################

def delEntryOrt(plz):
    
    connection = sqlite3.connect("mitarbeiterverwaltung.db")
    try:
        cursor = connection.cursor()
        
        sql_statement = "DELETE FROM Wohnort " \
                            "WHERE Ort_ID = " + '"' + plz + '"' + ";"
        cursor.execute(sql_statement)
        connection.commit()
    except Exception as e:
        print("Es ist folgender Fehler aufgetreten: \n" + e.args[0])
    finally:
        connection.close()
        
    return ######################



############################################################################
#                            LÖSCHEN Mitarbeiter                           #
############################################################################

def delEntryMA(id_ma):
    
    connection = sqlite3.connect("mitarbeiterverwaltung.db")
    try:
        cursor = connection.cursor()
        
        sql_statement = "DELETE FROM Mitarbeiter " \
                            "WHERE MA_ID = " + '"' + id_ma + '"' + ";"
        cursor.execute(sql_statement)
        connection.commit()
    except Exception as e:
        print("Es ist folgender Fehler aufgetreten: \n" + e.args[0])
    finally:
        connection.close()
        
    return ######################



############################################################################
#                                 ANZEIGEN                                 #
############################################################################

def showAllEntries(show_what):
    
    print("\n" + "ANZEIGEN>" + show_what + "\n")
    
    connection = sqlite3.connect("mitarbeiterverwaltung.db")
    
    try:
        cursor = connection.cursor()

        sql_statement = "SELECT * " \
                                "FROM " + '"' + show_what + '"' + ";"
        cursor.execute(sql_statement)
            
        for value in cursor:
            print(str(value[0]) + " - " + str(value[1]))

    #connection.commit()
            
    except Exception as e:
        print("Es ist folgender Fehler aufgetreten: \n" + e.args[0])
        
    finally:
        connection.close()
        
    return ######################



############################################################################
#                         Hauptfunktion des Programms                      #
############################################################################

def main():
    
    print(program_header)
    
    while True:

        print("\n" + "Was möchten Sie tun?")
        print("Sie haben folgende Möglichkeiten:" + "\n")

        print("1. EINTRAGEN --> Bitte die 1 drücken + ENTER")
        print("2. ÄNDERN    --> Bitte die 2 drücken + ENTER")
        print("3. LÖSCHEN   --> Bitte die 3 drücken + ENTER")
        print("4. ANZEIGEN  --> Bitte die 4 drücken + ENTER")
        
        decision_level_1 = input("\n" + "Ihr Wunsch: ")

        if(decision_level_1 == "1"):
            print("\n" + "Was möchten Sie eintragen?")
            print("Sie haben folgende Möglichkeiten:" + "\n")
            
            print("a. Abteilung                --> Bitte a eingeben + ENTER")   
            print("b. Beschäftigungsverhältnis --> Bitte b eingeben + ENTER")
            print("c. Wohnort                  --> Bitte c eingeben + ENTER")
            print("d. Mitarbeiter              --> Bitte d eingeben + ENTER")

            decision_level_2 = input("\n" + "Ihr Wunsch: ")

            if(decision_level_2 == "a"):
                print("\n" + "EINTRAGEN>Abteilung")
                print("\n" + "Im Moment gibt es die folgenden Abteilungen:")
                showAllEntries("Abteilung")
                print("\n" + "Welchen Abteilungsnamen möchten Sie einfügen?")
                name = input("Abteilungsname: ")
                newEntryAbt(name)
                
            elif(decision_level_2 == "b"):
                print("\n" + "EINTRAGEN>Beschäftigungsverhältnis")
                print("\n" + "Im Moment gibt es die folgenden Beschäftigungsverhältnisse:")
                showAllEntries("Bsv")
                print("\n" + "Welches Beschäftigungsverhältnis möchten Sie einfügen?")
                name = input("Beschäftigungsverhältnis: ")
                newEntryBsv(name)
                
            elif(decision_level_2 == "c"):
                print("\n" + "EINTRAGEN>Wohnort")
                print("\n" + "Im Moment gibt es die folgenden Wohnorte:")
                showAllEntries("Wohnort")
                print("\n" + "Welche Wohnorte möchten Sie einfügen?")
                plz = input("PLZ: ")
                name = input("Ort: ")
                newEntryOrt(plz, name)
                
            elif(decision_level_2 == "d"):
                print("\n" + "EINTRAGEN>Mitarbeiter")
                print("\n" + "Im Moment gibt es die folgenden Mitarbeiter:")
                showAllEntries("Mitarbeiter")
                print("\n" + "Welchen Mitarbeiter möchten Sie einfügen?")
                first_name = input("Vorname: ")
                last_name = input("Nachname: ")
                birth_date = input("Geburtsdatum wie folgt --> YYYY-MM-DD --> z.B. 1978-09-24: ")
                street_and_no = input("Straße und Hausnummer: ")
                tel_no = input("Telefonnummer: ")
                salary = input("Gehalt wie folgt --> NNNN oder NNNN.NN --> z.B. 2500 oder 2500.00: ")
                st_class = input("Steuerklasse: ")
                wohnort_ort_id = input("PLZ: ")
                abteilung_abt_id = input("Abteilungs-ID: ")
                bsv_bsv_id = input("Beschäftigungsverhältnis-ID: ")
                newEntryMA(first_name, last_name, birth_date,
                           street_and_no, tel_no, salary, st_class,
                           wohnort_ort_id, abteilung_abt_id, bsv_bsv_id)
                
            else:
                print("\n" + "Das war keine gültige Eingabe!!!")
                print("Bitte die folgende Fehlermeldung sorgfältig durchlesen!!!")
                print(error_header)
    
        elif(decision_level_1 == "2"):
            print("\n" + "Was möchten Sie ändern?")
            print("Sie haben folgende Möglichkeiten:" + "\n")
            
            print("a. Abteilung                --> Bitte a eingeben + ENTER")   
            print("b. Beschäftigungsverhältnis --> Bitte b eingeben + ENTER")
            print("c. Wohnort                  --> Bitte c eingeben + ENTER")
            print("d. Mitarbeiter              --> Bitte d eingeben + ENTER")

            decision_level_2 = input("\n" + "Ihr Wunsch: ")

            if(decision_level_2 == "a"):
                print("\n" + "ÄNDERN>Abteilung") 
                print("\n" + "Im Moment gibt es die folgenden Abteilungen:")
                showAllEntries("Abteilung")
                print("\n" + "Welche Abteilung möchten Sie ändern?")
                name_old = input("Abteilungsname: ")
                name_new = input("Neuer Abteilungsname: ")
                updateEntryAbt(name_old, name_new)
                
            elif(decision_level_2 == "b"):
                print("\n" + "ÄNDERN>Beschäftigungsverhältnis")
                print("\n" + "Im Moment gibt es die folgenden Beschäftigungsverhältnisse:")
                showAllEntries("Bsv")
                print("\n" + "Welches Beschäftigungsverhältnis möchten Sie ändern?")
                name_old = input("Name des Beschäftigungsverhältnisses: ")
                name_new = input("Neuer Name des Beschäftigungsverhältnisses: ")
                updateEntryBsv(name_old, name_new)
                
            elif(decision_level_2 == "c"):
                print("\n" + "ÄNDERN>Wohnort")
                print("\n" + "Im Moment gibt es die folgenden Wohnorte:")
                showAllEntries("Wohnort")
                print("\n" + "Welchen Wohnort möchten Sie ändern?")
                plz = input("PLZ: ")
                name_new = input("Neuer Ortsname: ")
                updateEntryOrt(plz, name_new)
                
            elif(decision_level_2 == "d"):
                print("\n" + "ÄNDERN>Mitarbeiter")
                print("\n" + "Im Moment gibt es die folgenden Mitarbeiter:")
                showAllEntries("Mitarbeiter")
                print("\n" + "Welchen Mitarbeiter möchten Sie ändern?")
                id_ma = input("Mitarbeiter-ID: ")
                print("Bitte tragen Sie die neuen Daten ein")
                first_name = input("Vorname: ")
                last_name = input("Nachname: ")
                birth_date = input("Geburtsdatum wie folgt --> YYYY-MM-DD --> z.B. 1978-09-24: ")
                street_and_no = input("Straße und Hausnummer: ")
                tel_no = input("Telefonnummer: ")
                salary = input("Gehalt wie folgt --> NNNN oder NNNN.NN --> z.B. 2500 oder 2500.00: ")
                st_class = input("Steuerklasse: ")
                wohnort_ort_id = input("PLZ: ")
                abteilung_abt_id = input("Abteilungs-ID: ")
                bsv_bsv_id = input("Beschäftigungsverhältnis-ID: ")
                updateEntryMA(id_ma, first_name, last_name, birth_date,
                              street_and_no, tel_no, salary, st_class,
                              wohnort_ort_id, abteilung_abt_id, bsv_bsv_id)
                
            else:
                print("\n" + "Das war keine gültige Eingabe!!!")
                print("Bitte die folgende Fehlermeldung sorgfältig durchlesen!!!")
                print(error_header)



        elif(decision_level_1 == "3"):
            print("\n" + "Was möchten Sie löschen?")
            print("Sie haben folgende Möglichkeiten:" + "\n")
            
            print("a. Abteilung                --> Bitte a eingeben + ENTER")   
            print("b. Beschäftigungsverhältnis --> Bitte b eingeben + ENTER")
            print("c. Wohnort                  --> Bitte c eingeben + ENTER")
            print("d. Mitarbeiter              --> Bitte d eingeben + ENTER")

            decision_level_2 = input("\n" + "Ihr Wunsch: ")

            if(decision_level_2 == "a"):
                print("\n" + "LÖSCHEN>Abteilung")
                print("\n" + "Im Moment gibt es die folgenden Abteilungen:")
                showAllEntries("Abteilung")
                print("\n" + "Welche Abteilung möchten Sie löschen?")
                name = input("Abteilungsname: ")
                delEntryAbt(name)
                
            elif(decision_level_2 == "b"):
                print("\n" + "LÖSCHEN>Beschäftigungsverhältnis")
                print("\n" + "Im Moment gibt es die folgenden Beschäftigungsverhältnisse:")
                showAllEntries("Bsv")
                print("\n" + "Welches Beschäftigungsverhältnis möchten Sie löschen?")
                name = input("Name des Beschäftigungsverhältnisses: ")
                delEntryBsv(name)
                
            elif(decision_level_2 == "c"):
                print("\n" + "LÖSCHEN>Wohnort")
                print("\n" + "Im Moment gibt es die folgenden Wohnorte:")
                showAllEntries("Wohnort")
                print("\n" + "Welchen Wohnort möchten Sie löschen?")
                plz = input("PLZ: ")
                delEntryOrt(plz)
                
            elif(decision_level_2 == "d"):
                print("\n" + "LÖSCHEN>Mitarbeiter")
                print("\n" + "Im Moment gibt es die folgenden Mitarbeiter:")
                showAllEntries("Mitarbeiter")
                print("\n" + "Welchen Mitarbeiter möchten Sie löschen?")
                id_ma = input("Mitarbeiter-ID: ")
                delEntryMA(id_ma)
                
            else:
                print("\n" + "Das war keine gültige Eingabe!!!")
                print("Bitte die folgende Fehlermeldung sorgfältig durchlesen!!!")
                print(error_header)

        elif(decision_level_1 == "4"):
            print("\n" + "Was möchten Sie angezeigt bekommen?")
            print("Sie haben folgende Möglichkeiten:" + "\n")
            
            print("a. Abteilung                --> Bitte a eingeben + ENTER")   
            print("b. Beschäftigungsverhältnis --> Bitte b eingeben + ENTER")
            print("c. Wohnort                  --> Bitte c eingeben + ENTER")
            print("d. Mitarbeiter              --> Bitte d eingeben + ENTER")

            decision_level_2 = input("\n" + "Ihr Wunsch: ")

            if(decision_level_2.lower() == "a"):
                showAllEntries("Abteilung")
  
            elif(decision_level_2.lower() == "b"):
                showAllEntries("Bsv")
                
            elif(decision_level_2.lower() == "c"):
                showAllEntries("Wohnort")
                
            elif(decision_level_2.lower() == "d"):
                showAllEntries("Mitarbeiter")
                
            else:
                print("\n" + "Das war leider keine gültige Eingabe!!!")
                print("Bitte die folgende Fehlermeldung sorgfältig durchlesen!!!")
                print(error_header)

        else:
            print("\n" + "Das war leider keine gültige Eingabe!!!")
            print("Bitte die folgende Fehlermeldung sorgfältig durchlesen!!!")
            print(error_header)


        exit_choice = input("\n" + "Programm beenden? Dann 'ja' + ENTER: ")
        if (exit_choice.lower() == "ja"):
            break



############################################################################
#                               Programm starten                           #
############################################################################

main()