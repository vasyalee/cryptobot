import telegram
import yaml

with open('config.yml') as f:
    
    data = yaml.load(f, Loader=yaml.FullLoader)
    



bot = telegram.Bot(token=data['TOKEN'])

