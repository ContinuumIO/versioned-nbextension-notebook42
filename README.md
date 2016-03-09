# versioned-nbextension-notebook42

A strawman for trying out a versioning scheme for a closely-coupled
(server/nb)extension.

You would install it like:

```shell
python setup.py develop
jupyter serverextension enable --py foo --sys-prefix
jupyter nbextension install --py foo --sys-prefix
jupyter nbextension enable --py foo --sys-prefix
```