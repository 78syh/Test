import os

COMMIT_SHA = os.getenv("GITHUB_SHA")

print(COMMIT_SHA)
