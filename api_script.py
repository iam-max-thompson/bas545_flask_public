from flask import Flask, jsonify
import psycopg2
import json


# what does this do
app = Flask(__name__)

# Load credentials from JSON file
with open("my_credentials.json", "r") as f:
    credentials = json.load(f)


# this is gonna need to be our secret file

# Create a connection to the database
connection = psycopg2.connect(
    host=credentials["postgresql"]["host"],
    port=credentials["postgresql"]["port"],
    dbname=credentials["postgresql"]["database"],
    user=credentials["postgresql"]["user"],
    password=credentials["postgresql"]["password"],
)

# Create a cursor to interact with the database
cursor = connection.cursor()


@app.route("/")
def hello_world():
    return "Hello from Flask!"


@app.route("/api/data", methods=["GET"])
def get_data():
    # Fetch data from the database (replace with your SQL query)
    cursor.execute("SELECT * FROM spaztic_elf")
    data = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    connection.close()

    # Return data as JSON
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
