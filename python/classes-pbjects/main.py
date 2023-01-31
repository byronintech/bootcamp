from user import User
from post import Post

app_user_one = User("byronsmith@gmail.com", "Byron Smith", "password", "DevOps Engineer")
app_user_one.get_user_info()

app_user_one.change_job_title("Cloud Engineer")
app_user_one.get_user_info()

app_user_two = User("bs@gmail.com", "Barry Smith", "supersecret", "Python Developer")
app_user_two.get_user_info()

new_post = Post("on a secret mission today", app_user_two.name)
new_post.get_post_info()
