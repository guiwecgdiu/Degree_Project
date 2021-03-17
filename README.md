flask-vue-todo
A todo app with Vue and backed by Flask

🚀 Live Demo preview

The demo is deployed on Heroku's free dyno and provides an interface of register/login for the use of a small group of users.

Start frontend development server
cd frontend
# install dependencies
yarn install

# serve with hot reload at localhost:8080
yarn run dev

# build for production with minification
yarn run build
Replace yarn with npm if you are using npm. Frontend pages will be served at http://localhost:8080

Note: In this mode, the backend is not available yet, any server request will fail on the page. It is only for frontend debugging.

Start flask development server
# In the repo root, install all dependencies
pipenv install

# Init DB
pipenv run flask db upgrade

# Start development server
FLASK_ENV=development pipenv run flask run
Pages will be served at http://localhost:5000.

Note: In this mode, all pages are served by Flask, so you need to build the frontend before this step.
