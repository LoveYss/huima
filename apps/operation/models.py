from datetime import datetime

from django.db import models

from user.models import User
from course.models import Course, Chapter, Video
from blog.models import Blog
from subject.models import ProjectDetail
from task.models import QuestionsBank, Questions


# Create your models here.
# 用户课程
class UserCourse(models.Model):
    user = models.ForeignKey(User, verbose_name='用户名', on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, verbose_name='课程名', on_delete=models.DO_NOTHING)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='初始点击时间')
    last_time = models.DateTimeField(default=datetime.now, verbose_name='最后点击时间')
    is_favorite = models.BooleanField(default=False, verbose_name='是否收藏')
    favorite_time = models.DateTimeField(default=datetime.now, verbose_name='收藏时间')
    is_like = models.BooleanField(default=False, verbose_name='是否点赞')
    study_time = models.TimeField(max_length=20, verbose_name='学习时长')

    class Meta:
        verbose_name = '课程用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s - %s' % (self.user, self.course)


# 课程评论
class CourseComment(models.Model):
    user = models.ForeignKey(User, verbose_name='用户名', on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, verbose_name='评论课程名', on_delete=models.DO_NOTHING)
    comment = models.TextField(verbose_name='评论内容')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    like_num = models.BooleanField(default=False, verbose_name='被点赞数')

    class Meta:
        verbose_name = '课程评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s - %s' % (self.user, self.course)


# 用户章节
class UserChapter(models.Model):
    user = models.ForeignKey(User, verbose_name='用户名', on_delete=models.DO_NOTHING)
    chapter = models.ForeignKey(Chapter, verbose_name='章节名', on_delete=models.DO_NOTHING)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='初始点击时间')
    last_time = models.DateTimeField(default=datetime.now, verbose_name='最后点击时间')
    is_favorite = models.BooleanField(default=False, verbose_name='收藏')
    favorite_time = models.DateTimeField(default=datetime.now, verbose_name='收藏时间')
    is_like = models.BooleanField(default=False, verbose_name='点赞')

    class Meta:
        verbose_name = '用户章节'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s - %s' % (self.user, self.chapter)


# 章节QA
class ChapterQA(models.Model):
    chapter = models.ForeignKey(Chapter, verbose_name='章节名', on_delete=models.DO_NOTHING)
    question = models.CharField(max_length=255, verbose_name='Q')
    answer = models.CharField(max_length=255, verbose_name='A')

    class Meta:
        verbose_name = '章节QA'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s - %s' % (self.chapter, self.question)


# 用户视频
class UserVideo(models.Model):
    user = models.ForeignKey(User, verbose_name='用户名', on_delete=models.DO_NOTHING)
    video = models.ForeignKey(Video, verbose_name='视频名', on_delete=models.DO_NOTHING)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='初始点击时间')
    is_like = models.BooleanField(default=False, verbose_name='点赞')

    class Meta:
        verbose_name = '用户视频'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s - %s' % (self.user, self.video)


# 用户视频问答
class VideoQA(models.Model):
    user = models.ForeignKey(User, verbose_name='用户名', on_delete=models.DO_NOTHING)
    video = models.ForeignKey(Video, verbose_name='视频名', on_delete=models.DO_NOTHING)
    content = models.CharField(max_length=2048, verbose_name='内容')
    is_reply_user = models.BooleanField(default=False, verbose_name='是否是回复别人')
    reply_user = models.IntegerField(default=0, verbose_name='被回复人ID')
    status = models.BooleanField(default=False, verbose_name='激活状态')

    class Meta:
        verbose_name = '视频问答'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s - %s - %s' % (self.user, self.video, self.reply_user)


