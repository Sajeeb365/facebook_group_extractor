import facebook

# Set up the Graph API client
access_token = 'YOUR_ACCESS_TOKEN'
graph = facebook.GraphAPI(access_token)

# Read the list of group IDs from a file
group_ids = []
with open('group_list.txt', 'r') as file:
    group_ids = [line.strip() for line in file]

# Extract and filter the groups
filtered_groups = []
for group_id in group_ids:
    try:
        group = graph.get_object(group_id, fields='name,admin,privacy')
        if 'admin' in group and len(group['admin']['data']) == 0 and group.get('privacy') == 'OPEN':
            filtered_groups.append(group)
    except facebook.GraphAPIError:
        pass

# Print the filtered groups
for group in filtered_groups:
    print(group['name'], group['id'])
