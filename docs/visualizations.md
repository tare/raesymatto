<!-- markdownlint-disable -->

<a href="../raesymatto/visualizations.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `visualizations`
Visualization related functions. 


---

<a href="../raesymatto/visualizations.py#L14"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `hide_frame`

```python
hide_frame(ax: Axes) → None
```

Hides spines. 



**Args:**
 
 - <b>`ax`</b> (plt.Axes):  Axes to be used. 


---

<a href="../raesymatto/visualizations.py#L26"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `draw_region_information`

```python
draw_region_information(
    ax: Axes,
    chromosome: str,
    start: int,
    end: int,
    fontsize: int = 7,
    kwargs: Optional[dict] = None
) → None
```

Draws region information. 



**Args:**
 
 - <b>`ax`</b> (plt.Axes):  Axes to be used. 
 - <b>`chromosome`</b> (str):  Chromosome of interest. 
 - <b>`start`</b> (int):  Start coordinate. 
 - <b>`end`</b> (int):  End coordinate. 
 - <b>`fontsize`</b> (int):  Font size. 
 - <b>`kwargs`</b> (Optional[dict]):  Additional arguments passed to Axes.arrow. 


---

<a href="../raesymatto/visualizations.py#L83"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `draw_bw`

```python
draw_bw(
    ax: Axes,
    chromosome: str,
    start: int,
    end: int,
    bw: bigWigFile,
    ymin: Optional[float] = None,
    ymax: Optional[float] = None,
    xspine: Optional[float] = None,
    skip: int = 1,
    fontsize: int = 7,
    ylabel: Optional[str] = None,
    label: Optional[str] = None,
    kwargs: Optional[dict] = None
) → None
```

Draws bigWig data. 



**Args:**
 
 - <b>`ax`</b> (plt.Axes):  Axes to be used. 
 - <b>`chromosome`</b> (str):  Chromosome of interest. 
 - <b>`start`</b> (int):  Start coordinate. 
 - <b>`end`</b> (int):  End coordinate. 
 - <b>`bw`</b> (pyBigWig.pybigWig):  bigWig object. 
 - <b>`ymin`</b> (Optional[float]):  Bottom of y axis. 
 - <b>`ymax`</b> (Optional[float]):  Top of y axis. 
 - <b>`xspine`</b> (Optional[float]):  Location for x spine. 
 - <b>`skip`</b> (int):  Visualize every skip-th value. Useful for downsampling. 
 - <b>`fontsize`</b> (int):  Font size. 
 - <b>`ylabel`</b> (Optional[str]):  Y axis label. 
 - <b>`label`</b> (Optional[str]):  Legend label. 
 - <b>`kwargs`</b> (Optional[dict]):  Additional arguments passed  to Axes.fill_between. 


---

<a href="../raesymatto/visualizations.py#L129"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `draw_bed`

```python
draw_bed(
    ax: Axes,
    chromosome: str,
    start: int,
    end: int,
    bed: DataFrame,
    fontsize=7,
    label: Optional[str] = None,
    frame: bool = True,
    scores: bool = False,
    cmap: str = 'Greys',
    vmin: Optional[float] = None,
    vmax: Optional[float] = None,
    spacing: int = 1,
    kwargs: Optional[dict] = None
) → None
```

Draws genomics regions defined using the BED format. 

Score defines the color. Does not take into account strand information at the moment. 



**Args:**
 
 - <b>`ax`</b> (plt.Axes):  Axes to be used. 
 - <b>`chromosome`</b> (str):  Chromosome of interest. 
 - <b>`start`</b> (int):  Start coordinate. 
 - <b>`end`</b> (int):  End coordinate. 
 - <b>`bed`</b> (pd.DataFrame):  Data in Browser Extensible Data (BED) format. 
 - <b>`fontsize`</b> (int):  Font size. 
 - <b>`label`</b> (Optional[str]):  Y axis label. 
 - <b>`frame`</b> (bool):  Draw spines. 
 - <b>`scores`</b> (bool):  Color the BED lines. 
 - <b>`cmap`</b> (str):  Colormap to be used when coloring the BED lines. 
 - <b>`vmin`</b> (Optional[float]):  Minimum score. 
 - <b>`vmax`</b> (Optional[float]):  Maximum score. 
 - <b>`spacing`</b> (int):  Spacing between rows of elements. 
 - <b>`kwargs`</b> (Optional[dict]):  Additional arguments passed  to mpl.patches.Rectangle. 


