from setuptools import find_packages,setup
#call setup method
setup(
    name='mcqgenrator',
    version='0.0.1',
    author='Prtaiksha Patel',
    author_email='pratiksha@cloudyuga.guru',
    install_requires=["ctransformers","langchain","Flask","sentence-transformers","python-dotenv","PyPDF2","pinecone-client"],
    packages=find_packages()
)

