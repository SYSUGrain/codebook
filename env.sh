conda env export > environment.yml
conda create --name recoveredenv --file environment.yml
pip install -e .   # -e indicates that the package should be editable. That means that if you change the files inside the src folder, you don’t need to re-install the package for your changes to be picked up by Python.


