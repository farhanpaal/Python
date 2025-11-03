from setuptools import setup, find_packages

setup(
    name="vocabulary-telegram-bot",
    version="1.0.0",
    description="Telegram bot for daily vocabulary words",
    packages=find_packages(),
    install_requires=[
        "python-telegram-bot==20.7",
        "requests==2.31.0",
        "schedule==1.2.0",
        "python-dotenv==1.0.0",
    ],
    entry_points={
        'console_scripts': [
            'vocabulary-bot=bot:main',
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    python_requires=">=3.6",
)