import os
import logging

from configserver import settings

log = logging.getLogger(__name__)


def get_repo_list():
    repo_list = []
    for repo_dir in os.listdir(settings.SVN_REPO_DIR):
        repo_list.append(repo_dir)
        
    log.debug('Found repositories: %s', str(repo_list))
    return repo_list