# 用户博客
class UserBlog(models.Model):
    user = models.ForeignKey(User, verbose_name='用户名', on_delete=models.DO_NOTHING)
    blog = models.ForeignKey(Blog, verbose_name='博客名', on_delete=models.DO_NOTHING)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='初始浏览时间')
    last_time = models.DateTimeField(default=datetime.now, verbose_name='最后浏览时间')
    is_favorite = models.BooleanField(default=False, verbose_name='收藏')
    favorite_time = models.DateTimeField(default=datetime.now, verbose_name='收藏时间')
    is_like = models.BooleanField(default=False, verbose_name='点赞')

    class Meta:
        verbose_name = '博客用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s - %s' % (self.user, self.blog)


# 博客回复
class BlogComment2(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户名")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name="回复博客名")
    content = models.TextField(verbose_name="回复内容")
    add_time = models.DateTimeField(auto_now=True, verbose_name="回复时间")
    like_num = models.IntegerField(default=0, verbose_name="被点赞数")

    def __str__(self):
        return '%s - %s' % (self.user, self.blog)

    class Meta:
        ordering = ['add_time']
        verbose_name = '博客回复'
        verbose_name_plural = verbose_name


# 用户项目
class UserProject(models.Model):
    user = models.ForeignKey(User, verbose_name='用户名', on_delete=models.DO_NOTHING)
    project = models.ForeignKey(ProjectDetail, verbose_name='项目名', on_delete=models.DO_NOTHING)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='初始点击时间')
    last_time = models.DateTimeField(default=datetime.now, verbose_name='最后点击时间')
    is_favorite = models.BooleanField(default=False, verbose_name='收藏')
    favorite_time = models.DateTimeField(default=datetime.now, verbose_name='收藏时间')
    is_like = models.BooleanField(default=False, verbose_name='点赞')

    class Meta:
        verbose_name = '项目用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s - %s' % (self.user, self.project)


# # 用户题库
# class UserTask(models.Model):
#     user = models.ForeignKey(User, verbose_name='用户', on_delete=models.DO_NOTHING)
#     questions_bank = models.ForeignKey(QuestionsBank, verbose_name='试题库', on_delete=models.DO_NOTHING)
#     add_time = models.DateTimeField(default=datetime.now, verbose_name='初始点击时间')
#     last_time = models.DateTimeField(default=datetime.now, verbose_name='最后点击时间')
#
#     class Meta:
#         verbose_name = '用户题库'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return '%s - %s' % (self.user, self.questions_bank)


# 用户试题
class UserQuestion(models.Model):
    user = models.ForeignKey(User, verbose_name='用户名', on_delete=models.DO_NOTHING)
    questions = models.ForeignKey(Questions, verbose_name='试题名', on_delete=models.DO_NOTHING)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='初始点击时间')
    last_time = models.DateTimeField(default=datetime.now, verbose_name='最后点击时间')
    is_favorite = models.BooleanField(default=False, verbose_name='收藏')
    favorite_time = models.DateTimeField(default=datetime.now, verbose_name='收藏时间')
    is_like = models.BooleanField(default=False, verbose_name='点赞')
    is_correct = models.BooleanField(default=False, verbose_name='回答正确')

    class Meta:
        verbose_name = '试题用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s - %s' % (self.user, self.questions)


# 试题评论
class QuestionComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户名")
    questions = models.ForeignKey(Questions, verbose_name='试题名', on_delete=models.DO_NOTHING)
    content = models.TextField(verbose_name="评论内容")
    add_time = models.DateTimeField(auto_now=True, verbose_name="评论")
    like_num = models.IntegerField(default=0, verbose_name="被点赞数")

    class Meta:
        verbose_name = '试题评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s - %s' % (self.user, self.questions)


# 消息分类
class MessageCategory(models.Model):
    name = models.CharField(max_length=20, verbose_name='类别名')

    class Meta:
        verbose_name = '消息分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 发送信息
class UserMessage(models.Model):
    # 发送给所有用户为0
    user = models.IntegerField(default=0, verbose_name='目标用户')
    message = models.CharField(max_length=500, verbose_name='消息内容')
    is_read = models.BooleanField(default=False, verbose_name='是否已读')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='消息时间')
    type = models.ForeignKey(MessageCategory, verbose_name='消息分类', on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = '消息'
        verbose_name_plural = verbose_name
