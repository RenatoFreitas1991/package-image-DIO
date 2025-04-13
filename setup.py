from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="image-processing-renato",
    version="0.0.1",
    author="Renato Freitas da Silveira",
    author_email="renatofsilveirax@gmail.com",
    description="pacote criado para desafio de Criando um Pacote de Processamento de Imagens com Python",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RenatoFreitas1991/package-image-DIO.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.12',
)