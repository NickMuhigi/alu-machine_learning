#!/usr/bin/env python3
"""
Uses the (unofficial) SpaceX API to print the upcoming launch as:
<launch name> (<date>) <rocket name> - <launchpad name> (<launchpad locality>)

The “upcoming launch” is the one which is the soonest from now, in UTC,
and if 2 launches have the same date, it's the first one in the API result.
"""

import requests


def get_upcoming_launch():
    """Fetch the soonest upcoming SpaceX launch and return its details."""
    # Fetch upcoming launches
    url = "https://api.spacexdata.com/v4/launches/upcoming"
    response = requests.get(url)
    launches = response.json()

    # Find the launch with the earliest date_unix
    earliest = None
    for launch in launches:
        if earliest is None or launch['date_unix'] < earliest['date_unix']:
            earliest = launch

    return earliest


def get_rocket_name(rocket_id):
    """Fetch and return the rocket name given its ID."""
    rocket_url = f"https://api.spacexdata.com/v4/rockets/{rocket_id}"
    rocket_data = requests.get(rocket_url).json()
    return rocket_data.get('name')


def get_launchpad_details(pad_id):
    """Fetch and return the launchpad name and locality given its ID."""
    pad_url = f"https://api.spacexdata.com/v4/launchpads/{pad_id}"
    pad_data = requests.get(pad_url).json()
    return pad_data.get('name'), pad_data.get('locality')


if __name__ == "__main__":
    # Get upcoming launch details
    launch = get_upcoming_launch()
    launch_name = launch.get('name')
    date_local = launch.get('date_local')
    rocket_id = launch.get('rocket')
    pad_id = launch.get('launchpad')

    # Fetch rocket and launchpad info
    rocket_name = get_rocket_name(rocket_id)
    pad_name, pad_locality = get_launchpad_details(pad_id)

    # Print final formatted output
    print(f"{launch_name} ({date_local}) {rocket_name} - "
          f"{pad_name} ({pad_locality})")
