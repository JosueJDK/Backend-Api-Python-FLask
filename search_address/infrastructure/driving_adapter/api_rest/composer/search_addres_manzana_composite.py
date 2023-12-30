from search_address.infrastructure.driving_adapter.api_rest.controllers import SearchAddressManzanaController

def search_addres_manzana_controller(dataframe) -> SearchAddressManzanaController:
    search_address_manzana_controller = SearchAddressManzanaController(dataframe)
    return search_address_manzana_controller