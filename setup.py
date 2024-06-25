from setuptools import setup
from shared import __version__

setup(
    name='shared',  # Уникальное имя вашего модуля
    version=__version__,  # Версия модуля
    description='SqlAlchemy models',
    url='https://github.com/ваш_github/ваш_репозиторий',  # Ссылка на репозиторий (необязательно)
    author='Booblegum',
    author_email='booblegum42@gmail.com',
    packages=['shared'],  # Список пакетов, которые нужно установить
)
