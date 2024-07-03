import os
from dotenv import load_dotenv, dotenv_values

env_secret = dict(dotenv_values("C:/Users/Dell/KUSH_SCIFOR/Git/Practice/.env.secret"))
env_shared = dict(dotenv_values("C:/Users/Dell/KUSH_SCIFOR/Git/Practice/.env.shared"))
current_env = dict(os.environ)

config = {}
config.update(env_secret)
config.update(env_shared)
config.update(current_env)
print("Config: ",config)

