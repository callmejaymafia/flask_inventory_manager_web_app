from dotenv import load_dotenv
from website import create_website

load_dotenv()
app = create_website()

if __name__ == '__main__':
    app.run()