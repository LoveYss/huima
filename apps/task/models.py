# -*- coding: utf-8 -*-
from django.db import models
from apps import course


class QuestionsBank(models.Model):
    its_course = models.ForeignKey('course.Chapter', on_delete=models.DO_NOTHING,
                                   verbose_name='所属章节', null=True, blank=True)
    QuestionsBank_name = models.CharField(max_length=500, verbose_name="题库名称")
    QuestionsBank_describe = models.CharField(max_length=700, verbose_name="题库简介", null=True, blank=True)
    create_time = models.DateField(verbose_name="创建时间", null=True, blank=True)
    schedule = models.IntegerField(verbose_name="进度时间", null=True, blank=True)


class Questions(models.Model):
    category = models.CharField(max_length=20, verbose_name="任务类别",
                                choices=(('1', '基础任务'), ('2', '进阶任务')), default='基础任务')
    title = models.CharField(max_length=500, verbose_name="任务题目")
    questions_img = models.ImageField(upload_to='questions_img/%Y/%m/%d', null=True, blank=True)
    select_answer_A = models.CharField(max_length=200, verbose_name="选项A", null=False, blank=False, default='')
    select_answer_B = models.CharField(max_length=200, verbose_name="选项B", null=False, blank=False, default='')
    select_answer_C = models.CharField(max_length=200, verbose_name="选项C", null=True, blank=True)
    select_answer_D = models.CharField(max_length=200, verbose_name="选项D", null=True, blank=True)
    select_answer_E = models.CharField(max_length=200, verbose_name="选项E", null=True, blank=True)
    select_answer_F = models.CharField(max_length=200, verbose_name="选项F", null=True, blank=True)
    select_answer_G = models.CharField(max_length=200, verbose_name="选项G", null=True, blank=True)
    answer = models.CharField(max_length=20, verbose_name="正确答案", choices=(('0', 'A'), ('1', 'B'), ('2', 'C'),
                                                                        ('3', 'D'), ('4', 'E'), ('5', 'F'), ('6', 'G')),
                              null=False, blank=False)
    create_time = models.DateField(verbose_name="创建时间", null=True, blank=True)
    schedule = models.IntegerField(verbose_name="进度时间", null=True, blank=True)
    its_QuestionsBank = models.ForeignKey(QuestionsBank, verbose_name='所属题库', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '任务'
        verbose_name_plural = verbose_name
# Create your models here.
