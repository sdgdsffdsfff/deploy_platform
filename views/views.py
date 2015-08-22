# -*- coding: utf-8 -*- 

import tornado.web
import time
class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
     return self.application.db
    def get_current_user(self):
     return self.get_secure_cookie("user")

class ChartHandler(BaseHandler):
    def get(self):
        self.render('chart.html') 

class Develop_Handler(BaseHandler):
    def get(self):
        self.render('develop.html') 

class View_Handler(BaseHandler):
    def get(self):
        self.render('view.html') 
class All_Handler(BaseHandler):
    def get(self):
        self.render('index.html') 


class Post_View_Handler(BaseHandler):
    def post(self):
        pro_name 	= self.get_argument("pro_name")
        pro_desc 	= self.get_argument("pro_desc")
        git_addr 	= self.get_argument("git_addr")
        exec_shell_1 	= self.get_argument("exec_shell_1")
        exec_shell_2 	= self.get_argument("exec_shell_2")
        ssh_server 	= self.get_argument("ssh_server")
        local_path 	= self.get_argument("local_path")
        remove_path 	= self.get_argument("remove_path")
        remote_path 	= self.get_argument("remote_path")
        mail_name 	= self.get_argument("mail_name")
        mail_subject 	= self.get_argument("mail_subject")
        mail_data 	= self.get_argument("mail_data")
        remote_exec_shell = self.get_argument("remote_exec_shell")
	if not self.db.exists(pro_name):
	    self.db.rpush( pro_name, pro_desc, git_addr, exec_shell_1, exec_shell_2, ssh_server, local_path, remove_path, remote_path,mail_name, mail_subject, mail_data, remote_exec_shell)
	    self.write("提交成功")
	else:
	    self.write("此工程项目已经存在")
