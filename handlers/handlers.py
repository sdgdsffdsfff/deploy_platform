from views.views import *
import os.path

STATIC_PATH   = os.path.join(os.path.dirname(__file__), "../static")
TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "../templates")
HANDLERS =[(r"/develop/" ,Develop_Handler),
	   (r"/view/",View_Handler),
	   (r"/post_view/",Post_View_Handler),
	   (r"/add_group/",Add_Group_Handler),
	   (r"/",All_Handler),
	]
HANDLERS +=[(r"/chart/", ChartHandler)]
