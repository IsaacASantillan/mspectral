#Import Pandas
import pandas as pd


#Converts TextFile into dictionary which is then passed into pandas to create data frame (see pandas documentation)
def dataframecreator(textfile):
    
    databaseColumns = ["RT1-A", "RT2-A", "Name", "Suspected_matches", "Formula", "MW", "ExactMass", "CAS#", "Derivatization_Agent", "Comments", "Retention_index", "Num Peaks", "X-Values", "Y-Values", "Description", "DB#", "Synon"]
    databaseDictionary = {key: [] for key in databaseColumns}
    
    def coordinatesfunction(coordinates):
        xcoords = [i.split()[0] for i in coordinates if len(i.split()) != 0]
        ycoords = [i.split()[1] for i in coordinates if len(i.split()) != 0]
        databaseDictionary["X-Values"].append(str(xcoords))
        databaseDictionary["Y-Values"].append(str(ycoords))
    
    def addNAValues(dic):
        [dic[keys].append("N/A") for keys in dic if len(dic[keys]) != len(dic["Name"])]
        

    openfile = open(textfile, "r", encoding = "cp1252")
    contentLine = "Start"
    while contentLine:
        contentLine = openfile.readline()
        if not contentLine.strip():
            addNAValues(databaseDictionary)
            continue
        contentList = contentLine.split(":")
        columnnames = contentList[0]
        if columnnames == "Comments":
            metadata = contentList[1].split()
            metadata = str(metadata)
            databaseDictionary["Comments"].append(metadata)
            continue
        if columnnames[0].isdigit():
            coordinatesfunction(columnnames.split(";"))
            continue
        databaseDictionary[columnnames].append(contentList[1].strip())
    openfile.close()
    return pd.DataFrame(databaseDictionary)  


