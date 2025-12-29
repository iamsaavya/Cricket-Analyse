import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def get_db_connection():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="9977277199aaa",  # Using your established password
            database="cricket"
        )
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def compare_players():
    conn = get_db_connection()
    if not conn:
        return
    
    cursor = conn.cursor()
    
    # Input players to compare
    player1 = input("Enter first player name: ")
    player2 = input("Enter second player name: ")
    
    # Query for batting stats
    query = "SELECT Runs, 100s, 50s, Average, SR FROM batting WHERE name = %s"
    
    cursor.execute(query, (player1,))
    stats1 = cursor.fetchone()
    
    cursor.execute(query, (player2,))
    stats2 = cursor.fetchone()
    
    if stats1 and stats2:
        labels = ['Runs', '100s', '50s', 'Average', 'SR']
        x = np.arange(len(labels))  # Label locations
        width = 0.35  # Width of the bars

        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Create side-by-side bars
        rects1 = ax.bar(x - width/2, stats1, width, label=player1, color='skyblue')
        rects2 = ax.bar(x + width/2, stats2, width, label=player2, color='orange')

        # Add labels and title
        ax.set_ylabel('Values')
        ax.set_title(f'Stat Comparison: {player1} vs {player2}')
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()

        # Log scale for 'Runs' since it's much higher than '100s'
        ax.set_yscale('log')
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        print(f"Generating graph for {player1} and {player2}...")
        plt.show()
    else:
        print("One or both players not found in the database.")
    
    cursor.close()
    conn.close()

if __name__ == "__main__":
    compare_players()