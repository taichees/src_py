from django.db import models

from . import Users

class Contents(models.Model):
    contentsId = models.AutoField(primary_key=True)  # 自動でインクリメントされる整数の主キー
    content = models.TextField()  # テキスト型
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)  # Userテーブルの外部キー
    data = models.TextField()  # テキスト型

    # def __str__(self):
    #     return self.content