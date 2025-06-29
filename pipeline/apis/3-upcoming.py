#!/usr/bin/env python3
"""
Uses the (unofficial) SpaceX API to print the upcoming launch as:
<launch name> (<date>) <rocket name> - <launchpad name> (<launchpad locality>)
"""

import requests

if __name__ == "__main__":
    launches_url = "https://api.spacexdata.com/v4/launches/upcoming"
    launches = requests.get(launches_url).json()

    # Get launch with earliest date_unix
    earliest = None
    for launch in launches:
        if earliest is None or launch["date_unix"] < earliest["date_unix"]:
            earliest = launch

    # Get relevant data
    launch_name = earliest["name"]
    date_local = earliest["date_local"]
    rocket_id = earliest["rocket"]
    pad_id = earliest["launchpad"]

    # Get rocket name
    rocket_url = f"https://api.spacexdata.com/v4/rockets/{rocket_id}"
    rocket_name = requests.get(rocket_url).json().get("name")

    # Get launchpad name and locality
    pad_url = f"https://api.spacexdata.com/v4/launchpads/{pad_id}"
    pad_info = requests.get(pad_url).json()
    pad_name = pad_info.get("name")
    pad_locality = pad_info.get("locality")

    # Final output
    print(f"{launch_name} ({date_local}) {rocket_name} - {pad_name} ({pad_locality})")
