import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "tourist_project.db")

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

# =========================
# PLACES TABLE
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS places (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    destination TEXT NOT NULL,
    category TEXT NOT NULL,
    description TEXT NOT NULL,
    average_cost INTEGER NOT NULL,
    rating REAL NOT NULL,
    image_url TEXT,
    google_map_link TEXT
)
""")

# =========================
# SEARCH HISTORY TABLE
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS search_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    destination TEXT,
    category TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# =========================
# TOURIST PLACES
# =========================

places = [
    (
        "Baga Beach",
        "Goa",
        "Beaches",
        "One of the most popular beaches in Goa, known for water sports and nightlife.",
        3000,
        4.8,
        "baga_beach.jpg",
        "https://www.google.com/maps/search/?api=1&query=Baga+Beach+Goa"
    ),
    (
        "Marina Beach",
        "Chennai",
        "Beaches",
        "India's longest urban beach with a beautiful sunrise view.",
        1500,
        4.6,
        "marina_beach.jpg",
        "https://www.google.com/maps/search/?api=1&query=Marina+Beach+Chennai"
    ),
    (
        "Kovalam Beach",
        "Kerala",
        "Beaches",
        "Famous for its lighthouse, golden sand and relaxing atmosphere.",
        2500,
        4.7,
        "kovalam_beach.jpg",
        "https://www.google.com/maps/search/?api=1&query=Kovalam+Beach+Kerala"
    ),
    (
        "Munnar Tea Gardens",
        "Munnar",
        "Nature",
        "Beautiful green tea plantations surrounded by hills.",
        3500,
        4.9,
        "munnar_tea_gardens.jpg",
        "https://www.google.com/maps/search/?api=1&query=Munnar+Tea+Gardens"
    ),
    (
        "Ooty Lake",
        "Ooty",
        "Nature",
        "A peaceful lake offering boating and scenic beauty.",
        2500,
        4.7,
        "ooty_lake.jpg",
        "https://www.google.com/maps/search/?api=1&query=Ooty+Lake"
    ),
    (
        "Athirappilly Waterfalls",
        "Kerala",
        "Nature",
        "The largest waterfall in Kerala, often called the Niagara of India.",
        2000,
        4.8,
        "athirappilly_waterfalls.jpg",
        "https://www.google.com/maps/search/?api=1&query=Athirappilly+Waterfalls"
    ),
    (
        "Mysore Palace",
        "Mysore",
        "Historical Places",
        "A magnificent royal palace famous for its architecture and history.",
        1800,
        4.9,
        "mysore_palace.jpg",
        "https://www.google.com/maps/search/?api=1&query=Mysore+Palace"
    ),
    (
        "Hampi",
        "Karnataka",
        "Historical Places",
        "UNESCO World Heritage Site with ancient temples and ruins.",
        2500,
        4.8,
        "hampi.jpg",
        "https://www.google.com/maps/search/?api=1&query=Hampi+Karnataka"
    ),
    (
        "Charminar",
        "Hyderabad",
        "Historical Places",
        "Historic monument and symbol of Hyderabad.",
        1500,
        4.7,
        "charminar.jpg",
        "https://www.google.com/maps/search/?api=1&query=Charminar+Hyderabad"
    ),
    (
        "Commercial Street",
        "Bangalore",
        "Shopping",
        "Popular shopping destination for clothes, footwear and accessories.",
        2000,
        4.5,
        "commercial_street.jpg",
        "https://www.google.com/maps/search/?api=1&query=Commercial+Street+Bangalore"
    ),
    (
        "Pondy Bazaar",
        "Chennai",
        "Shopping",
        "One of Chennai's busiest shopping streets.",
        1800,
        4.4,
        "pondy_bazaar.jpg",
        "https://www.google.com/maps/search/?api=1&query=Pondy+Bazaar+Chennai"
    ),
    (
        "Rishikesh River Rafting",
        "Rishikesh",
        "Adventure",
        "Experience thrilling white-water rafting on the Ganges.",
        4500,
        4.9,
        "rishikesh_rafting.jpg",
        "https://www.google.com/maps/search/?api=1&query=Rishikesh+River+Rafting"
    ),
    (
        "Solang Valley",
        "Manali",
        "Adventure",
        "Popular destination for skiing, paragliding and snow activities.",
        5000,
        4.8,
        "solang_valley.jpg",
        "https://www.google.com/maps/search/?api=1&query=Solang+Valley+Manali"
    ),
    (
        "Bandipur National Park",
        "Karnataka",
        "Wildlife",
        "Famous wildlife sanctuary with elephants, deer and tigers.",
        3500,
        4.7,
        "bandipur.jpg",
        "https://www.google.com/maps/search/?api=1&query=Bandipur+National+Park"
    ),
    (
        "Periyar National Park",
        "Kerala",
        "Wildlife",
        "Beautiful wildlife reserve known for elephants and boating.",
        3200,
        4.8,
        "periyar.jpg",
        "https://www.google.com/maps/search/?api=1&query=Periyar+National+Park"
    ),
    (
        "Meenakshi Temple",
        "Madurai",
        "Spiritual",
        "Historic Hindu temple known for its magnificent architecture.",
        1000,
        4.9,
        "meenakshi_temple.jpg",
        "https://www.google.com/maps/search/?api=1&query=Meenakshi+Temple+Madurai"
    ),
    (
        "Golden Temple",
        "Amritsar",
        "Spiritual",
        "One of the most sacred Sikh pilgrimage sites.",
        1500,
        5.0,
        "golden_temple.jpg",
        "https://www.google.com/maps/search/?api=1&query=Golden+Temple+Amritsar"
    ),
    (
        "Hyderabad Food Street",
        "Hyderabad",
        "Food",
        "Enjoy famous Hyderabadi biryani and local street food.",
        2000,
        4.8,
        "hyderabad_food.jpg",
        "https://www.google.com/maps/search/?api=1&query=Hyderabad+Food+Street"
    ),
    (
        "Lucknow Food Walk",
        "Lucknow",
        "Food",
        "Explore authentic Awadhi cuisine and kebabs.",
        2200,
        4.8,
        "lucknow_food.jpg",
        "https://www.google.com/maps/search/?api=1&query=Lucknow+Food+Walk"
    ),
    (
        "Dindigul Cuisine",
        "Dindigul",
        "Food",
        "Known for its delicious Dindigul biryani and traditional dishes.",
        1800,
        4.7,
        "dindigul_food.jpg",
        "https://www.google.com/maps/search/?api=1&query=Dindigul+Cuisine"
    )
]

# Insert only if places table is empty
cursor.execute("SELECT COUNT(*) FROM places")
count = cursor.fetchone()[0]

if count == 0:
    cursor.executemany("""
        INSERT INTO places
        (
            name,
            destination,
            category,
            description,
            average_cost,
            rating,
            image_url,
            google_map_link
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, places)

    print("20 tourist places inserted successfully!")

else:
    print(f"Places table already contains {count} records.")

connection.commit()
connection.close()

print("SQLite database created successfully!")
print(f"Database location: {DB_PATH}")