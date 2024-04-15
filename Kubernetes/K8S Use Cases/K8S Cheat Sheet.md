#### A. Running App
(+) `kubectl run + <app name> --image=<repository>/<info>:<tag> --port=<port mapping> --labels app=<app name>`
==> `kubectl run demo --image=dixluwn/myhello_testk8s:v1.0 --port=9999 --labels app=demo`

(+) `kubectl port-forward <name> <port mapping>`
==> `kubectl port-forward demo 9999:8888`

(+) `kubectl get pods --selector app=<name>`
==> `kubectl get pods --selector app=demo`
