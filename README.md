1. Create network
- `docker network create selenium-net`

2. Start Hub
-  `docker run -d --network selenium-net --name selenium-hub selenium/hub`

3. Start Nodes
- `docker run -d --network selenium-net --name chrome-node selenium/node-chrome`
- `docker run -d --network selenium-net --name firefox-node selenium/node-firefox`

4. Run tests
- `docker run --rm --network selenium-net -v ${PWD}/results/chrome:/app/results/chrome test-chrome`
