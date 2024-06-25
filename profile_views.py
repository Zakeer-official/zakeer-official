import os

def increment_profile_views():
    count_file = 'profile_views.txt'
    if os.path.exists(count_file):
        with open(count_file, 'r+') as f:
            count = int(f.read().strip())
            if not visitor_is_self():
                count += 1
                f.seek(0)
                f.write(str(count))
                f.truncate()
            return count
    else:
        return None

def visitor_is_self():
    return False

new_count = increment_profile_views()
if new_count is not None:
    print(f'Profile views: {new_count}')
