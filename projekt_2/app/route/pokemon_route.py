from flask import Blueprint, request, Response

from projekt_2.app.model.knn_rq import KnnRq
from projekt_2.app.model.sort_rq import SortRq
from projekt_2.app.plot.pokemon_plot import plot_pokemon_statistics, calculate_correlations, plot_correlation_heatmap
from projekt_2.app.plot.pokemon_analysis import linear_regression_plot, knn_plot
from projekt_2.app.service.pokemon_service import fetch_pokemon_data, compare_pokemon, find_all_pokemons, \
    get_sorted
from projekt_2.app.decorators.pokemon_decorator import json_response

pokemon_blueprint = Blueprint('pokemon', __name__)


@pokemon_blueprint.route('/list', methods=['GET'])
@json_response
def get_all():
    return find_all_pokemons(int(request.args.get('limit', 10)), int(request.args.get('offset', 0)))


@pokemon_blueprint.route('/<name>', methods=['GET'])
@json_response
def get_pokemon(name):
    return fetch_pokemon_data(name)


@pokemon_blueprint.route('/compare', methods=['POST'])
@json_response
def compare_pokemon_route():
    return compare_pokemon(request.json['pokemon1'], request.json['pokemon2'])


@pokemon_blueprint.route('/sort', methods=['GET'])
@json_response
def sort_by():
    return get_sorted(SortRq.from_rq(request))


@pokemon_blueprint.route('/plot', methods=['GET'])
def plot_pokemon():
    plot_pokemon_statistics()
    return Response(status=200)


@pokemon_blueprint.route('/correlations', methods=['GET'])
def correlations():
    return calculate_correlations().to_html()


@pokemon_blueprint.route('/heatmap', methods=['GET'])
def heatmap():
    plot_correlation_heatmap()
    return Response(status=200)


@pokemon_blueprint.route('/linear_regression', methods=['GET'])
def linear_regression():
    linear_regression_plot()
    return Response(status=200)


@pokemon_blueprint.route('/knn', methods=['GET'])
def knn():
    knn_plot(KnnRq.from_rq(request))
    return Response(status=200)
