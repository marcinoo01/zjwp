from sklearn.neighbors import KNeighborsClassifier

from flask import request, Response
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
from projekt_2.app.model.redis_handler import RedisHandler, r
from projekt_2.app.utils.utils import valid_stats

redis_handler = RedisHandler(r)


def linear_regression_plot():
    stat_x = request.args.get('stat_x')
    stat_y = request.args.get('stat_y')

    if stat_x not in valid_stats or stat_y not in valid_stats:
        return Response(
            f"Invalid stats. Please choose from: {', '.join(valid_stats)}",
            status=400
        )

    pokemons = redis_handler.get_data("pokemons")

    x = np.array([pokemon['stats'][stat_x] for pokemon in pokemons]).reshape(-1, 1)
    y = np.array([pokemon['stats'][stat_y] for pokemon in pokemons])

    if len(x) < 2:
        return Response("Not enough data points for regression.", status=400)

    model = LinearRegression()
    model.fit(x, y)
    y_pred = model.predict(x)

    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, color='blue', label='Actual Data')
    plt.plot(x, y_pred, color='red', label='Regression Line')
    plt.title(f"{stat_x.capitalize()} vs {stat_y.capitalize()} Regression")
    plt.xlabel(stat_x.capitalize())
    plt.ylabel(stat_y.capitalize())
    plt.legend()
    plt.show()


def knn_plot(knn_rq):
    if knn_rq.stat_x not in valid_stats or knn_rq.stat_y not in valid_stats:
        return Response(f"Invalid stats. Please choose from: {', '.join(valid_stats)}", status=400)

    pokemons = redis_handler.get_data("pokemons")

    x = np.array([[pokemon['stats'][knn_rq.stat_x], pokemon['stats'][knn_rq.stat_y]] for pokemon in pokemons])
    y = np.array([1 if pokemon['stats'][knn_rq.stat_y] > knn_rq.threshold else 0 for pokemon in pokemons])

    if len(x) < knn_rq.k:
        return Response("Not enough data points for KNN classification.", status=400)

    knn = KNeighborsClassifier(n_neighbors=knn_rq.k)
    knn.fit(x, y)

    x_min, x_max = x[:, 0].min() - 1, x[:, 0].max() + 1
    y_min, y_max = x[:, 1].min() - 1, x[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                         np.arange(y_min, y_max, 0.1))

    z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
    z = z.reshape(xx.shape)

    plt.figure(figsize=(10, 8))
    plt.contourf(xx, yy, z, alpha=0.8)

    scatter = plt.scatter(x[:, 0], x[:, 1], c=y, edgecolor='k')

    plt.title(f"KNN Decision Boundary ({knn_rq.stat_x.capitalize()} vs {knn_rq.stat_y.capitalize()})")
    plt.xlabel(knn_rq.stat_x.capitalize())
    plt.ylabel(knn_rq.stat_y.capitalize())
    handles, labels = scatter.legend_elements(prop="colors")
    plt.legend(handles, ["Class 0", "Class 1"], title="Classes", loc="upper right")

    plt.tight_layout()
    plt.show()
