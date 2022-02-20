from django.db import models
from django.urls import reverse

# sms for verification
class SMS(models.Model):
    phone_number = models.CharField(max_length=20)
    code = models.IntegerField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f'User phone{self.phone_number} - verification {self.code}'

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    
    # def save(self, code, *args, **kwargs):
    #     code_item = []
    #     code_list = [i for i in range(10)]
    #     for in range(4):
    #         import random
    #         number_codes = random.choice(code_list)
    #         code_item.append(number_code)

    #         code_string = "".join(str(item) for item in number_code)
    #     code_string = code

    #     return self.code