import requests

GITHUB_TOKEN = ""  # Git Token
REPO = "" # GIt Repo
headers = {"Authorization": f"token {GITHUB_TOKEN}"}


def delete_artifact():
    print("Deleting GitHub Actions artifact...")
    artifacts_url = f"https://api.github.com/repos/{REPO}/actions/artifacts"
    response = requests.get(artifacts_url, headers=headers)
    artifacts = response.json().get("artifacts", [])
    print(artifacts)

    for artifact in artifacts:
        artifact_id = artifact["id"]
        delete_url = f"https://api.github.com/repos/{REPO}/actions/artifacts/{artifact_id}"
        del_response = requests.delete(delete_url, headers=headers)
        if del_response.status_code == 204:
            print(f"Deleted artifact ID: {artifact_id}")
        else:
            print(f"Failed to delete artifact ID: {artifact_id}")


def delete_caches():
    print("Deleting GitHub Actions cache...")
    cache_url = f"https://api.github.com/repos/{REPO}/actions/caches"
    response = requests.get(cache_url, headers=headers)

    if response.status_code == 200:
        caches = response.json().get("actions_caches", [])
        print(caches)
        for cache in caches:
            cache_id = cache["id"]
            delete_url = f"{cache_url}/{cache_id}"
            del_response = requests.delete(delete_url, headers=headers)
            if del_response.status_code == 204:
                print(f"Deleted cache ID: {cache_id}")
            else:
                print(f"Failed to delete cache ID: {cache_id}")
    else:
        print("Failed to fetch caches. Status code:", response.status_code)


def delete_workflow_runs():
    print("Deleting GitHub Actions workflow runs...")
    runs_url = f"https://api.github.com/repos/{REPO}/actions/runs"
    response = requests.get(runs_url, headers=headers)
    print(response)

    if response.status_code == 200:
        runs = response.json().get("workflow_runs", [])
        for run in runs:
            run_id = run["id"]
            delete_url = f"{runs_url}/{run_id}"
            del_response = requests.delete(delete_url, headers=headers)
            if del_response.status_code == 204:
                print(f"Deleted workflow run ID: {run_id}")
            else:
                print(f"Failed to delete workflow run ID: {run_id}")
    else:
        print("Failed to fetch workflow runs. Status code:", response.status_code)


delete_artifact()
delete_caches()
delete_workflow_runs()