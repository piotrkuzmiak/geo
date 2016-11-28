def dane_geo(input_adres):
    """
    Funkcja zwracajacy koordynaty i obslugujaca wyjatki
    
    ----
    Atrybuty:/n
    @input_adres\n
    Adres do wyszukania koordynatow
    
    """
    import numpy as np
    from geopy.geocoders import Nominatim
    from geopy.exc import GeocoderTimedOut, GeocoderServiceError
    geolocator = Nominatim()
    try:
        location=geolocator.geocode(input_adres, timeout=10)
    except GeocoderServiceError as e:
        print(e)
        return np.nan
    except:
        print(e)
        return np.nan
    else:
        return(location.latitude,location.longitude)
        print('Pobralem koordynaty')
