# XMeme : A Meme posting Django App

<p float="left">
  <img src="screenshots/XMEME 28-02-2021 23-31-03.png" width="200" />
<img src="screenshots/XMEME 28-02-2021 23-31-39.png"  width="200" />
<img src="screenshots/Edit Meme 28-02-2021 23-32-16.png"  width="200" />
</p>

---
Developed this app as a part of the Crio Externship program. This app allows you to post a meme using a image url

Deployed Frontend app link : [XmemeFrontend App](http://xmemefrontend.herokuapp.com)

Checkout Xmeme backend also : [XmemeBackend App](https://github.com/sukanta-nandi/XMEME-Backend)


---

# Instructions to run xmeme locally :

1. Clone the repo

```
git clone https://github.com/sukanta-nandi/XMEME-Frontend.git
```

2. Install python3 and vitualenv. cd into the cloned folder and create a virtual env. Activate your virtual env

```
pip3 install virtualenv
python3 -m venv <name of your venv>

# for linux
source <name of your venv>/bin/activate

#for windows
source <name of your venv>/scripts/activate
```

3. Install the requirements using requirements.txt for both backend and frontend

```
pip install -r XMEME-Frontend/requirements.txt
```

4.
```
cd XMEME-Frontend
python manage.py runserver <port>
```

5. Run the frontend
Note : check the BACKEND_URL in xmemeapp->views.py and specify your backend url


For first time run
```
cd XMEME-Frontend
python manage.py makemigrations
python manage.py migrate
```

```
cd XMEME-Frontend
python manage.py runserver <port>
```
