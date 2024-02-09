![logo]("https://github.com/farhadm1990/pytmler/pix/logo.png")

# PyTmler

## A tiny python package to create shinny html report directly from python outputs. 

### Installation

```python

pip install --user pytmler

```

Alternatively, you can download the latest version from this github page and install it locally:

```python

git clone https://github.com/farhadm1990/pytmler.git

cd pytmler

pip install .

```

### Usage

```python

from pytmler.htmler import report_maker

```

### Instances
`report_maker` is the main class of pytmler package that has four instances: `plot_add` to add plots, `table_add` to add tables, `text_add` to add body of texts, `cod_add` to add code snippets, and `div_rm` to remove a certain element from your html report.

#### Example

```python
#create the empty file by running report_maker()

html = report_maker(out_name="report_name", 
                           out_dir="/output/dir", 
                           title="any titles", 
                           user="Farhad", 
                           logo="/path/to/any/logo.png | or url", header_color="black")

```

```python
# Adding elements to the html class object.

html.plot_add() #To add plots 
html.text_add() #To add body of text
html.table_add() #TO add tables
html.code_add() #To add code chunks
html.TD_add()   #To add protein 3D models.
html.div_rm()   # To remove any of above-mentioned elements from your report.

```

