Practica 1.

Esta practica consta de realizar 3 proyectos en 3 frameworks diferentes(Laravel, Adonisjs y Flask). Los tres estan conectado a una misma base datos, lo cual el gestor que se utilizó es PostgreSQL.
Y cada uno se consume por medio de APIS.

~ ¿Que hacer después de clonar el repositorio?

		LARAVEL
1. Abrimos el proyecto de Laravel.
2. Instalaciones que debemos realizar para tener los paquetes necesarios en nuestro proyecto:
	~ npm install
3. Nos dirijimos al apartado de .env, en vamos a configurar la conexión de nuestra base de datos.
		DB_CONNECTION=pgsql
		DB_HOST=127.0.0.1
		DB_PORT=5432
		DB_DATABASE=[name_db]
		DB_USERNAME=[name_user]
		DB_PASSWORD=[password_user]
	3.1. Nos dirijimos a la carpeta "config", luego al archivo "database.php" en el checaremos si la configuración de la base de datos es para PostgreSQL.
		'default' => env('DB_CONNECTION', 'pgsql'),
4. Hacemos una migración con el siguiente comando: ~ php artisan make:migration
	4.1. Checamos en nuestro gestor de base de datos --> "pgAdmin" si la tabla que migramos se migro correctamente. Lo hacemos dandole click derecho a la base de datos en la opcion "refresh"
5. Levantamos el servidor con el siguiente comando: ~ php artisan serve
6. Consumimos la API que se realizo en el proyecto con cliente que mas usemos.
	http://127.0.0.1:8000/api/registro --> Es la URL que vamos a utilizar con el verbo "POST" y mediante un JSON le mandaremos los datos que requiere y los que nosotros le vamos a otorgar:
	{
		"name":"nombre_usuario",
		"email":"correo_usuario",
		"password":"contraseña_usuario"
	}
7. Checamos nuestra base de datos con el gestor pgAdmin y al darle click derecho a la base de datos que usamos saldra Query tools, en ella podremos hacer una consulta para verificar si los datos que mandamos fueron los correctos
	select * from users;

		ADONIS JS
1. Abrimos el proyecto de Adonisjs.
2. Instalaciones que debemos realizar para tener los paquetes necesarios en nuestro proyecto:
	~ npm install.
	~ npm install pg --save
3. Nos dirijimos al apartado de .env, en vamos a configurar la conexión de nuestra base de datos.
		DB_CONNECTION=pg
		DB_HOST=127.0.0.1
		DB_PORT=5432
		DB_USER=[name_user]
		DB_PASSWORD=[password_user]
		DB_DATABASE=[name_db]
4. Nos dirijimos a la carpeta "config", luego al archivo "database.js" en el checaremos si la configuración de la base de datos es para PostgreSQL.
		connection: Env.get('DB_CONNECTION', 'pg'),
5. Levantamos el servidor con el siguiente comando: ~ adonis serve --dev 
6. Consumimos la API que se realizo en el proyecto con cliente que mas usemos.
	http://127.0.0.1:3333/registrate --> Es la URL que vamos a utilizar con el verbo "POST" y mediante un JSON le mandaremos los datos que requiere y los que nosotros le vamos a otorgar:
	{
		"name":"nombre_usuario",
		"email":"correo_usuario",
		"password":"contraseña_usuario"
	}
7. Checamos nuestra base de datos con el gestor pgAdmin y al darle click derecho a la base de datos que usamos saldra Query tools, en ella podremos hacer una consulta para verificar si los datos que mandamos fueron los correctos
	select * from users;

			FLASK
1. Abrimos el proyecto de Flask (para ello ya debemos tener instalado python).
2. Instalaciones que debemos realizar para tener los paquetes necesarios en nuestro proyecto:
	~ pip install Flask --> Es el framework que vamos a utilizar
	~ pip instalar Flask-RESTful
	~ pip instalar SQLAlchemy --> Es una herramienta que nos da acceso a las bases de dato
3. Nos dirijimos al archivo .conf.py, en el vamos a configurar la conexión de nuestra base de datos.
	Debemos checar que los siguiente campos esten bien respecto a nuestra base de datos
	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://[name_user]:[password]@localhost:5432/[name_db]'
4. Levantamos el servidor con el siguiente comando: ~ python main.py
5.  Consumimos la API que se realizo en el proyecto con cliente que mas usemos.
	http://127.0.0.1:5000/usuario --> Es la URL que vamos a utilizar con el verbo "POST" y mediante un JSON le mandaremos los datos que requiere y los que nosotros le vamos a otorgar:
	{
		"name":"nombre_usuario",
		"email":"correo_usuario",
		"password":"contraseña_usuario"
	}
6. Checamos nuestra base de datos con el gestor pgAdmin y al darle click derecho a la base de datos que usamos saldra Query tools, en ella podremos hacer una consulta para verificar si los datos que mandamos fueron los correctos
	select * from users;