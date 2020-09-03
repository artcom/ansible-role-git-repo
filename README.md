# Git Repo
Initializes a git repository and optionally configures post-update and update hooks. To use the hooks they must be present on the file system.

## Requirements
None.

## Role Variables
Available variables are listed below, along with default values `(see defaults/main.yml)`:
```yaml
git_repo_directory: null
git_repo_name: null
git_repo_owner: root
git_repo_group: root
git_repo_post_update_hook: null
git_repo_update_hook: null
git_server_restart_command: null
```
Mandatory variables (role will fail if the variables are not set):
```yaml
git_repo_directory: "string"
git_repo_name: "string"
git_server_restart_command: "string"
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
        git_repo_post_update_hook: /usr/local/bin/post-update-hook
        git_repo_update_hook: /usr/local/bin/update-hook
        git_server_restart_command: "systemctl restart git-server"
```

## Test
### Requirements
- python >= 3.7
- docker

### Run
```bash
pip install -r requirements.txt
molecule test --all
```

## License
MIT
