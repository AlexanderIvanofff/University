from django.db import models


class Title(models.Model):
    title_name = models.CharField(max_length=200)

    def __str__(self):
        return self.title_name


class Professors(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    titles = models.ForeignKey(Title, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Course(models.Model):
    title = models.CharField(max_length=200)
    credits = models.IntegerField()
    professor = models.ForeignKey(Professors, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'


class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    courses = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.courses}'
