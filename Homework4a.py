import requests


def repository_list(GIT_ID):
    repository_data = requests.get(f"https://api.github.com/users/{GIT_ID}/repos")
    arr = []
    if repository_data:
        repository_data_json = repository_data.json()
        for repo in repository_data_json:
            repository_name = repo["name"]
            commits_data = requests.get(
                f"https://api.github.com/repos/{GIT_ID}/{repository_name}/commits"
            )
            if commits_data:
                commits_json = commits_data.json()
                arr.append((repository_name, len(commits_json)))
            else:
                return f"ERROR: Cannot Retrieve Commit Data '{repository_name}' STATUS CODE: {repository_data.status_code}: {repository_data.reason}"
        return arr
    else:
        return f"ERROR: Cannot Retrieve Repository Data {repository_data.status_code}: {repository_data.reason}"


if __name__ == "__main__":
    USER_ID = "douglas0520"
    result = repository_list(USER_ID)
    if isinstance(result, list):
        for repository_print in result:
            print(repository_print[0] + ":", repository_print[1])
    else:
        print(result)
