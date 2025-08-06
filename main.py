from country import Country
import csv

def main(): 
    with open("countries.csv", 'r', newline='') as file:
        reader = csv.DictReader(file)
        
        if not reader.fieldnames:
            print("no data")

        bulk_countries = []
    
        for line in reader:

            country = Country(None, None, None, None)
    
            country.set_country_name(line['Country Name'])
            country.set_country_code(line['Country Code'])
            country.set_series_name(line['Series Name'])
            country.set_series_code(line['Series Code'])
            # country.set_country_name(line['Year'])
        
            bulk_countries.append(country)
        
        countries = set(bulk_countries)
        # print(bulk_countries)
        # print("****")

        for country in countries:
            print(country)

        file.close()

if __name__ == "__main__":
    main()