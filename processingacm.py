import json
import datetime
from dateutil.parser import parse


with open('acm.json') as data_file:
    data = json.load(data_file)

dico_journal = {}
all_journals = []


for v in data:
    if v["Date"] != "":
        date = parse(v["Date"])
        Year = date.year
        Year = str(Year)
        Month = date.month
        Month = str(Month)
        if (Month == "1"):
            MonthName = "January"
        if (Month == "2"):
            MonthName = "February"
        if (Month == "3"):
            MonthName = "March"
        if (Month == "4"):
            MonthName = "April"
        if (Month == "5"):
            MonthName = "May"
        if (Month == "6"):
            MonthName = "June"
        if (Month == "7"):
            MonthName = "July"
        if (Month == "8"):
            MonthName = "August"
        if (Month == "9"):
            MonthName = "September"
        if (Month == "10"):
            MonthName = "October"
        if (Month == "11"):
            MonthName = "November"
        if (Month == "12"):
            MonthName = "December"
        Day = date.day
        Day = str(Day)
    else:
        Year = ""
        Month = ""
        MonthName = ""
        Day = ""
    LocationsPro = []
    Universities = []
    Countries = []
    for location in v["Locations"]:
        location = location.split('\n', 1)[0]
        location = location.replace('View Profile', '')
        University = location.split(',')[0]
        Country = location.split(', ')[-1]
        if (Country == University):
            Country = ""
        LocationsPro.append(location)
        Universities.append(University)
        Countries.append(Country)

    dico_journal = {"Title":v["Title"], "Abstract": v["Abstract"], "Type": v["Type"], "Access": v["Access"], "Date": v["Date"], "Year": Year, "Month": Month, "MonthName": MonthName, "Day": Day, "DOI": v["DOI"], "Publisher": v["Publisher"], "Authors": v["Authors"], "Locations": LocationsPro, "Universities": Universities, "Countries": Countries, "WebSite": "ACM"}
    # print()
    all_journals.append(dico_journal)
        # print(all_journals)
with open("acmPro1.json", "w") as write_file:
        json.dump(all_journals, write_file, indent=4)