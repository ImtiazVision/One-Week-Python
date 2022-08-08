# pip is the Python package installer that we can use to install hundreds of thousands of packages for use in our projects. 


# PyPI: The Python Package Index is a repository of software for the Python programming language. It helps us find and install software developed and shared by the Python community. 

# translate sentences

from translate import Translator
translator = Translator(to_lang='es')
translation = translator.translate("Hello, I love you")
print(translation)