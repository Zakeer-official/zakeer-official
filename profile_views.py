import os

def increment_profile_views():
    count_file = 'profile_views.txt'
    
    # Debug: Print current working directory
    print(f"Current working directory: {os.getcwd()}")
    
    # Initialize the count to 0 if the file doesn't exist
    if not os.path.exists(count_file):
        print(f"{count_file} not found. Creating it with 0 views.")
        with open(count_file, 'w') as f:
            f.write('0')  # Initialize with 0 views
    
    # Read, increment, and update the count
    with open(count_file, 'r+') as f:
        count = int(f.read().strip())
        print(f"Current profile views: {count}")
        if not visitor_is_self():  # Only increment if the visitor is not yourself
            count += 1
            print(f"Incremented profile views to: {count}")
            f.seek(0)  # Move the file pointer to the beginning
            f.write(str(count))  # Write the updated count
            f.truncate()  # Truncate the file in case the new count is shorter
    
    return count

def visitor_is_self():
    return False

# Main execution
if __name__ == "__main__":
    new_count = increment_profile_views()
    print(f'Profile views: {new_count}')
