# Git Repo
Initializes a git repository and configures hooks. Intended for use with [backend-git container]***REMOVED***.

## Requirements
None.

## Role Variables
Available variables are listed below, along with default values `(see defaults/main.yml)`:
```yaml
git_repo_directory: /var/local/repos
git_repo_name: repo_name
git_repo_post_update_hook: false
git_repo_update_hook: false
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
        git_repo_directory: /var/local/repos
        git_repo_name: repo_name
        git_repo_post_update_hook: true
        git_repo_update_hook: true
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
