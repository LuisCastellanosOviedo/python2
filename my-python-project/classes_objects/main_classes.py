from classes_objects.post import Post
from classes_objects.user import User

tony_stark = User("test@gmail.com", "tony stark", "12345", "stark industries CEO")
tony_stark.get_user_info()

tony_stark.change_job_title("stark industries CTO")
tony_stark.get_user_info()

app_user_two = User("bbb@gmail.com","james bond" , "asdfw4vrwef", "Agent")
app_user_two.get_user_info()


post = Post("on a secret mission", app_user_two.name)
post.get_post_info()