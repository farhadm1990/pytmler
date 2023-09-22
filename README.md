# HTMLER 
## A tiny python package to create shinny html report directly from python outputs. 

### Installation

```python

pip install --user git+https://github.com/farhadm1990/pytmler.git

```

### Usage

```python

from pytmler.htmler import report_maker

```

### Instances
`report_maker` is the main class of pytmler package that has four instances: `plot_add` to add plots, `table_add` to add tables, `text_add` to add body of texts, and `div_rm` to remove a certain element from your html report.

#### Example

```python
#create the empty file by running report_maker()

html = htmler.report_maker(out_name="report_name", 
                           out_dir="/output/dir", 
                           title="any titles", 
                           user="Farhad", 
                           logo="/path/to/any/logo.png | or url", header_color="black")

```

