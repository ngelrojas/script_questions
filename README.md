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

#### 4. run the test script, be sure that file automate.sh have permission to execute
```shell
-> chmod +x automate.sh
-> ./automate.sh
```


#### 5. run the script using app.sh, be sure that file app.sh have permission to execute
-- environment must be activated
```shell
-> chmod +x app.sh
-> ./app.sh
```

#### 6. import your .csv file in folder nodes_csv and change name to "data_nodes.csv"
#### 7. if you .csv file has a different name headers, change the name in load_csv.py, 
#### in lines show this message # CHANGE HERE