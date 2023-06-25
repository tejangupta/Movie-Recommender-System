from setuptools import find_packages, setup

# edit below variables as per your requirements
REPO_NAME = 'Movie-Recommender-System'
AUTHOR_USER_NAME = 'tejangupta'

with open('README.md', encoding='utf-8') as file_obj:
    long_description = file_obj.read()

setup(
    name='movie-recommender',
    version='0.0.1',
    author=AUTHOR_USER_NAME,
    author_email='tejangupta8@gmail.com',
    description='A small package for Movie Recommender System',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    packages=find_packages(),
    license='MIT',
    python_requires='>=3.7',
    install_requires=['pandas', 'nltk', 'scikit-learn', 'streamlit']
)
