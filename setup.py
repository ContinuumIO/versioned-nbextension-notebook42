import setuptools

setuptools.setup(
    name="foo",
    version='0.1.0',
    url="https://example.com/foo",
    author="Foo Bar",
    description="More foo in the Jupyter notebook",
    long_description="Foo",
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False,
)