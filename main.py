import os
from datetime import datetime, timedelta

def clear_old_files(landing_area_path, retention_days=3):
    # Get the current date and time
    current_time = datetime.now()

    # Iterate over files in the landing area
    for filename in os.listdir(landing_area_path):
        file_path = os.path.join(landing_area_path, filename)

        # Check if the file is a regular file and not a directory
        if os.path.isfile(file_path):
            # Get the modification time of the file
            modification_time = datetime.fromtimestamp(os.path.getmtime(file_path))

            # Calculate the age of the file in days
            age_in_days = (current_time - modification_time).days

            # Check if the file is older than the retention period
            if age_in_days > retention_days:
                # Delete the file
                os.remove(file_path)
                print(f"Deleted: {filename}")

# Specify the landing area path
landing_area_path = '/path/to/landing/area'

# Specify the retention period in days (e.g., 3 days)
retention_days = 3

# Call the function to clear old files
clear_old_files(landing_area_path, retention_days)
