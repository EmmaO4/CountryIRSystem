import csv

def main(): 
    with open("countries.csv", 'r', newline='') as file:
        reader = csv.DictReader(file)
        
        if not reader.fieldnames:
            print("no data")

        country_names = []
    
        for line in reader:
            country_names.append(line['Country Name'])
        
        if country_names:
            set_cnames = set(country_names)
            print(set_cnames)

        file.close()

if __name__ == "__main__":
    main()