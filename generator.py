import requests

# Function to fetch user data from the GitHub API
def get_github_data(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error: Unable to fetch GitHub data.")
        return None

# Function to get user input for GitHub README
def get_user_input():
    name = input("Enter your name: ")
    username = input("Enter your GitHub username: ")
    bio = input("Enter a short bio: ")
    job = input("Enter your job title: ")
    favorite_languages = input("Enter your favorite programming languages (comma-separated): ")
    background_color = input("Enter a background color (hex or name, press Enter to skip): ")
    text_color = input("Enter a text color (hex or name, press Enter to skip): ")
    show_github_stats = input("Include GitHub statistics (followers, following, public repos)? (y/n): ")
    return name, username, bio, job, favorite_languages, background_color, text_color, show_github_stats.lower() == "y"

# Function to generate the GitHub Profile README in Markdown format
def generate_readme(name, username, bio, job, favorite_languages, background_color, text_color, show_github_stats):
    user_data = get_github_data(username) if show_github_stats else None

    # Create the Markdown content
    readme = f"# {name}\n\n"
    readme += f"**GitHub Username:** {username}\n\n"
    readme += f"**Bio:** {bio}\n\n"
    readme += f"**Job:** {job}\n\n"
    readme += f"**Favorite Languages:** {favorite_languages}\n"

    if show_github_stats and user_data:
        followers = user_data["followers"]
        following = user_data["following"]
        public_repos = user_data["public_repos"]
        readme += f"\n**Followers:** {followers}  **Following:** {following}  **Public Repos:** {public_repos}\n"

    # Add custom styles for the README
    if background_color and text_color:
        readme = f'<div style="background-color: {background_color}; color: {text_color}; padding: 20px;">\n{readme}\n</div>'

    return readme

# Main function
def main():
    name, username, bio, job, favorite_languages, background_color, text_color, show_github_stats = get_user_input()
    readme_content = generate_readme(name, username, bio, job, favorite_languages, background_color, text_color, show_github_stats)

    if readme_content:
        with open("README.md", "w") as file:
            file.write(readme_content)
        print("README.md has been created successfully.")
    else:
        print("Error: Unable to generate README.")

if __name__ == "__main__":
    main()
