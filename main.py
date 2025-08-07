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
                line['Series Code'])
        
            bulk_countries.append(country)
        
        countries = set(bulk_countries)

        for country in countries:
            print(country)

if __name__ == "__main__":
    main()