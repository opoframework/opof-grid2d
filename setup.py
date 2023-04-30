import os

from setuptools import find_namespace_packages, setup

with open(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
    encoding="utf-8",
) as f:
    long_description = f.read()

setup(
    name="opof-grid2d",
    version="0.2.0",
    description="OPOF domains for 2D grid worlds",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Yiyuan Lee",
    author_email="yiyuan.lee@rice.edu",
    project_urls={
        "Source": "https://github.com/opoframework/opof-grid2d",
    },
    url="https://github.com/opoframework/opof-grid2d",
    license="BSD-3",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.9",
    install_requires=[
        "opof",
        "torch",
        "numpy",
        "sortedcontainers",
        "tqdm",
        "mazelib-alt",
    ],
    extras_require={"tests": ["pytest", "pytest-cov", "pytest-timeout"]},
    packages=find_namespace_packages(),
    include_package_data=True,
    keywords="opof, optimization, machine learning, reinforcement learning, planning, grid world, robotics",
)
