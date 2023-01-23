FROM ubuntu:18.04
RUN apt update && apt upgrade
RUN apt install python3 -y
ADD desafio-01.sh desafio-01.sh
ADD desafio-02.py desafio-02.py
ADD cromai.log cromai.log
ADD pid.txt pid.txt
CMD ./desafio-01.sh