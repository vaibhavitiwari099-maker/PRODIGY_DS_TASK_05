import pandas as pd
import matplotlib.pyplot as plt
import os

# Load dataset
file_path = "dataset/US_Accidents_March23.csv"
df = pd.read_csv(file_path)

print("Dataset Shape:", df.shape)

# Create output folder
os.makedirs("output", exist_ok=True)

# -------------------------------------------------
# 1. Accident Severity Distribution
# -------------------------------------------------

severity_counts = df["Severity"].value_counts().sort_index()

print("\nAccident Severity Distribution:")
print(severity_counts)

plt.figure(figsize=(8, 5))
severity_counts.plot(kind="bar")

plt.title("Accident Severity Distribution")
plt.xlabel("Severity")
plt.ylabel("Number of Accidents")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("output/severity_distribution.png", dpi=300)
plt.close()


# -------------------------------------------------
# 2. Accidents by Weather Condition
# -------------------------------------------------

if "Weather_Condition" in df.columns:

    weather_counts = df["Weather_Condition"].value_counts().head(10)

    print("\nTop 10 Weather Conditions:")
    print(weather_counts)

    plt.figure(figsize=(12, 6))
    weather_counts.plot(kind="bar")

    plt.title("Top 10 Weather Conditions During Accidents")
    plt.xlabel("Weather Condition")
    plt.ylabel("Number of Accidents")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    plt.savefig("output/weather_conditions.png", dpi=300)
    plt.close()


# -------------------------------------------------
# 3. Accidents by Time of Day
# -------------------------------------------------

if "Sunrise_Sunset" in df.columns:

    time_counts = df["Sunrise_Sunset"].value_counts()

    print("\nAccidents by Time of Day:")
    print(time_counts)

    plt.figure(figsize=(7, 5))
    time_counts.plot(kind="bar")

    plt.title("Accidents by Time of Day")
    plt.xlabel("Time of Day")
    plt.ylabel("Number of Accidents")
    plt.xticks(rotation=0)
    plt.tight_layout()

    plt.savefig("output/time_of_day.png", dpi=300)
    plt.close()


# -------------------------------------------------
# 4. Road / Traffic Conditions
# -------------------------------------------------

road_columns = [
    "Amenity",
    "Bump",
    "Crossing",
    "Give_Way",
    "Junction",
    "No_Exit",
    "Railway",
    "Roundabout",
    "Station",
    "Stop",
    "Traffic_Calming",
    "Traffic_Signal"
]

available_road_columns = [
    col for col in road_columns if col in df.columns
]

road_data = {}

for column in available_road_columns:
    road_data[column] = df[column].sum()

road_counts = pd.Series(road_data).sort_values(ascending=False)

print("\nRoad and Traffic Conditions:")
print(road_counts)

plt.figure(figsize=(12, 6))
road_counts.plot(kind="bar")

plt.title("Road and Traffic Conditions Associated with Accidents")
plt.xlabel("Road / Traffic Condition")
plt.ylabel("Number of Accidents")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig("output/road_conditions.png", dpi=300)
plt.close()


# -------------------------------------------------
# 5. Accident Hotspots
# -------------------------------------------------

if "Start_Lat" in df.columns and "Start_Lng" in df.columns:

    # Sample points if dataset is very large
    plot_df = df.dropna(
        subset=["Start_Lat", "Start_Lng"]
    )

    if len(plot_df) > 50000:
        plot_df = plot_df.sample(50000, random_state=42)

    plt.figure(figsize=(10, 7))

    plt.scatter(
        plot_df["Start_Lng"],
        plot_df["Start_Lat"],
        s=2,
        alpha=0.3
    )

    plt.title("Accident Hotspots")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.tight_layout()

    plt.savefig("output/accident_hotspots.png", dpi=300)
    plt.close()


print("\nAnalysis completed successfully!")

print("\nOutput files created:")
print("output/severity_distribution.png")
print("output/weather_conditions.png")
print("output/time_of_day.png")
print("output/road_conditions.png")
print("output/accident_hotspots.png")