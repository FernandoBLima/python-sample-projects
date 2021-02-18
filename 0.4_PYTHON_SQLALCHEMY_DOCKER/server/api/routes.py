from api.views.pokedex import PokedexFilterView, PokedexView, PokedexWelcome
from api.views.trainers import TrainersView


def set_routes(app):
    """ Set routes, mechanism of mapping the URL directly to the code"""

    app.router.add_route('GET', "/", PokedexWelcome)
    app.router.add_route('GET', "/pokedex/all", PokedexView)
    app.router.add_route('GET', "/pokedex/filter", PokedexFilterView)
    app.router.add_route('GET', "/trainers", TrainersView)
    app.router.add_route('POST', "/trainer", TrainersView)
    app.router.add_route('PUT', "/trainer", TrainersView)
    app.router.add_route('DELETE', "/trainer", TrainersView)
