# Git Repo
Initializes a git repository and configures hooks. Intended for use with [backend-git container]***REMOVED***.

## Requirements
None.

## Role Variables
Available variables are listed below, along with default values `(see defaults/main.yml)`:
```yaml

```

## Dependencies
None.

# Example Playbook
```yaml
- name: Initialize git repo
  hosts: all
  become: true
  roles:
    - role: git-repo
      vars:
        repo_path: /var/local/repos/repo_name
        hooks:
          post-update: true
          update: true
```

## Test
### Requirements
- python >= 3.7
- docker

### Run
```bash
pip install -r requirements.txt
molecule test
```

## License
MIT
