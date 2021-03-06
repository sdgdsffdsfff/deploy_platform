from views.views import *
import os.path

STATIC_PATH   = os.path.join(os.path.dirname(__file__), "../static")
TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "../templates")
HANDLERS =[(r"/develop/" ,Develop_Handler),
	   (r"/view/",View_Handler),
	   (r"/charts/",ChartHandler),
	   (r"/schedule/",Schedule_Handler),
	   (r"/exec_build/",Exec_Build_Handler),
	   (r"/post_view/",Post_View_Handler),
	   (r"/add_group/",Add_Group_Handler),
	   (r"/all/(.*)/",All_Handler),
	   (r"/",Index_Handler),
	]
HANDLERS +=[(r"/chart/", ChartHandler)]
