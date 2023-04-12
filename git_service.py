import os
import shutil
from datetime import date
from github import Github


def git_backip():
    github_username = '**'
    github_password = '**'
    repository_name = '**'
    repository_owner = '**'

    git_hub = Github(github_username, github_password)

    repo = git_hub.get_user(repository_owner).get_repo(repository_name)

    today = date.today()
    today_str = today.strftime('%Y-%m-%d')

    backup_dir = f'{os.getcwd()}\{repository_name}-{today_str}-backup'

    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    repo_clone = repo.clone_url
    clone = "git clone " + repo_clone
    os.chdir(backup_dir)
    os.system(clone)
    shutil.make_archive(backup_dir, "zip", backup_dir)
    print(f'{repository_name} backed up successfully to {backup_dir}.')
