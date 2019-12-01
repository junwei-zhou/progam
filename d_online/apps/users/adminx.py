
import xadmin
from xadmin import views
#注册邮箱验证
from .models import EmailVerifyRecord,Banner

class BaseSetting(object):
    #这些主题菜单需要在有网络的情况下，才会使用出来
    enable_themes = True
    use_bootswatch = True

# 全局修改，固定写法
class GlobalSettings(object):
    # 修改title
    site_title = '慕雪课堂后台管理界面'
    # 修改footer
    site_footer = '慕雪课堂'
    # 收起菜单
    menu_style = 'accordion'

class EmailVerifyRecordAdmin(object):
    list_display = ['code','email','send_type','send_time',]
    # 创建搜索框
    search_fields = ['code','email','send_type',]
    #筛选
    list_filter = ['code','email','send_type','send_time',]

class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    # 创建搜索框
    search_fields = ['title', 'image', 'url', 'index', ]
    # 筛选
    list_filter = ['title', 'image', 'url', 'index', 'add_time']

xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)