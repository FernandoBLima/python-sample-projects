FROM mongo

COPY pokemon.csv /pokemon.csv
CMD mongoimport --host mongodb --db pokemon --collection pokedex --type csv --headerline --file pokemon.csv