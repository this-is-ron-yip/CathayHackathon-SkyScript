from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():# -> dict[str, Any] | Literal['please provide more data']:# -> dict[str, Any] | Literal['please provide more data']:
    prompt = request.form["message"]
    if "Data insufficient":
        response = "please provide more data"
    else:
        response = {'destination': 'Hong Kong', 'length': 3, 'interest': 'hiking'}
    return response


@app.route("/route", methods=["POST"])
def get_route():
    destination = request.form["destination"]
    length = request.form["length"]
    interest = request.form["interest"]

    data = [
        [
            {'business_status': 'OPERATIONAL', 'formatted_address': '15 Bligh St, Sydney NSW 2000, Australia', 'geometry': {'location': {'lat': -33.8651343, 'lng': 151.2104596}, 'viewport': {'northeast': {'lat': -33.86383727010728, 'lng': 151.2118845298927}, 'southwest': {'lat': -33.86653692989272, 'lng': 151.2091848701073}}}, 'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png', 'icon_background_color': '#FF9E67', 'icon_mask_base_uri': 'https://maps.gstatic.com/mapfiles/place_api/icons/v2/restaurant_pinlet', 'name': 'Restaurant Hubert', 'opening_hours': {'open_now': True}, 'photos': [{'height': 683, 'html_attributions': [
                '<a href="https://maps.google.com/maps/contrib/113719639442868633401">Ashley Hughes</a>'], 'photo_reference': 'AdCG2DOy7KPOE7BNu6boMu40_EnOpHPFeGEopdVxJKhTxuucUQ500DszuoBe3jnq_P3wOG44-cmtyyGIx0M7Q3XILGF9JMIR8S0vAmmnahKeVg0YM4NEsSGZ5iqKRP7B2Lk3fidG7q3tQCCkuvB2eFLZkUlsBWIEs0J0gprl0oyoVKLxdTK3', 'width': 1024}], 'place_id': 'ChIJF5-RdGquEmsR5rN_H74uSqQ', 'plus_code': {'compound_code': '46M6+W5 Sydney, New South Wales, Australia', 'global_code': '4RRH46M6+W5'}, 'price_level': 3, 'rating': 4.6, 'reference': 'ChIJF5-RdGquEmsR5rN_H74uSqQ', 'types': ['restaurant', 'point_of_interest', 'food', 'establishment'], 'user_ratings_total': 4096},
            {'business_status': 'OPERATIONAL', 'formatted_address': '1 Macquarie St, Sydney NSW 2000, Australia', 'geometry': {'location': {'lat': -33.8592041, 'lng': 151.2132635}, 'viewport': {'northeast': {'lat': -33.85786707010728, 'lng': 151.2147093298927}, 'southwest': {'lat': -33.86056672989272, 'lng': 151.2120096701072}}}, 'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png', 'icon_background_color': '#FF9E67', 'icon_mask_base_uri': 'https://maps.gstatic.com/mapfiles/place_api/icons/v2/restaurant_pinlet', 'name': 'Aria Restaurant Sydney', 'opening_hours': {'open_now': True}, 'photos': [{'height': 2756, 'html_attributions': [
                '<a href="https://maps.google.com/maps/contrib/104093802548855304589">A Google User</a>'], 'photo_reference': 'AdCG2DMkTp97oAathHqWkGEa2aSP1BS5JPTLWL2Shka3KvjL74M_VfFzojYcvWnm9DN0bi2OVM-qwumUCWwfpV8YGAUydJDxJiWh9LYFchL_QoZ2VLghfwWiq9vGMyMVA581R_V08ufclxhZxISwlgWrVKKTMYslMQ4_65qBZLR3zGUcjb_R', 'width': 4134}], 'place_id': 'ChIJdxxU1WeuEmsR11c4fswX-Io', 'plus_code': {'compound_code': '46R7+88 Sydney, New South Wales, Australia', 'global_code': '4RRH46R7+88'}, 'price_level': 4, 'rating': 4.5, 'reference': 'ChIJdxxU1WeuEmsR11c4fswX-Io', 'types': ['restaurant', 'point_of_interest', 'food', 'establishment'], 'user_ratings_total': 2077}
        ],
        [
            {'business_status': 'OPERATIONAL', 'formatted_address': '15 Bligh St, Sydney NSW 2000, Australia', 'geometry': {'location': {'lat': -33.8651343, 'lng': 151.2104596}, 'viewport': {'northeast': {'lat': -33.86383727010728, 'lng': 151.2118845298927}, 'southwest': {'lat': -33.86653692989272, 'lng': 151.2091848701073}}}, 'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png', 'icon_background_color': '#FF9E67', 'icon_mask_base_uri': 'https://maps.gstatic.com/mapfiles/place_api/icons/v2/restaurant_pinlet', 'name': 'Restaurant Hubert', 'opening_hours': {'open_now': True}, 'photos': [{'height': 683, 'html_attributions': [
                '<a href="https://maps.google.com/maps/contrib/113719639442868633401">Ashley Hughes</a>'], 'photo_reference': 'AdCG2DOy7KPOE7BNu6boMu40_EnOpHPFeGEopdVxJKhTxuucUQ500DszuoBe3jnq_P3wOG44-cmtyyGIx0M7Q3XILGF9JMIR8S0vAmmnahKeVg0YM4NEsSGZ5iqKRP7B2Lk3fidG7q3tQCCkuvB2eFLZkUlsBWIEs0J0gprl0oyoVKLxdTK3', 'width': 1024}], 'place_id': 'ChIJF5-RdGquEmsR5rN_H74uSqQ', 'plus_code': {'compound_code': '46M6+W5 Sydney, New South Wales, Australia', 'global_code': '4RRH46M6+W5'}, 'price_level': 3, 'rating': 4.6, 'reference': 'ChIJF5-RdGquEmsR5rN_H74uSqQ', 'types': ['restaurant', 'point_of_interest', 'food', 'establishment'], 'user_ratings_total': 4096},
            {'business_status': 'OPERATIONAL', 'formatted_address': '1 Macquarie St, Sydney NSW 2000, Australia', 'geometry': {'location': {'lat': -33.8592041, 'lng': 151.2132635}, 'viewport': {'northeast': {'lat': -33.85786707010728, 'lng': 151.2147093298927}, 'southwest': {'lat': -33.86056672989272, 'lng': 151.2120096701072}}}, 'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png', 'icon_background_color': '#FF9E67', 'icon_mask_base_uri': 'https://maps.gstatic.com/mapfiles/place_api/icons/v2/restaurant_pinlet', 'name': 'Aria Restaurant Sydney', 'opening_hours': {'open_now': True}, 'photos': [{'height': 2756, 'html_attributions': [
                '<a href="https://maps.google.com/maps/contrib/104093802548855304589">A Google User</a>'], 'photo_reference': 'AdCG2DMkTp97oAathHqWkGEa2aSP1BS5JPTLWL2Shka3KvjL74M_VfFzojYcvWnm9DN0bi2OVM-qwumUCWwfpV8YGAUydJDxJiWh9LYFchL_QoZ2VLghfwWiq9vGMyMVA581R_V08ufclxhZxISwlgWrVKKTMYslMQ4_65qBZLR3zGUcjb_R', 'width': 4134}], 'place_id': 'ChIJdxxU1WeuEmsR11c4fswX-Io', 'plus_code': {'compound_code': '46R7+88 Sydney, New South Wales, Australia', 'global_code': '4RRH46R7+88'}, 'price_level': 4, 'rating': 4.5, 'reference': 'ChIJdxxU1WeuEmsR11c4fswX-Io', 'types': ['restaurant', 'point_of_interest', 'food', 'establishment'], 'user_ratings_total': 2077}
        ]
    ]

    return data