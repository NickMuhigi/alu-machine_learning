#!/usr/bin/env python3
"""
Uses the (unofficial) SpaceX API to print the upcoming launch as:
<launch name> (<date>) <rocket name> - <launchpad name> (<launchpad locality>)

The “upcoming launch” is the one which is the soonest from now, in UTC
and if 2 launches have the same date, it's the first one in the API result.
"""

import requests

if __name__ == "__main__":
    # Fetch upcoming launches
    url = "https://api.spacexdata.com/v4/launches/upcoming"
    response = requests.get(url)
    launches = response.json()

    # Find the launch with the earliest date_unix
    earliest = None
    for launch in launches:
        if earliest is None or launch['date_unix'] < earliest['date_unix']:
            earliest = launch

    # Extract launch data
    launch_name = earliest.get('name')
    date_local = earliest.get('date_local')
    rocket_id = earliest.get('rocket')
    pad_id = earliest.get('launchpad')

    # Fetch rocket info
    rocket_url = f"https://api.spacexdata.com/v4/rockets/{rocket_id}"
    rocket_name = requests.get(rocket_url).json().get('name')

    # Fetch launchpad info
    pad_url = f"https://api.spacexdata.com/v4/launchpads/{pad_id}"
    pad_data = requests.get(pad_url).json()
    pad_name = pad_data.get('name')
    pad_locality = pad_data.get('locality')

    # Print result in required format
    print(f"{launch_name} ({date_local}) {rocket_name} - {pad_name} ({pad_locality})")
