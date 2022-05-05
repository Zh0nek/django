from django.db import models
from users.models import User


class GradedAssignmentTestManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(assignment__teacher__username='testt')


class QuestionTestManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(question='test')


class ChoiceTestManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(title='test')


class AssignmentTestManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(title='test')


class Assignment(models.Model):
    title = models.CharField(max_length=50)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = models.Manager()  # The default manager.
    test_assignments = AssignmentTestManager()

    def __str__(self):
        return self.title


class GradedAssignment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment = models.ForeignKey(
        Assignment, on_delete=models.SET_NULL, blank=True, null=True)
    grade = models.FloatField()
    objects = models.Manager()  # The default manager.
    test_teachers = GradedAssignmentTestManager()

    def __str__(self):
        return self.student.username


class Choice(models.Model):
    assignment = models.ForeignKey(
        Assignment, on_delete=models.CASCADE, related_name='choices', blank=True, null=True)
    title = models.CharField(max_length=50)
    objects = models.Manager()  # The default manager.
    test_choices = ChoiceTestManager()

    def __str__(self):
        return self.title


class Question(models.Model):
    question = models.CharField(max_length=200)
    choices = models.ManyToManyField(Choice)
    answer = models.ForeignKey(
        Choice, on_delete=models.CASCADE, related_name='answer', blank=True, null=True)
    assignment = models.ForeignKey(
        Assignment, on_delete=models.CASCADE, related_name='questions', blank=True, null=True)
    order = models.SmallIntegerField()

    objects = models.Manager()  # The default manager.
    test_questions = QuestionTestManager()

    def __str__(self):
        return self.question
