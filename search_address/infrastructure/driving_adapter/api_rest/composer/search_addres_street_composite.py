from search_address.infrastructure.driving_adapter.api_rest.controllers import SearchAddressStreetController

def create_search_address_street_controller(dataframe, dataframe2) -> SearchAddressStreetController:
    search_address_street_controller = SearchAddressStreetController(dataframe, dataframe2)
    return search_address_street_controller