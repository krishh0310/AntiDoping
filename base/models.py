from django.db import models


class Module(models.Model):
    title   = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    order   = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.order}. {self.title}"


class ModulePart(models.Model):
    module  = models.ForeignKey(Module, on_delete=models.CASCADE,
                                related_name='parts')
    title   = models.CharField(max_length=200)
    content = models.TextField()
    order   = models.IntegerField(default=1)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.module.title} – Part {self.order}: {self.title}"


class QuizQuestion(models.Model):
    module         = models.ForeignKey(Module, on_delete=models.CASCADE,
                                       related_name='questions', null=True, blank=True)
    question       = models.CharField(max_length=255)
    option_a       = models.CharField(max_length=200)
    option_b       = models.CharField(max_length=200)
    option_c       = models.CharField(max_length=200)
    option_d       = models.CharField(max_length=200)
    correct_option = models.CharField(max_length=1)

    def __str__(self):
        return self.question


class QuizResult(models.Model):
    student_name = models.CharField(max_length=100, default="Participant")
    score        = models.IntegerField()
    total        = models.IntegerField()
    module       = models.ForeignKey(Module, on_delete=models.SET_NULL,
                                     null=True, blank=True)
    created_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} - {self.score}/{self.total}"


class Update(models.Model):
    title      = models.CharField(max_length=200)
    message    = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title