# Aircraft production app

Build, start and stop project with
```sh
./bin/docker/build.sh
./bin/docker/up.sh
./bin/docker/down.sh
```

Don't forget to :
```sh
chmod +x bin/docker/build.sh
chmod +x bin/docker/up.sh
chmod +x bin/docker/down.sh
```

When the project started it's available at :

[https://localhost](https://localhost)

You may have a warning with the ssl certificate, you can skip with trusting the certificate. Prebuilded certificate is located at : [config/nginx/certs/default](config/nginx/certs/default) , you can create yours by your owns and place it.

## Missing features

- ACL Gesture (everybody are admin)
- Documentation
- RESTful endpoint

## Available plugins

- **Django Admin** [https://localhost/admin/](https://localhost/admin/)
- **Swagger** [https://localhost/api/v1/schema/swagger-ui/](https://localhost/api/v1/schema/swagger-ui/)
- **Redoc** [https://localhost/api/v1/schema/redoc/](https://localhost/api/v1/schema/redoc/)

## Admin credentials
```
Username : admin
Password : password
```
Other user are listed in [server/apps/users/fixtures/default_users.json](server/apps/users/fixtures/default_users.json)

## How the app works

At first you should define Models and Parts in **Production** tab and after you can go to **Factory** tab to create desired part. **Teams** tabs allow an admin or a staff to maange group permission and members.