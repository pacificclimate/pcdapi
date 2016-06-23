# pcdapi

The PCDAPI defines a REST API to the Pacific Climate Impact Consortium's (PCIC) Provincial Climate DataSet (PCDS)

## Installation

```bash
pyvenv venv
$ source venv/bin/activate
(venv)$ pip install -U pip
(venv)$ pip install --trusted-host tools.pacificclimate.org -i http://tools.pacificclimate.org/pypiserver/ -e .
```

## Testing

```bash
pip install pytest
py.test -v
```
