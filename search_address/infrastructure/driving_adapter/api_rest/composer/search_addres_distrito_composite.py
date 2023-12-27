from search_address.infrastructure.driving_adapter.api_rest.controllers import SearchAddressDistritoController

def search_addres_distrito_controller(dataframe) -> SearchAddressDistritoController:
    search_address_distrito_controller = SearchAddressDistritoController(dataframe)
    return search_address_distrito_controller