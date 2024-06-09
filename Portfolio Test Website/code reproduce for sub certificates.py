import os

# Path to the folder containing the files
folder_path = "images/GADA/"

# List of filenames
filenames = [
    "Foundations of Data Science.pdf",
    "Get Started with Python.pdf",
    "Go Beyond the Numbers: Translate Data into Insights.pdf",
    "The Power of Statistics.pdf",
    "Regression Analysis: Simplify Complex Data Relationships.pdf",
    "The Nuts and Bolts of Machine Learning.pdf",
    "Google Advanced Data Analytics Capstone.pdf",
    "GADA.pdf"
]

for filename i
# Generate the HTML code
    html_code = "<article>\n"
    html_code += "<header>\n"
    html_code += "<h2><a>Odio magna<br /> sed consectetur</a></h2>\n"
    html_code += "</header>\n"
    html_code += "<div class='image fit'>\n"
    html_code += "<img src='" + os.path.join(folder_path, filename) + "' alt='' />\n"
    html_code += "</div>\n"
    html_code += "<p>Donec eget ex magna. Interdum et malesuada fames ac ante ipsum primis in faucibus. Pellentesque venenatis dolor imperdiet dolor mattis sagittis magna etiam.</p>\n"
    html_code += "<h3>SKILLS:</h3>\n"
    html_code += "<p>------------------------</p>\n"
    html_code += "<h3>Technologies:</h3>\n"
    html_code += "<p>...........................</p>\n"
    html_code += "<ul class='actions special'>\n"
    html_code += "<li><a class='button'>FILES</a></li><li><a class='button'>Verify</a></li>\n"
    html_code += "</ul>\n"
    html_code += "</article>"
    

# Print the generated HTML code
print(html_code)
