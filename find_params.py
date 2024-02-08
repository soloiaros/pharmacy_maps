def find_params(response, address_inp):

    json_response = response.json()
    toponym = json_response["features"][0]
    toponym_coordinates = toponym["geometry"]["coordinates"]
    toponym_longitude, toponym_lattitude = toponym_coordinates
    org_point_start = "{0},{1}".format(address_inp.split(',')[0], address_inp.split(',')[1])
    org_point_dest = "{0},{1}".format(toponym_longitude, toponym_lattitude)

    map_params = {
        "ll": ",".join([str(toponym_longitude), str(toponym_lattitude)]),
        "l": "map",
        "pt": "~".join(["{0},pm2dgl".format(org_point_dest), "{0},pm2dgl".format(org_point_start)])
    }

    return map_params
