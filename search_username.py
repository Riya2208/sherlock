import requests

def search_username(username: str) -> dict:
    """
    Searches for the given username across multiple social networks.

    Args:
        username (str): The username to search for.

    Returns:
        dict: A dictionary containing social networks as keys and the corresponding account URLs as values.
        
    Example:
        >>> search_username('exampleUser')
        {'twitter': 'https://twitter.com/exampleUser', 'facebook': 'https://facebook.com/exampleUser'}
    """
    results = {}
    social_networks = ['twitter', 'facebook', 'instagram', 'linkedin']  # Add more networks as needed

    for network in social_networks:
        response = requests.get(f"https://api.{network}.com/users/{username}")
        if response.status_code == 200:
            results[network] = response.url  # Or any other logic to extract the account URL

    return results
