class User:
    def __init__(self, email, name, password, current_job_title):
        self.email = email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password
        print(f"{self.name}'s Password has been updated to {new_password}.")

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title
        print(f"{self.name}'s Job Title has been updated to {new_job_title}.")

    def get_user_info(self):
        print("-----" * 24)
        print(f"User {self.email} currently works as a {self.current_job_title}. You can contact them at {self.email}")
