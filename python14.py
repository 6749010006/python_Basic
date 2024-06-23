"""
#
#Part: Python PIP
#
"""

#pip list
#python.exe -m pip install - -upgrade pip
#pip install camelcase
#pip uninstall camelcase

import camlcase
camel = camlcase.Camelcase()
txt = "hello wolrd"
print(camel.hump(txt))
