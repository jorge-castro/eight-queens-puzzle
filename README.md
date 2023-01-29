# Eight Queens Puzzle

This is my solution to the [eight queens puzzle](https://en.wikipedia.org/wiki/Eight_queens_puzzle) (and the more general _n_ queens problem).

## Requirements

This project uses [Poetry](https://python-poetry.org/) for dependency management. To install dependencies simply run:

```shell
poetry install
```

Note that this application depends on [psycopg2](https://www.psycopg.org/docs/) and is therefore subject to its [build and runtime prerequisites][1].

## Usage

To compute and visualize the solutions run the `main` submodule inside the project package and pass the number of queens as an argument (defaults to 8 if not
provided):

```shell
python -m eight_queens_puzzle.main [QUEEN_NUMBER]
```

To compute and write the solutions to a PostgreSQL database run the project package as a module following the same pattern as above:

```shell
python -m eight_queens_puzzle [QUEEN_NUMBER]
```

And lastly, the `view_db_solutions.py` script can retrieve stored solutions from the database and display them. E.g.:

```shell
python view_db_solutions.py [QUEEN_NUMBER] | less
```

The parameters for the connection to the database are to be configured by the use of [libpq environment variables][2]. These can be placed in an `.env` file
for convenience. Further details can be found in the [SQLAlchemy docs][3].

## Testing

Tests are located under `tests/` and are run with [pytest](https://pytest.org).

## Docker

A `Dockerfile` and a Compose file are provided to ease development/deployment.

The following commands will drop you into a shell where you can run tests and code that don't depend on a database connection:

```shell
docker build -t eight-queens-puzzle .
docker run -it eight-queens-puzzle
```

To spin up a PostgreSQL instance with data persisted to a volume:

```shell
export POSTGRES_PASSWORD=create-db-with-this-password
docker compose up -d
```

The above will also create an instance of the application and write the solutions for a standard 8x8 chessboard to the database. To run further commands, such
as those in the [usage section](#usage) (or drop into a shell before doing so):

```shell
docker compose run app [COMMAND] [ARGS...]
```

[1]: https://www.psycopg.org/docs/install.html#prerequisites
[2]: https://www.postgresql.org/docs/current/libpq-envars.html
[3]: https://docs.sqlalchemy.org/en/14/dialects/postgresql.html#empty-dsn-connections-environment-variable-connections
[4]: https://github.com/docker-library/docs/blob/master/postgres/README.md#postgres_password
