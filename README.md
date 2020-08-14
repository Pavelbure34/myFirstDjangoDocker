<h1>My first Django Project</h1>

This is my first Django Project. This project is written in Python.
### Contets
<ul>
    <li><a href="#terms">Terms</a></li>
    <li><a href="#whatisthis">What is this Project about</a></li>
    <li><a href="#requirements">Requirements</a></li>
    <li><a href="#instruction">Instruction</a></li>
    <ul>
        <li><a href="#instruction-runningtheproject">running the project</a></li>
        <li><a href="#instruction-addingasubapp">adding a sub-app</a></li>
        <li><a href="#instruction-cleaningup">cleaning up the project</a></li>
    </ul>
    <li><a href="#models">Models in this App</a></li>
    <li><a href="#tech-stack">Tech Stack</a></li>
</ul>

<h2 id="terms">Terms</h2>
This project contains the secret key for this django project.
I do not intend to use this Django app for production.
This project is free to use and tinker with.

<h2 id="whatisthis">What is this Project about</h2>
This project shows backend of web blog which stores the articles data and link,
 using  Python, Django, graphQL, and Docker.
I have worked on this project to demonstrate my experience with the
following languages and packages.

<h2 id="requirements">Requirements</h2>
Make sure you have installed the following packages in your computer
<ul>
    <li>Python3</li>
    <li>Docker Desktop</li>
</ul>

<h2 id="instruction">Instruction</h2>

<h3 id="instruction-runningtheproject">For running this django project,</h3>
<ol>
    <li>Clone this repository</li>
    <li>Go to the root directory of the project</li>
    <li>run "docker-compose up -d --build" to build and run the container</li>
    <li>run "docker-compose run web python manage.py migrate" to complete the initial installment</li>
    <li>run "docker-compose run web python manage.py createsuperuser" to create the super user</li>
    <li>create the super user.</li>
    <li>check if the server is running with "http://localhost:8000/"</li>
    <li>If so, go to "http://localhost:8000/admin" and use your superuser account to log in</li>
    <li>and enjoy!</li>
</ol>

<h3 id="instruction-addingasubapp">For adding your own sub-application,</h3>
<ul>
    <li>move to the root of the project</li>
    <li>run "mkdir ./myfirstdjango/${dir_name}"</li>
    <li>run "docker-compose run web python manage.py startapp ${app_name} ./myfirstdjango/${dir_name}"</li>
</ul>

<h3 id="instruction-cleaningup">For cleaning up the project,</h3>
<ol>
    <li>Move to the root of the project</li>
    <li>run "docker-compose down"</li>
    <li>run "docker system prune" and answer with y with the following question</li>
    <li>run "docker volume ls" to see the remaining container</li>
    <li>run "docker volume rm ${name of container}" and fill in the name</li>
</ol>

<h2 id="models">Models in this App</h2>

### article
<ul>
    <li>id: unique id</li>
    <li>end_point: end point for the article</li>
    <li>title: title for the article</li>
    <li>author: author of the article</li>
    <li>posted_DateTime: date and time of the article when posted</li>
    <li>likes: number of likes</li>
    <li>contents: content for the article</li>
</ul>

### reply
<ul>
    <li>id: unique id</li>
    <li>target_article: target article for the reply</li>
    <li>author: author of the article</li>
    <li>posted_DateTime: date and time of the article when posted</li>
    <li>contents: content for the article</li>
</ul>

<h2 id="tech-stack">Tech Stack</h2>
<ul>
    <li>Docker: used to ensure the same working environment</li>
    <li>Django: Web server module</li>
    <li>Django Rest Framework: enabling REST api for the server</li>
    <li>postgres: database for the Django</li>
    <li>graphene-django: enabling graphQL query over postgres database</li>
</ul>
