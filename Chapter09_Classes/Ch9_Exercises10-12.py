# 9-10 Imported Restaurant
from restaurants import Restaurant

food = Restaurant('Pizza Land', 'pizza')

food.describe_restaurant()


# 9-11 Imported Admin
from users import Admin

tyson = Admin('tyson', 'nguyen', 'tysonnguyen', 22, 'oregon')
tyson.privileges.show_privileges()


# 9-12 Multiple Modules where User class in one module, and store the Privileges and Admin separately.
from user_privileges import Admin, Privileges

tyson = Admin('tyson', 'nguyen', 'tysonnguyen', 22, 'oregon')
tyson.privileges.show_privileges()