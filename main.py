from country import Country
import csv

def main(): 
    with open("countries.csv", 'r', newline='') as file:
        reader = csv.DictReader(file)
        
        if not reader.fieldnames:
            print("no data")
            return

        bulk_countries = []
    
        for line in reader:
            country = Country(
                line['Country Name'], 
                line['Country Code'], 
                line['Series Name'], 
                line['Series Code'],
                line['2020 [YR2020]'])
        
            bulk_countries.append(country)
        
        # countries = set(bulk_countries)
        
        for i in range(len(bulk_countries)):
            print(bulk_countries[i].get_country_name() + ":", bulk_countries[i].get_series_name() + ":", bulk_countries[i].get_data())

        # for country in countries:
        #     print(country)

if __name__ == "__main__":
    main()