<h1>My first Django Project</h1>

This is my first Django Project. This project is written in Python.
### Contets
<ul>
    <li><a href="#whatisthis">What is this Project about</a></li>
    <li><a href="#requirements">Requirements</a></li>
    <li><a href="#instruction">Instruction</a></li>
    <li><a href="#tech-stack">Tech Stack</a></li>
</ul>

<h2 id="whatisthis">What is this Project about</h2>
This project holds the articles data for the blog.
I have worked on this project to demonstrate my experience
with Python, Django, graphQL, and Docker.

<h2 id="requirements">Requirements</h2>
Make sure you have installed the following packages in your computer
<ul>
    <li>Python3</li>
    <li>Docker</li>
</ul>

<h2 id="instruction">Instruction</h2>
For running this django app,
<ol>
    <li>Clone this repository</li>
    <li>Go to the root directory of the project</li>
    <li>run "docker-compose up -d --build"</li>
</ol>

For cleaning up the app,
<ol>
    <li>Move to the root of the project</li>
    <li>run "docker-compose down"</li>
    <li>run "docker system prune" and answer with y with the following question</li>
    <li>run "docker volume ls" to see the remaining container</li>
    <li>run "docker volume rm ${name of container}" and fill in the name</li>
</ol>

<h2 id="tech-stack">Tech Stack</h2>
<ul>
    <li>Docker: used to ensure the same working environment</li>
    <li>Django: Web server module</li>
    <li>Django Rest Framework: enabling REST api for the server</li>
    <li>postgres: database for the Django</li>
    <li>graphene-django: enabling graphQL query over postgres database</li>
</ul>
