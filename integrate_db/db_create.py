import db_connection

conn = db_connection.remote_db_connection()

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Doping attraction_reviews table if already exists.
cursor.execute("DROP TABLE IF EXISTS attraction_reviews")

#Creating table as per requirement
sql ="""
    CREATE TABLE attraction_reviews (
        id SERIAL PRIMARY KEY,
        trip_id INT,
        url TEXT,
        title TEXT,
        lang TEXT,
        published_date TEXT,
        rating INT,
        review_text TEXT,
        trip_type TEXT,
        reviewer_name TEXT,
        reviewer_total_contributions INT,
        reviewer_helpful_votes INT,
        reviewer_avatar TEXT,
        reviewer_profile_link TEXT,
        place_info_name TEXT,
        place_rating INT,
        place_number_of_reviews INT,
        place_location TEXT,
        place_full_address TEXT,
        place_street1 TEXT,
        place_street2 TEXT,
        place_city TEXT,
        place_state TEXT,
        place_country TEXT,
        place_postcode TEXT,
        place_lat FLOAT,
        place_long FLOAT,
        place_url TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
"""
cursor.execute(sql)

print("Table attraction_reviews created successfully.")

conn.commit()
#Closing the connection
cursor.close()
conn.close()