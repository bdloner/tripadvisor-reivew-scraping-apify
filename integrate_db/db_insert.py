from . import db_connection

def insert_into_database(item):
    # Establish database connection
   
    conn = db_connection.remote_db_connection()
    cursor = conn.cursor()

    # Construct the INSERT query to attraction_reviews
    sql = """INSERT INTO attraction_reviews (
                 trip_id, url, title, lang, published_date, rating, review_text,
                 trip_type, reviewer_name, reviewer_total_contributions,
                 reviewer_helpful_votes, reviewer_avatar, reviewer_profile_link,
                 place_info_name, place_rating, place_number_of_reviews,
                 place_location, place_full_address, place_street1,
                 place_street2, place_city, place_state, place_country,
                 place_postcode, place_lat, place_long, place_url
             ) 
             VALUES (
                 %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                 %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
             )"""

    # Extract values from the item dictionary
    values = (
        item['id'], item['url'], item['title'], item['lang'], item['publishedDate'],
        item['rating'], item['text'], item['tripType'], item['user']['name'],
        item['user']['contributions']['totalContributions'],
        item['user']['contributions']['helpfulVotes'], item['user']['avatar'],
        item['user']['link'], item['placeInfo']['name'],
        item['placeInfo']['rating'], item['placeInfo']['numberOfReviews'],
        item['placeInfo']['locationString'], item['placeInfo']['address'],
        item['placeInfo']['addressObj']['street1'],
        item['placeInfo']['addressObj']['street2'], item['placeInfo']['addressObj']['city'],
        item['placeInfo']['addressObj']['state'], item['placeInfo']['addressObj']['country'],
        item['placeInfo']['addressObj']['postalcode'], item['placeInfo']['latitude'],
        item['placeInfo']['longitude'], item['placeInfo']['webUrl']
    )

    # Execute the INSERT query
    cursor.execute(sql, values)

    print("Insert to attraction_reviews table successfully.")

    # Commit the transaction
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()