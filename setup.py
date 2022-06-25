import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    readme = fh.read()

setuptools.setup(
    name='uavlink',
    version='0.0.1',
    author_email="shayan.majumder2@gmail.com",
    description='UAV Link Simulation',
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/ShayanMajumder/Swarm_UAV_communication",
    license='MIT',
    python_requires='>=3.4',
    packages=setuptools.find_namespace_packages(where="src"),
    package_dir={"": "src"},
    install_requires=['numpy', 'matplotlib'],
)
