# web_console

This project is just to PoC, how to enable a bash-console inside a docker container, and been accessed through a web interface.  

## Requirements

- ttyd 

https://github.com/tsl0922/ttyd

- docker

## Diagram

```
    user1     user2
       \      /
        \    /
         wsgy (:5000)
        /    \
       /      \
    ttyd1      ttyd2
    (:8080)    (:8082)
    |                 \
    |                  \
docker                docker
(custom-image)        (custom-image)

```

- custom image: 
have a lot of restrictions in terms of bash. The idea is control what a user can do or can't. If we take a look at **Dockerfile** and how the image is created , we will see that we hide some commands, and we give priority over the **kubectl-x** command.

