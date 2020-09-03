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
    assert repo.user == 'root'
    assert repo.group == 'root'


def test_post_update_hook(host):
    post_update = host.file('/var/local/repos/repo_name/hooks/post-update')

    assert not post_update.exists


def test_update_hook(host):
    update = host.file('/var/local/repos/repo_name/hooks/update')

    assert not update.exists
