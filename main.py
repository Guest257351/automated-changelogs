import os
import requests  # noqa We are just importing this to prove the dependency installed correctly


def main():
    commits = os.environ["commits"]

    version = os.environ["versionNo"]

    messages = '\n'.join([i.message for i in commits])

    changelog = f"""Version {version}
```md
{messages}
```
"""

    print(f"::set-output name=myOutput::{changelog}")


if __name__ == "__main__":
    main()
