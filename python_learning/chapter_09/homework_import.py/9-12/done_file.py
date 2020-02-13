from user import User
from privileges_admin import Admin, Privileges

admin = Admin('danil', 'lomakin', 15, 'dan programmer', 341021946235102002)
admin.privileges.privileges = [
	'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    	]
admin.privileges.show_privileges()
