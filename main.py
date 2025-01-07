import pandas as pd
import matplotlib.pyplot as plt

# Sample data for Indian players in the 2019 Cricket World Cup
data = {
    "Player": ["Rohit Sharma", "Virat Kohli", "KL Rahul", "MS Dhoni", "Hardik Pandya", 
               "Jasprit Bumrah", "Mohammed Shami", "Yuzvendra Chahal", "Ravindra Jadeja"],
    "Matches Played": [9, 9, 9, 9, 9, 9, 4, 8, 2],
    "Runs Scored": [648, 443, 361, 273, 226, 0, 0, 0, 77],
    "Wickets Taken": [0, 0, 0, 0, 2, 18, 14, 12, 2],
    "Strike Rate": [98.3, 94.6, 77.3, 87.8, 112.3, None, None, None, 136.8],
    "Economy Rate": [None, None, None, None, None, 4.41, 5.48, 6.22, 5.35]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("Indian Players' Performance in the 2019 World Cup:")
print(df)

# Bar plot for runs scored by players
plt.figure(figsize=(10, 6))
plt.bar(df["Player"], df["Runs Scored"], color='skyblue', label="Runs Scored")
plt.xticks(rotation=45, ha="right")
plt.title("Runs Scored by Indian Players in 2019 World Cup", fontsize=14)
plt.xlabel("Player", fontsize=12)
plt.ylabel("Runs Scored", fontsize=12)
plt.legend()
plt.tight_layout()
plt.show()

# Bar plot for wickets taken by players
plt.figure(figsize=(10, 6))
plt.bar(df["Player"], df["Wickets Taken"], color='orange', label="Wickets Taken")
plt.xticks(rotation=45, ha="right")
plt.title("Wickets Taken by Indian Players in 2019 World Cup", fontsize=14)
plt.xlabel("Player", fontsize=12)
plt.ylabel("Wickets Taken", fontsize=12)
plt.legend()
plt.tight_layout()
plt.show()

# Highlight top performers
top_scorer = df.loc[df["Runs Scored"].idxmax()]
top_wicket_taker = df.loc[df["Wickets Taken"].idxmax()]

print(f"\nTop Scorer: {top_scorer['Player']} with {top_scorer['Runs Scored']} runs.")
print(f"Top Wicket-Taker: {top_wicket_taker['Player']} with {top_wicket_taker['Wickets Taken']} wickets.")

# Scatter plot for strike rates vs runs scored (for batsmen)
batsmen = df[df["Strike Rate"].notnull()]
plt.figure(figsize=(8, 6))
plt.scatter(batsmen["Runs Scored"], batsmen["Strike Rate"], color='purple', s=100)
for i, player in enumerate(batsmen["Player"]):
    plt.text(batsmen["Runs Scored"].iloc[i], batsmen["Strike Rate"].iloc[i], player, fontsize=10)
plt.title("Strike Rate vs Runs Scored (Indian Batsmen)", fontsize=14)
plt.xlabel("Runs Scored", fontsize=12)
plt.ylabel("Strike Rate", fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()
