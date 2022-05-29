# Face_unlock
Unlocks the app using face verification and stores the username and password in the database

To install Locally and test the application

```bash
conda install -c conda-forge dlib  
pip install -r STREAMLIT/requirement.txt
pip install -r FASTAPI/requirement.txt
```

To test the Application using Docker

command to up the services
```bash
docker-compose up
```

command to down the services
```bash
docker-compose down
```

if making any changes and need to re build the image then you can
```bash
cd [folder name]
docker build -t [image name:tag name] .
```


