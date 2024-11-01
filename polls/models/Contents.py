from django.db import models

from . import Users

class Contents(models.Model):
    contentId = models.AutoField(primary_key=True)  # 自動でインクリメントされる整数の主キー
    content = models.TextField()  # テキスト型
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)  # Userテーブルの外部キー
    date = models.DateTimeField()  # タイムスタンプ型