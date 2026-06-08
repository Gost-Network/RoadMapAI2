import osmnx as ox
import networkx as nx


def generate_route(
    source_lat,
    source_lon,
    destination_lat,
    destination_lon
):

    try:

        center_lat = (
            source_lat +
            destination_lat
        ) / 2

        center_lon = (
            source_lon +
            destination_lon
        ) / 2

        graph = ox.graph_from_point(
            (
                center_lat,
                center_lon
            ),
            dist=30000,
            network_type="drive"
        )

        origin_node = ox.distance.nearest_nodes(
            graph,
            source_lon,
            source_lat
        )

        destination_node = ox.distance.nearest_nodes(
            graph,
            destination_lon,
            destination_lat
        )

        shortest_route = nx.shortest_path(
            graph,
            origin_node,
            destination_node,
            weight="length"
        )

        route_length = nx.shortest_path_length(
            graph,
            origin_node,
            destination_node,
            weight="length"
        )

        coordinates = []

        for node in shortest_route:

            coordinates.append({

                "lat":
                graph.nodes[node]["y"],

                "lon":
                graph.nodes[node]["x"]

            })

        distance_km = round(
            route_length / 1000,
            2
        )

        eta_minutes = round(
            (distance_km / 40) * 60,
            0
        )

        return {

            "success": True,

            "distance_km":
            distance_km,

            "eta_minutes":
            eta_minutes,

            "route":
            coordinates

        }

    except Exception as e:

        print(
            "ROUTE ERROR:",
            e
        )

        return {

            "success": False,

            "message":
            str(e)

        }