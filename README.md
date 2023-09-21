# HTMLER 
## A tiny python package to create shinny html report directly from python outputs. 

### Installation

```python

pip install git+https://github.com/farhadm1990/htmler

```

### Usage

```python

from htmler.htmler import report_maker

```

### Instances
`report_maker` is the main class of htmler function that has four instances: `add plot` to add plot, `table_add` to add tables, `text_add` to add body of texts, and `div_rm` to remove a certain element from your html report.

#### Example

```python
#create the empty file by running report_maker()

html = report_maker(out_name="report_name", out_dir="/output/dir", title="any titles", user="Farhad", logo="./data/Ku-logo.png", header_color="black")

```

