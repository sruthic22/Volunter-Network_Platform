import psycopg2

# Database connection parameters
HOST = 'your-redshift-cluster-endpoint'
PORT = '5439'
DB_NAME = 'volunteer_db'
USER = 'your_username'
PASSWORD = 'your_password'

def create_tables():
    # Connect to the Redshift database
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT
    )
    cursor = conn.cursor()
    
    # Create tables
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS volunteer_profiles (
        id INT PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100),
        phone VARCHAR(15),
        activity VARCHAR(100),
        engagement_date DATE
    );
    '''
    
    cursor.execute(create_table_query)
    
    # Commit changes and close connection
    conn.commit()
    cursor.close()
    conn.close()
    print("Tables created successfully in Redshift.")

if __name__ == "__main__":
    create_tables()
