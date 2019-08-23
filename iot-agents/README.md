# Echo server for testing purposes

## Overview

It provides a basic functionality (reply with correct status codes) for functional/performance tests. 
  
## How to use

```bash
docker run -d -p 4096:4096 -p 7896:7896 fiware/echo:iot-agents
curl -XPOST http://localhost:4096/iot/devices
     201: Created
```
