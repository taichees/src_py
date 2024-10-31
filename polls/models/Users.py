from django.db import models

class Users(models.Model):
    userId = models.AutoField(primary_key=True)  # 自動でインクリメントされる整数の主キー
    userName = models.TextField()  # テキスト型
    password = models.TextField()  # テキスト型

    # def __str__(self):
    #     return self.userName