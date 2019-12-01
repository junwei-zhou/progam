from django.db import models
from datetime import datetime
from organization.models import CourseOrg

class Course(models.Model):
    DEGREE_CHOICES = (
        ("cj", "初级"),
        ("zj", "中级"),
        ("gj", "高级")
    )
    name = models.CharField("课程名",max_length=50)
    desc = models.CharField("课程描述",max_length=300)
    detail = models.TextField("课程详情")
    degree = models.CharField('难度',choices=DEGREE_CHOICES, max_length=2)
    learn_times = models.IntegerField("学习时长(分钟数)",default=0)
    students = models.IntegerField("学习人数",default=0)
    fav_nums = models.IntegerField("收藏人数",default=0)
    image = models.ImageField("封面图",upload_to="courses/%Y/%m",max_length=100)
    click_nums = models.IntegerField("点击数",default=0)
    add_time = models.DateTimeField("添加时间",default=datetime.now,)
    course_org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name="所属机构", null=True, blank=True)

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 章节
class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程",on_delete=models.CASCADE)
    name = models.CharField(max_length=100,verbose_name=u"章节名称")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")
    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name

# 视频
class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u"章节",on_delete=models.CASCADE)
    name = models.CharField(max_length=100,verbose_name=u"视频名称")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name

#   课程资源
class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程",on_delete=models.CASCADE)
    # 自动生成上传按钮
    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name=u"资源文件", max_length=100)
    name = models.CharField(max_length=100, verbose_name=u"课程资源")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name

