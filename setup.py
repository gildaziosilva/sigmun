from setuptools import setup, find_packages

setup(
    name="sigmun",
    version="0.1.0",
    description="SIGMUN — Sistema Integrado de Gestão Municipal",
    author="Equipe SIGMUN",
    author_email="sigmun@camacan.ba.gov.br",
    license="MIT",
    python_requires=">=3.10",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "fastapi>=0.110.0",
        "uvicorn[standard]>=0.29.0",
        "sqlalchemy>=2.0.0",
        "alembic>=1.13.0",
        "psycopg2-binary>=2.9.0",
        "pydantic>=2.6.0",
        "pydantic-settings>=2.2.0",
        "python-jose[cryptography]>=3.3.0",
        "passlib[bcrypt]>=1.7.4",
        "python-multipart>=0.0.9",
        "redis>=5.0.0",
        "celery>=5.3.0",
        "httpx>=0.27.0",
        "python-dotenv>=1.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=8.0.0",
            "pytest-asyncio>=0.23.0",
            "pytest-cov>=5.0.0",
            "ruff>=0.3.0",
            "mypy>=1.9.0",
            "black>=24.0.0",
            "isort>=5.13.0",
            "pre-commit>=3.6.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "sigmun=src.main:app",
        ],
    },
)
