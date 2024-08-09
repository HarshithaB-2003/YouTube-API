
from setuptools import setup, find_packages

from setuptools import setup, find_packages

setup(
    name='youtube_data_api_transcript_wrapper',
    version='0.1.0',
    packages=find_packages(include=['youtube_data_api', 'transcript_api']),
    install_requires=[
        # List your dependencies here
    ],
    tests_require=[
        'pytest',
        # Any additional test dependencies
    ],
    test_suite='tests',
    author='Harshitha_2003.B',
    author_email='praniharshitha@gmail.com',
    description='A brief description of your package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/my_package',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)


setup(
    name="youtube_transcript_api_wrapper",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "youtube-transcript-api"
    ],
    description="A wrapper module for YouTube Transcript API.",
    author='Harshitha_2003.B',
    author_email='praniharshitha@gmail.com',
    url="https://github.com/yourusername/youtube_transcript_api_wrapper",
)

