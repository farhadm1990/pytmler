#installing dependiencies
import importlib

required_modules = ["jinja2", "datetime", "pandas", "numpy", "requests", "beautifulsoup4", "pygments"]

for md in required_modules:
    try:
        importlib.import_module(md)
    except ImportError:
        print(f"Installing {md}...")
        try:
            import subprocess
            subprocess.check_call(["pip", "install", md])
        except Exception as e:
            print(f"Failed to install {md}: {e}")

from jinja2 import Template, Environment, FileSystemLoader
import datetime
import io
import base64
import os
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter





class report_maker:
    def __init__ (self, out_name, out_dir, title, user, logo, header_color):
        self.out_name =  out_name
        self.out_dir = out_dir
        self.title = title
        self.user = user
        self.logo = logo
        self.header_color = header_color

        #check if logo is a url or a file
        def is_valid_url(url):
            try:
                response = requests.head(url)
                return response.status_code == 200
            except requests.ConnectionError:
                return False
        if os.path.isfile(self.logo):
            with open(self.logo, 'rb') as logo:
                base_logo = base64.b64encode(logo.read()).decode()
                logo_src = f'data:image/png;base64,{base_logo}'
        else:
            if is_valid_url(self.logo):
                log_src = self.logo
            else:
                raise TypeError("Error: your logo pic must be either a vlid URL or a png file!")
        
        html_template = """
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="http://cdn.datatables.net/1.10.2/css/jquery.dataTables.min.css">
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.24.1/themes/prism.min.css">
                <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
                <script type="text/javascript" src="http://cdn.datatables.net/1.10.2/js/jquery.dataTables.min.js"></script>
                <script type="text/javascript" src="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.24.1/prism.min.js"></script>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.24.1/plugins/autoloader/prism-autoloader.min.js"></script>
                <script type="text/javascript" src="path/to/JSmol.min.js"></script>
                <script type="text/javascript" src="path/to/JSmolCore.js"></script>

                <style>
                    body {
                    font-family: Helvetica;
                    background-color: white;
                    margin: 0;
                    box-sizing: border-box; /* only once to be applied in the body.  */
                    }


                    .output-plot > img {
                        flex: auto;
                    }

                    label {
                        font-style: bold;
                        color:rgb(53, 2, 15);
                        width: 50%;
                    }

                    h1, h2, h3, h3, h4, h5, h6, p {
                        font-family: Helvetica;
                        overflow: hidden;
                    }

                    header {
                        margin-bottom: 100px;
                        padding: 20px;
                        display: flex;
                        flex-direction: row;
                        justify-content: space-between;
                        color: white;
                        top: 0px;
                        left: 0px;
                        z-index: 1000;
                        position: sticky;


                    }

                   #head-title {
                    transition: height 0.5s ease;
                   }

                   .head-title-hidden {
                    height: 0;
                    display: none;
                   } 
                
                    .title-section {
                        flex-direction: column;
                        align-items: flex-start;
                        justify-content: center;
                        font-family: Arial;
                        flex: 1 1 auto;
                        position: relative;
                    }

                    .logo-container {
                        display: flex;
                        align-items: center;
                        flex: 0 0 auto;
                        justify-content: center;
                    }

                    .logo {
                        max-width: 80px;
                    }

                    
                    h1 {
                        font-family: 'Helvetica', cursive;
                    }

                    form {
                        width: 90%;
                        margin: auto;
                        border: solid 1px grey;
                        border-radius: 20px 0 20px 0px;
                        padding: 0px 10px 10px 0;
                        background-color: rgb(71, 56, 69);
                    }

                    input,
                    textarea {
                        width: 50%;
                        margin: 3px 10px 5px 0;
                        padding: 8px;
                        background: rgb(255, 255, 255);
                        font-family: Lato;
                        border: solid 0.3px grey;
                    }

                    legend {
                        background: #F76C6C;
                        padding: 5px;
                        color: white;
                    }

                    .output-plot {
                        padding: 0 10px;
                        width: auto;
                        border: solid 1px rgb(150, 150, 150); 
                        border-radius: 8px;
                        margin: 30px 10px 30px 10px;
                        flex: auto;
                        overflow-x: auto;
                        overflow-y: auto;

                    }
                    
                    .sub-plot {
                        overflow-x: auto;
                    }

                    table th:nth-child(30), td:nth-child(30){
                        display: none;
                        flex: auto;
                        margin-left: 100px;
                    }
                    
                    .tabdiv {
                        overflow-x: auto; 
                        width: auto;
                        border: solid 1px rgb(150, 150, 150); 
                        border-radius: 8px;
                        margin: 30px 10px 30px 10px;
                        flex: auto;
                        background-color: rgb(236, 236, 236);
                    }

                    .table-title {
                        display: block;
                        margin-left: 10px;
                        margin-right: 10px;
                        margin-bottom: 20px;
                        border-bottom: solid 0.5px rgb(150, 150, 150);
                        padding: 20px 0 20px 10px;
                    }

                    .text-div {
                        width: auto;
                        border: solid 1px rgb(150, 150, 150); 
                        border-radius: 8px;
                        margin: 30px 10px 30px 10px;
                        flex: auto;
                        padding-left: 10px;
                        padding-right: 10px;
                    }

                </style>
            <title>The output report</title>
            </head>
            
            <body>
                <header style="background-color: {{ head_color }};">
                    <div class="title-section">
                        <h1 id="head-title">{{ title }}</h1>
                        <h2 style="margin-top: 1px; margin-bottom: 20px;"><strong>Author:</strong> {{ author }}</h2>
                        <p style="margin-top: 2px;">{{ date }}</p>
                    </div>
                    <div class="logo-container"> 
                        <img class="logo" src="{{ logo }}" >
                    </div>

                    
                
                </header>

                <h2 style="text-align: center; border-bottom: solid 0.5px rgb(150, 150, 150); padding-bottom: 20px; margin-left: 20px; margin-right: 20px;"> Report Form </h2>
                
                
                <!-- element_loc -->
            
                
            </body>
            <script>
                $(document).ready(function() {
                $('table').DataTable( {
                    responsive: "auto",
                    "pageLength": 10
                    
                    } );
                } );
            </script>
            <script>
                window.addEventListener('scroll', function() {
                    const header = document.getElementById('head-title');
                    if (window.scrollY > 100) { 
                        header.classList.add('head-title-hidden');
                    } else {
                        header.classList.remove('head-title-hidden');
                    }
                });

            </script>
            <script>
            function copyToClipboard(element) {
                var $temp = $("<input>");
                $("body").append($temp);
                $temp.val($(element).text()).select();
                document.execCommand("copy");
                $temp.remove();
            }

            
            $(".copy-button").click(function() {
                var codeElement = $(this).siblings("pre"); 
                copyToClipboard(codeElement);
            });
        </script>

        </html>

        """

        template = Template(html_template) 
        date = datetime.datetime.now().strftime("%Y-%m-%d")



        #create the raw html
        render_html = template.render(title = self.title, 
                                date = date, 
                                author = self.user,
                                logo = logo_src,
                                head_color = self.header_color
                                )
        out_file = f"{self.out_dir}/{self.out_name}.html"
        with open(out_file, 'w') as out:
            out.write(render_html)

    #plot adder
    def plot_add(self, plot: str, id: str, fignumber: str, plotcaption: str, height: int, width: int) -> None:
        #If plot is an external object
        if os.path.isfile(plot):
            with open(plot, 'rb') as p:
                 plot = base64.b64encode(p.read()).decode()
        # elif is_valid_url(plot):
        #         plot = plot
        #     else:
        #         raise TypeError("Error: your plot must be either a vlid URL, pyplot or a png file!")

        plot_div = str('<div id="{{ id }}" class="output-plot"><div class="plot-div"><h3>{{ fignumber }}</h3><p>{{ plotcaption }}</p><img style="height: {{ height }}px; width: {{ width }}px;" class="long-plot" src="data:image/png;base64,{{ plot }}" alt="{{ plotcaption }}" /></div> </div> \n        <!-- element_loc -->')

        env = Environment(loader=FileSystemLoader(self.out_dir))
        template = env.get_template(f"{self.out_dir}/{self.out_name}.html").render()
        temp = str(template).replace('<!-- element_loc -->', plot_div)
        template = Template(temp)

        plot_html = template.render(fignumber = fignumber, 
                                plotcaption = plotcaption, 
                                plot = plot,
                                height = height,
                                width = width,
                                id = id                                                             
                                )
        with open(f"{self.out_dir}/{self.out_name}.html", 'w') as out:
            out.write(plot_html)
            
    #Table adder
    def table_add(self, table: str, id: str, tabnumber: str, tabpaction: str) -> None:
        
        tab_div = str('<div id="{{ id }}" class="tabdiv" ><div class="table-title"><h3 style="display: flex; margin-bottom: 0;">{{ tabnumber }}</h3><p>{{ tabcaption }}</p><br></div><table id="table" class="display" cellspacing="0"><thead><tr>{% for column in table.columns %}<th>{{ column }}</th>{% endfor %}</tr></thead><tbody>{% for row in table.values %}<tr>{% for value in row %}<td>{{ value }}</td>{% endfor %}</tr>{% endfor %}</tbody></table></div> \n        <!-- element_loc -->')

        env = Environment(loader=FileSystemLoader(self.out_dir))
        template = env.get_template(f"{self.out_dir}/{self.out_name}.html").render()
        temp = str(template).replace('<!-- element_loc -->', tab_div)
        template = Template(temp)

        tab_html = template.render(table = table, 
                                tabnumber = tabnumber, 
                                tabcaption = tabpaction,
                                id = id   
                                                             
                                )
        with open(f"{self.out_dir}/{self.out_name}.html", 'w') as out:
            out.write(tab_html)
        
    #Text adder
    def text_add(self, header: str, id: str, text_body: str) -> None:
        
        text_div = str('<div id="{{ id }}" class="text-div" style="flex: auto; overflow: hidden;"><h3>{{ header }}</h3><p>{{ text_body }}</p></div> \n        <!-- element_loc -->')

        env = Environment(loader=FileSystemLoader(self.out_dir))
        template = env.get_template(f"{self.out_dir}/{self.out_name}.html").render()
        temp = str(template).replace('<!-- element_loc -->', text_div)
        template = Template(temp)

        text_html = template.render(header = header, 
                                text_body = text_body,
                                id = id   
                                                             
                                )
        
        with open(f"{self.out_dir}/{self.out_name}.html", 'w') as out:
            out.write(text_html)
    
    #Div remover
    def div_rm(self, id: str) -> None:
        with open(f"{self.out_dir}/{self.out_name}.html", 'rb') as html_file:
            html_content = html_file.read()
        soup = BeautifulSoup(html_content, 'html.parser')
        div_rm = soup.find(id=id)
        div_rm.extract()
        modified_html= str(soup)
        html  = Template(modified_html)
        out = html.render()
        with open(f"{self.out_dir}/{self.out_name}.html", 'w') as output:
            output.write(out)
        
    #Code adder
    def code_add(self, id: str, code_snippet: str, latex_enc: "python")  -> None:

        lexer = get_lexer_by_name(latex_enc)

        highlighted = highlight(code_snippet, lexer, HtmlFormatter())

        code_div = """
        <div class="code-container" id="{{ id }}" style="background-color: rgb(245, 245, 245); border: solid 0.05px rgb(150, 150, 150); border-radius: 5px; padding-bottom: 10px; padding-left: 10px; padding-top: 20px; margin-left: 10px; margin-right: 10px; margin-bottom: 20px; margin-top: 20px; position: relative; overflow-x: auto;">
            
            <pre class="language-javascript"><br>
                <code><br>{{ highlighted }}<br></code><br>
            </pre>
            <button style="position: absolute; top: 5px; left: 5px;" class="copy-button" onclick="copyToClipboard({{ id }})">Copy</button>
            
        </div>
        <!-- element_loc -->

        """
        env = Environment(loader=FileSystemLoader(self.out_dir))
        template = env.get_template(f"{self.out_dir}/{self.out_name}.html").render()
        temp = str(template).replace('<!-- element_loc -->', code_div)
        template = Template(temp)

        code_html = template.render(highlighted = highlighted,
                                id = id   
                                                             
                                )
        with open(f"{self.out_dir}/{self.out_name}.html", 'w') as out:
            out.write(code_html)

    #3D molecule
    def TD_add(self, id: str, fignumber: str, plotcaption: str, height: int, width: int, cif_path: str)  -> None:
        
        with open(cif_path, 'r') as cif_file:
            cif_content = cif_file.read()


        td_div = f"""
        <div id="{ id }" class="3d-molecule" style="height: { height }px; width: { width }px;"><h3>{ fignumber }</h3><p>{ plotcaption }</p> </div>
        <script type="text/javascript">
            var viewer = $3Dmol.createViewer($("#{ id }"), {{
                width: { width },
                height: { height }
            }});
            viewer.addModel('{ cif_content }', 'cif');
            viewer.setStyle({{}});
            viewer.zoomTo();
            viewer.render();
        </script>\n  
        <!-- element_loc -->'

        """
        env = Environment(loader=FileSystemLoader(self.out_dir))
        template = env.get_template(f"{self.out_dir}/{self.out_name}.html").render()
        temp = str(template).replace('<!-- element_loc -->', td_div)
        template = Template(temp)

        code_html = template.render(height = height,
                                    width = width,
                                    fignumber = fignumber,
                                    plotcaption = plotcaption,
                                    id = id   
                                                             
                                )
        with open(f"{self.out_dir}/{self.out_name}.html", 'w') as out:
            out.write(code_html)

