import pandas as pd
import math
from sklearn.cluster import KMeans

from ItineraryDrafting import ItineraryDraftAgent
from DestinationRetreiver import DestinationRetreiverAgent

def getData(destinations):
    df = list()
    raw_data = dict()
    for interest, destinations in destinations.items():

        for r in destinations["results"]:
            raw_data[r["place_id"]] = r
            df.append({
                "place_id": r["place_id"],
                "type": interest,
                "lat": r["geometry"]["location"]["lat"],
                "lng": r["geometry"]["location"]["lng"]
            })

    df = pd.DataFrame(df)
    return df, raw_data


def getCentroids(df, days):

    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=days)
    df['cluster'] = kmeans.fit_predict(df[['lat', 'lng']])

    # Calculate centroids for each cluster
    centroids = df.groupby('cluster').agg(
        {'lat': 'mean', 'lng': 'mean'}).reset_index()

    return centroids


def calculateDistance(df, centroids):
    def haversineDistance(pt1, pt2):
        (lat1, lon1), (lat2, lon2) = pt1, pt2
        # Convert latitude and longitude from degrees to radians
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

        # Haversine formula
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat/2)**2 + math.cos(lat1) * \
            math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.asin(math.sqrt(a))

        # Radius of the Earth in kilometers
        radius = 6371  # Earth's radius in km

        # Calculate the distance
        distance = radius * c
        return distance

    for i in range(len(centroids)):
        df[f'distance_to_{i}'] = df.apply(
            lambda row: haversineDistance((row['lat'], row['lng']), (centroids.iloc[i]['lat'], centroids.iloc[i]['lng'])), axis=1
        )
    return df


def ItineraryPlanAgent(data):

    destinations = DestinationRetreiverAgent(data)

    df, raw_data = getData(destinations)
    centroids = getCentroids(df, data["length"])
    df = calculateDistance(df, centroids)
    
    full_result = list()
    for i in range(data["length"]):
        result = list()
        draft_route = ItineraryDraftAgent(data["interest"])
        for event in draft_route:
            if len(event) == 3:
                filtered_df = df[(df['type'] == event[2])]
            else:
                filtered_df = df[(df['type'] == data["interest"][0])]
            if (len(filtered_df)):
                min_distance_index = filtered_df[f'distance_to_{i}'].idxmin()
                min_distance_record = df.loc[min_distance_index]
                df = df[df['place_id'] != min_distance_record['place_id']]
                result.append({"time": {"start": event[0], "end": event[1]}, "destination": raw_data[min_distance_record["place_id"]]})
        full_result.append(result)
    return full_result


if __name__ == "__main__":
    data = {'destination': 'hong kong', 'interest': [
        'shopping', 'movie', 'eating'], 'length': 3}
    final_route = ItineraryPlanAgent(data)
