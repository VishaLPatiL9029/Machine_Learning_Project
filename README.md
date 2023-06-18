## Machine_Learning_Project

### This is first machine learning project


### Software and account Rqquirement.

1. [Github Account](https://github.con)
2. [aws Account](httpas://dashboard.aws.com/login)
3. [git cli](https://git.com)


### creating conda environment


```
conda create -p venv python == 3.7 -y
```

```
conda activate venv/
```
> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status

```
git status
```
To check all version maintain by git

```
git log

```

To create version/commit all changes by git

```
git commit -m "message"
```

To send version/changes to github

```
git push origin main
```
To check remote github

```
git remote -v
```

build docker image

```
docker build -t <image_name>:<tagname> .
```

> note: Image name for docker must be lowercase



Run docker image

```
docker run -p 5000:5000 -e PORT=5000 e34817b6c5ea
```

To check running container in docker

```
docker ps
```

to stop docker container

```
docker stop <container_id>
```