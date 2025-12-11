class MovieFetcher:
    def featch_movie_from_provider(self, movie_id: int) -> dict:
        print(f"[MovieFetcher] Fetching movie {movie_id} from external provider...")
        return {
            "id": movie_id,
            "title": "Sample Movie",
            "year": 2024
        }

class MovieCreator:
    def create(self, movie_dto: dict) -> None:
        print(f"[MovieCreator] Creating movie in local database...")
        print(f"[MovieCreator] Movie data: {movie_dto}")

class MediaImporter:
    def import_media_for_movie(self, movie_id: int) -> None:
        print(f"[MediaImporter] Importing media for movie {movie_id}...")

class GenreImporter:
    def import_genre_for_movie(self, movie_id: int) -> None:
        print(f"[GenreImporter] Importing genres for movie {movie_id}...")

class MovieImporter:
    def __init__(
            self,
            movie_fetcher: MovieFetcher,
            movie_creator: MovieCreator,
            media_importer: MediaImporter,
            genre_importer: GenreImporter
    ) -> None:
        self.__movie_fetcher = movie_fetcher
        self.__movie_creator = movie_creator
        self.__media_importer = media_importer
        self.__genre_importer = genre_importer

    def import_movie(self, movie_id: int) -> None:
        print("[MovieImporter] Starting movie importation process...")

        movie_dto = self.__movie_fetcher.featch_movie_from_provider(movie_id)

        self.__movie_creator.create(movie_dto)
        self.__media_importer.import_media_for_movie(movie_id)
        self.__genre_importer.import_genre_for_movie(movie_id)

        print("[MovieImporter] Movie importation process completed.")


def facade_app() -> None:
    movie_fetcher = MovieFetcher()
    movie_creator = MovieCreator()
    media_importer = MediaImporter()
    genre_importer = GenreImporter()
    movie_importer = MovieImporter(
        movie_fetcher=movie_fetcher,
        movie_creator=movie_creator,
        media_importer=media_importer,
        genre_importer=genre_importer
    )

    movie_importer.import_movie(movie_id=1)


if __name__ == "__main__":
    facade_app()