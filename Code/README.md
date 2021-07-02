# Code for our final project



### Requirements

We require our code to be run in jupyter lab or notebook, before we do that, there are some python packages you would need to install.



These packages are listed for you in the `requirements.txt` file. To install them, you must ensure pip is on your current system and execute `pip install -r requirements.txt`. If a permission error occurs please add the `--user` tag after install.



### Code structure

Our code is structured below:

* `data`
  
  * This folder contains the raw data we need to use, which is the CSV files containing happiness values and relavant features

* `src`
  
  * This folder contains actual code, within it, we want to run two jupyter notebooks to reproduce the results
  
  * `processData.ipynb`
    
    * This notebook file contains all the relevant techniques applied onto the csv data files in order to produce two pickled dataframes, `test.pkl` and `train.pkl`
  
  * `randomForest.ipynb`
    
    * This notebook file contains all the relevant techniques used to train, assess, measure and predict using random forest regressor and the previous two pickled dataframes.



Everything within the code structure should run as-is, meaning there is no need to modify file paths as they have been hard coded into the notebooks itself. Changing file paths are not advised.



In addition, there are comments throughout the notebook that should guide and give insight to the logic and design decisions that was made.