---

<a href="../raesymatto/visualizations.py#L238"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `draw_boxes`

```python
draw_boxes(
    ax: Axes,
    chromosome: str,
    start: int,
    end: int,
    bed: DataFrame,
    fontsize: int = 7,
    ylabel: Optional[dict] = None,
    vmin: Optional[float] = None,
    vmax: Optional[float] = None,
    kwargs: Optional[dict] = None
) → None
```

Draws genomics regions defined using the BED format. 

Score defines the height. Does not take into account strand information at the moment. 



**Args:**
 
 - <b>`ax`</b> (plt.Axes):  Axes to be used. 
 - <b>`chromosome`</b> (str):  Chromosome of interest. 
 - <b>`start`</b> (int):  Start coordinate. 
 - <b>`end`</b> (int):  End coordinate. 
 - <b>`bed`</b> (pd.DataFrame):  Data in Browser Extensible Data (BED) format. 
 - <b>`fontsize`</b> (int):  Font size. 
 - <b>`ylabel`</b> (Optional[str]):  Y axis label. 
 - <b>`vmin`</b> (Optional[float]):  Minimum score. 
 - <b>`vmax`</b> (Optional[float]):  Maximum score. 
 - <b>`kwargs`</b> (Optional[dict]):  Additional arguments passed  to mpl.patches.Rectangle. 


---

<a href="../raesymatto/visualizations.py#L295"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `draw_loops`

```python
draw_loops(
    ax: Axes,
    chromosome: str,
    start: int,
    end: int,
    bed: DataFrame,
    fontsize: int = 7,
    ymin: float = 1,
    ymax: float = 10,
    flip: bool = False,
    frame: bool = True,
    ylabel: Optional[str] = None,
    kwargs: Optional[dict] = None
) → None
```

Draws loops. 



**Args:**
 
 - <b>`ax`</b> (plt.Axes):  Axes to be used. 
 - <b>`chromosome`</b> (str):  Chromosome of interest. 
 - <b>`start`</b> (int):  Start coordinate. 
 - <b>`end`</b> (int):  End coordinate. 
 - <b>`bed`</b> (pd.DataFrame):  Data in Browser Extensible Data (BED) format. 
 - <b>`fontsize`</b>:  Font size. 
 - <b>`ymin`</b> (float):  Minimum loop height. 
 - <b>`ymax`</b> (float):  Maximum loop height. 
 - <b>`flip`</b> (bool):  Flip the y axis. 
 - <b>`frame`</b> (bool):  Draw spines. 
 - <b>`ylabel`</b> (Optional[str]):  Y axis label. 
 - <b>`kwargs`</b> (Optional[dict]):  Additional arguments passed  to mpl.patches.PathPatch. 


---

<a href="../raesymatto/visualizations.py#L362"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `draw_gene_models`

```python
draw_gene_models(
    ax: Axes,
    chromosome: str,
    start: int,
    end: int,
    genes: DataFrame,
    min_height: int = None,
    gene_name_field: str = 'gene_id',
    fontsize: int = 7,
    frame: bool = True,
    kwargs: Optional[dict] = None
) → None
```

Draws gene models. 



**Args:**
 
 - <b>`ax`</b> (plt.Axes):  Axes to be used. 
 - <b>`chromosome`</b> (str):  Chromosome of interest. 
 - <b>`start`</b> (int):  Start coordinate. 
 - <b>`end`</b> (int):  End coordinate. 
 - <b>`genes`</b> (pd.DataFrame):  Gene definitions in General Transfer  Format (GTF). 
 - <b>`min_height`</b> (Optional[int]):  Minimum number of gene tracks.  This can be used to have predictable gene heights. 
 - <b>`gene_name_field`</b> (str):  Name of the column to be used  when labeling genes. 
 - <b>`fontsize`</b> (int):  Font size. 
 - <b>`frame`</b> (bool):  Draw spines. 
 - <b>`kwargs`</b> (Optional[dict]):  Additional arguments passed to Axes.text. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
