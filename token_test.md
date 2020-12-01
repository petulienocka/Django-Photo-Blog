curl -X POST -d "username=van&password=password" http://127.0.0.1:8000/api/auth/token/

eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyNSwidXNlcm5hbWUiOiJ2YW4iLCJleHAiOjE1OTEyMDI1NTksImVtYWlsIjoidmFuQHZhbi5jb20ifQ.uzRrnY7v6uJE6fqWTjS0PHuuQw9q43tN3vAaDvovJLE

curl -H "Authorization: JWT <your_token>" http://localhost:8000/protected-url/
