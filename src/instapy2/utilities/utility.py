from instagrapi import Client

class Utility:
    def __init__(self, client: Client):
        self.client = client

    def __get_pk(self, query: str) -> int | None:
        places = self.client.fbsearch_places(query=query)
        place_tuple = [(place.name, place.city, place.zip, place.pk) for place in places]

        for index, place in enumerate(iterable=place_tuple):
            name, city, zip, pk = place
            selection_string = ""
            for index, element in enumerate(iterable=[name, city, zip, pk]):
                if element is not None and element != "":
                    selection_string += f"{element}" if index == 0 else f", {element}"
            print(f"{index + 1}: {selection_string}")

        selection = int(input(f"Enter the index for the correct location (1-{len(place_tuple)}): "))
        if 1 <= selection <= len(places):
            _, _, _, pk = place_tuple[selection - 1]
            return pk
        else:
            return None