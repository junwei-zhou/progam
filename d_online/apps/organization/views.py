from django.shortcuts import render

from django.views.generic import View
from .models import CourseOrg,CityDict
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from django.http import HttpResponse
from .forms import UserAskForm

class OrgView(View):
    '''课程机构'''

    def get(self, request):
        # 所有课程机构,下面的数据头都是数据模型而来的
        all_orgs = CourseOrg.objects.all()

        # 所有城市，下面的数据是由数据模型提供的
        all_citys = CityDict.objects.all()
        # 城市筛选
        city_id = request.GET.get('city','')
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        # 类别筛选
        category = request.GET.get('ct','')
        if category:
            all_orgs = all_orgs.filter(category=category)

        # 热门课程机构排名，按逆序输出三个
        hot_orgs = all_orgs.order_by('-click_nums')[:3]
        # 学习人数和课程数筛选
        sort = request.GET.get('sort', "")
        if sort:
            if sort == "students":
                all_orgs = all_orgs.order_by("-students")
            elif sort == "courses":
                all_orgs = all_orgs.order_by("-course_nums")
        # 有多少家机构
        org_nums = all_orgs.count()
        # 对课程机构进行分页
        # 尝试获取前台get请求传递过来的page参数
        # 如果是不合法的配置参数默认返回第一页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        # 这里指从allorg中取五个出来，每页显示5个
        p = Paginator(all_orgs, 2, request=request)
        orgs = p.page(page)
        #下面返回的属性值，是交给前端来进行逻辑判断显示的
        return render(request, "org-list.html", {
            "all_orgs": orgs,
            "all_citys": all_citys,
            "org_nums": org_nums,
            'city_id':city_id,
            "category": category,
            'hot_orgs':hot_orgs,
            'sort':sort,
        })


class AddUserAskView(View):
    """
    用户添加咨询
    """
    def post(self, request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            user_ask = userask_form.save(commit=True)
            # 如果保存成功,返回json字符串,后面content type是告诉浏览器返回的数据类型
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            # 如果保存失败，返回json字符串,并将form的报错信息通过msg传递到前端
            return HttpResponse('{"status":"fail", "msg":"添加出错"}', content_type='application/json')


class OrgHomeView(View):
    '''机构首页'''

    def get(self,request,org_id):
        # 根据id找到课程机构
        course_org = CourseOrg.objects.get(id=int(org_id))
        # 反向查询到课程机构的所有课程和老师
        all_courses = course_org.course_set.all()[:4]
        all_teacher = course_org.teacher_set.all()[:2]
        return render(request,'org-detail-homepage.html',{
            'course_org':course_org,
            'all_courses':all_courses,
            'all_teacher':all_teacher,
        })