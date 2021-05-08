import string
import random


def generate_password():
    pass


def random_password_generator():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    size = 8
    return ''.join(random.choice(chars) for x in range(size, 20))


def random_password_generator_ico():
    random_password_generator_ico = """
	#############################################################
	# PYTHON - Random Password Generetor (RPG) - GH0ST S0FTWARE #
	#############################################################
	#                         CONTACT                           #
	#############################################################
	#               DEVELOPER :      ⁱ " αм ツ ђ𝒶𝕧σ𝒸             #
	#          Mail Address :     atrimaysaha@gmail.com         #
	#   LINKEDIN : https://www.linkedin.com/in/sahaatrimay      #
	#              Whatsapp : + 91 9903 718 803                 #
	#############################################################
	"""
    print(random_password_generator_ico)

random_password_generator_ico()
print("Password : " + random_password_generator())
