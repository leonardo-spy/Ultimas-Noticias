
from config.config import initialize
from core.app import app
from db.fauna import init


def main():
    vars_env = initialize()
    init(vars_env)  # init db
    # def async para abrir um websocket
    app(vars_env)


if __name__ == '__main__':
    main()
