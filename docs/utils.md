<!-- markdownlint-disable -->

<a href="../raesymatto/utils.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `utils`
Metric (SI) prefixes. 



---

<a href="../raesymatto/utils.py#L5"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Units`
Provides an interface to metric prefixes. 

See https://en.wikipedia.org/wiki/Metric_prefix#List_of_SI_prefixes 

Adapted from https://stackoverflow.com/a/20427577 



**Args:**
 
 - <b>`overrides`</b> (Optional[dict]):  Manual overrides. Might be helpful for  disabling certain prefixes. 

<a href="../raesymatto/utils.py#L17"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(overrides: Optional[dict] = None) → None
```

 






---

<a href="../raesymatto/utils.py#L76"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `convert`

```python
convert(number: float) → tuple[int, str]
```

Returns multiplier and prefix. 



**Args:**
 
 - <b>`number`</b> (float):  Number of interest. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
