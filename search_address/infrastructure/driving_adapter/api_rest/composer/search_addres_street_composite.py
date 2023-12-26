from search_address.infrastructure.driving_adapter.api_rest.controllers import SearchAddressStreetController

def create_search_address_street_controller(dataframe) -> SearchAddressStreetController:
    search_address_street_controller = SearchAddressStreetController(dataframe)
    return search_address_street_controller