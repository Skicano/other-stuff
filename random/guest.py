class User:

    @staticmethod
    def get_user_name():
        first_name = input('Please enter your first name: ')
        last_name = input('Please enter your last name: ')
        full_name = first_name.title() + ' ' + last_name.title()
        return full_name

    @staticmethod
    def greet_user():
        print(f'Hello {User.get_user_name()}.')

    @staticmethod
    def get_info():
        info = input('Tell us why you like programing: ')
        return f'Volim programiranje jer: {info}.'


class Save(User):

    @staticmethod
    def save_user_info():
        with open('user_names.txt', 'w') as f:
            f.write(User.get_user_name() + '\n')
            f.write(User.get_info() + '\n')

    @staticmethod
    def read_user_info():
        with open('user_names.txt', 'r') as f:
            users = f.readlines()
        for user in users:
            print(user.rstrip())


class Poll(User):

    @staticmethod
    def poll():

        print('\nPlease enter your info in this poll. Enter "q" when you want to quit.\n')
        Save().save_user_info()
        print(f'Thank you for filling this poll.')


Poll().poll()
Save().read_user_info()
