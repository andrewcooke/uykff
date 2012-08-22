
from uykff.core.support.configure import Config
from uykff.core.db import startup as db_startup
from uykff.core.web import startup as web_startup


def main(config):
    db_startup(config)
    web_startup(config)


if __name__ == '__main__':
    main(Config())
