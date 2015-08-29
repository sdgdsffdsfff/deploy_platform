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
    ''' 
    设置具体job的信息
    ''' 
    def get(self):
	data = self.db.lrange("PROJECT_NAME",0,-1)
        self.render('view.html', data = data) 

class All_Handler(BaseHandler):
    '''
    在首页展示分组的汇总信息
    '''
    def get(self,group_name):
        self.group_name = group_name 
	data = self.db.lrange("PROJECT_NAME",0,-1)
	group_table = self.db.hgetall(self.group_name)
        self.render('index.html', data = data, group_table = group_table ) 
class Index_Handler(BaseHandler):
    '''
    重定向到all汇总信息页面
    '''
    def get(self):
	data = self.db.lrange("PROJECT_NAME",0,-1)
        group_hash_key = ''.join((eval(data[0])).keys())
	self.redirect('/all/%s/'%(group_hash_key) , permanent=True)

class Post_View_Handler(BaseHandler):
    '''
    项目构建提交的资料
    '''
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
        print  self.get_argument("select_group")
	if not self.db.exists(pro_name):
	    self.db.rpush( pro_name, pro_desc, git_addr, exec_shell_1, exec_shell_2, ssh_server, local_path, remove_path, remote_path,mail_name, mail_subject, mail_data, remote_exec_shell)
	    self.write("提交成功")
	else:
	    self.write("此工程项目已经存在")

class Add_Group_Handler(BaseHandler):
    '''
    增加分组到REDIS的hash
    '''
    def post(self):
        Group_Name = self.get_argument("Group_Name")
        Group_Desc = self.get_argument("Group_Desc")
	gro_dict={}
	gro_dict[Group_Name] = Group_Desc
	G_redis_name="PROJECT_NAME"
	if self.db.rpush(G_redis_name,gro_dict):
	    self.write("提交成功")
