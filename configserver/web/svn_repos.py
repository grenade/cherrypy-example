import os
import cherrypy
from datetime import datetime
from cherrypy.lib import static

from configserver import settings

from configserver.tools.svn_repos import get_repo_list
from configserver.tools.common import render_template, info, error, success, warning


class RepoServer:
	@cherrypy.expose
	def index(self):
		repo_list = get_repo_list()
		return render_template("svnrepos.html", repo_list=repo_list)
		