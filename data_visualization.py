import psycopg2
import matplotlib.pyplot as plt

# Database connection parameters
HOST = 'your-redshift-cluster-endpoint'
PORT = '5439'
DB_NAME = 'volunteer_db'
USER = 'your_username'
PASSWORD = 'your_password'

def fetch_data():
    # Connect to the Redshift database
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT
    )
    cursor = conn.cursor()
    
    # Query data
    query = "SELECT activity, COUNT(*) FROM volunteer_profiles GROUP BY activity;"
    cursor.execute(query)
    
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return results

def visualize_data(data):
    activities = [row[0] for row in data]
    counts = [row[1] for row in data]
    
    plt.barh(activities, counts)
    plt.xlabel('Number of Volunteers')
    plt.title('Volunteer Activities')
    plt.show()

def main():
    data = fetch_data()
    visualize_data(data)

if __name__ == "__main__":
    main()
