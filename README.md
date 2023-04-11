## setup

#### 1. create a python environment using
```shell
python3 -m venv backend
```

#### 2. activate the environment using
```shell
source backend/bin/activate
```

#### 3 . install requirements.txt using
```shell
pip install -r requirements.txt
```

#### 4. run the test script using
```shell
pytest --pyargs tests
```

#### 4. import .csv file and change name to "data_nodes.csv" put it in the same folder as the script
#### 5. if you .csv file has a different name headers, change the name in load_csv.py, 
#### in lines show this message # CHANGE HERE