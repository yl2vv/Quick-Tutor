# from django.contrib.auth.models import User

# from allauth.exceptions import ImmediateHttpResponse
# from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


# class MyAdapter(DefaultSocialAccountAdapter):
#     def pre_social_login(self, request, sociallogin):
#         try:
#             print(sociallogin.values)
#             #sociallogin.connect(request, user)
#             # Create a response object
#             #raise ImmediateHttpResponse(response)
#         except User.DoesNotExist:
#             pass