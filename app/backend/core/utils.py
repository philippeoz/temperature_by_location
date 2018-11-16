import requests

from django.conf import settings
from django.utils.translation import gettext as _


class APIClient:
    """
    Class to consume geocode and dark sky apis.
    """

    geocode_api_key = settings.GOOGLE_API_KEY
    dark_sky_api_key = settings.DARK_SKY_API_KEY

    @classmethod
    def geocode_api_url(cls, address):
        """
        Returns formated url to geocode api
        """
        url = 'https://maps.googleapis.com/maps/api/geocode/json'
        address = address.replace(' ', '+')
        return f'{url}?key={cls.geocode_api_key}&address={address}'
    
    @classmethod
    def dark_sky_api_url(cls, lat, lng):
        """
        Returns formated url to dark sky api
        """
        url = 'https://api.darksky.net/forecast'
        return f'{url}/{cls.dark_sky_api_key}/{lat},{lng}'
    
    @classmethod
    def temperature_from_coordinates(cls, latitude, longitude):
        """
        Returns temperature from region according coordinates
        """
        if not latitude or not longitude:
            raise Exception(
                _('Invalid latitude or longitude.')
            )
        
        response = requests.get(
            cls.dark_sky_api_url(latitude, longitude), params={'units': 'auto'}
        )

        if response.status_code != 200:
            raise Exception(
                _('Error on getting temperature.')
            )
    
        data = response.json()
        return round(data['currently']['temperature'], 3)

    @classmethod
    def latitude_longitude_from_address(cls, address):
        """
        Returns a formatted address, latitude and longitude from address
        """
        if not address:
            raise Exception(
                _('Invalid address.')
            )

        response = requests.get(cls.geocode_api_url(address))

        if response.status_code != 200 or response.json()['status'] != 'OK':
            raise Exception(
                _('Error on getting latitude and longitude.')
            )

        data = response.json()
        results = data.get('results')

        if not results:
            raise Exception(
                _('Address not found.')
            )
        
        first_result = results[0]
        geometry = first_result.get('geometry')

        return {
            'formatted_address': first_result.get('formatted_address'),
            'latitude': geometry.get('location').get('lat'),
            'longitude': geometry.get('location').get('lng')
        }
