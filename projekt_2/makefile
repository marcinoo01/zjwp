BASE_URL=http://127.0.0.1:5000/pokemon
CONTENT_TYPE=application/json
LIMIT=50
TEST_CMD=.. pytest --disable-warnings

.PHONY: list get compare sort plot heatmap correlations linear_regression knn test coverage

list:
	curl -X GET "$(BASE_URL)/list?limit=$(LIMIT)" -H "Content-Type: $(CONTENT_TYPE)"

get:
	curl -X GET "$(BASE_URL)/$(id)" -H "Content-Type: $(CONTENT_TYPE)"

compare:
	curl -X POST "$(BASE_URL)/compare" \
		-H "Content-Type: $(CONTENT_TYPE)" \
		-d '{"pokemon1": "$(pokemon1)", "pokemon2": "$(pokemon2)"}'

sort:
	curl -X GET "$(BASE_URL)/sort?field=$(field)&order=$(order)&limit=$(limit)&to_display=$(to_display)" -H "Content-Type: $(CONTENT_TYPE)"

plot:
	curl -X GET "$(BASE_URL)/plot" -H "Content-Type: $(CONTENT_TYPE)"

heatmap:
	curl -X GET "$(BASE_URL)/heatmap" -H "Content-Type: $(CONTENT_TYPE)"

correlations:
	curl -X GET "$(BASE_URL)/correlations" -H "Content-Type: $(CONTENT_TYPE)"

linear_regression:
	curl -X GET "$(BASE_URL)/linear_regression?stat_x=$(stat_x)&stat_y=$(stat_y)" -H "Content-Type: $(CONTENT_TYPE)"

knn:
	curl -X GET "$(BASE_URL)/knn?stat_x=$(stat_x)&stat_y=$(stat_y)&k=$(k)&threshold=$(threshold)" -H "Content-Type: $(CONTENT_TYPE)"

test:
	PYTHONPATH=$(shell pwd)/.. pytest --disable-warnings

