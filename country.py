# this file contains the construction of a country and its attributes
# attributes: Country Name,Country Code,Series Name,Series Code,Year

class Country:

    def __init__(self, country_name, country_code, series_name, series_code):
        self._country_name = country_name
        self._country_code = country_code
        self._series_name = series_name
        self._series_code = series_code

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
    
    def __str__(self):
        return (f"Country Name: {self.get_country_name}, Country Code: {self.get_country_code}, Series Name: {self.get_series_name}, Series Code: {self.get_series_code}")

    def __eq__(self, value):
        pass
    
    def __hash__(self):
        pass 