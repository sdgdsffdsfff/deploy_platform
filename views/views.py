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


class Post_View_Handler(BaseHandler):
    def post(self):
        print  self.get_argument("pro_name")
        print  self.get_argument("git_addr")
        print  self.get_argument("exec_shell_1")
        print  self.get_argument("exec_shell_2")
        print "ssh",self.get_argument("ssh_server")
        print  self.get_argument("local_path")
        print  self.get_argument("remove_path")
        print  self.get_argument("remote_path")
        print  self.get_argument("mail_name")
        print  self.get_argument("mail_subject")
        print  self.get_argument("mail_data")
        print  self.get_argument("pro_name")
        print  self.get_argument("pro_name")
	self.write("提交成功")
