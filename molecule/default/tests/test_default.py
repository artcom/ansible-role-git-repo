import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_git_installed(host):
    git = host.package('git')

    assert git.is_installed


def test_repo_folder(host):
    repo = host.file('/var/local/repos/repo_name')

    assert repo.exists
    assert repo.is_directory
    assert repo.user == 'www-data'
    assert repo.group == 'www-data'


def test_post_update_hook(host):
    post_update = host.file('/var/local/repos/repo_name/hooks/post-update')

    assert post_update.exists
    assert post_update.is_symlink
    assert post_update.linked_to == '/usr/local/bin/configuration-change-hook'
    assert post_update.user = 'www-data'
    assert post_update.group = 'www-data'


def test_update_hook(host):
    update = host.file('/var/local/repos/repo_name/hooks/update')

    assert update.exists
    assert update.is_symlink
    assert update.linked_to == '/usr/local/bin/validation-hook'
    assert update.user = 'www-data'
    assert update.group = 'www-data'
