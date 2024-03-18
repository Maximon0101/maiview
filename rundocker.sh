docker stop maiview
docker rm maiview
docker run -it -d -v $(pwd):/opt/app --restart=always -p 8086:80 --name=maiview $(docker build -q .)