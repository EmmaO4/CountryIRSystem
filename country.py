# this file contains the construction of a country and its attributes
# attributes: Country Name,Country Code,Series Name,Series Code,Year
class Country:

    def __init__(self, country_name, country_code, series_name, series_code, data):
        self._country_name = country_name
        self._country_code = country_code
        self._series_name = series_name
        self._series_code = series_code
        self._data = data

    def get_country_name(self):
        return self._country_name
    
    def set_country_name(self, country_name):
        self._country_name = country_name

    def get_country_code(self):
        return self._country_code
    
    def set_country_code(self, country_code):
        self._country_code = country_code
    
    def get_series_name(self):
        return self._series_name
    
    def set_series_name(self, series_name):
        self._series_name = series_name
    
    def get_series_code(self):
        return self._series_code
    
    def set_series_code(self, series_code):
        self._series_code = series_code

    def get_data(self):
        return self._data
    
    def set_data(self, data):
        if data:
            self._data = data
        else:
            self._data = 0
    
    def __str__(self):
        return (f"Country Name: {self.get_country_name()}, Country Code: {self.get_country_code()}, Series Name: {self.get_series_name()}, Series Code: {self.get_series_code()}, Data: {self.get_data()}")

    # allows the comparison between country objects to produce a valid bool instead of defaulting to False
    # for creating a set out of list of countries in main.py
    def __eq__(self, value):
        if not isinstance(value, Country):
            return NotImplemented
        return (self._country_name == value._country_name and 
                self._country_code == value._country_code and
                self._series_name == value._series_name and
                self._series_code == value._series_code and
                self._data == value._data)
    
    # must be used in conjuction with equality dunder: allows country objects to be usable keys in dictionaries or elems in sets
    # for creating a set out of list of countries in main.py
    def __hash__(self):
        return hash((
            self._country_name,
            self._country_code,
            self._series_name,
            self._series_code,
            tuple(self._data) if self._data else None))