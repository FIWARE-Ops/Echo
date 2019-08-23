# Mock server for testing purposes

## Overview

It provides a basic functionality (reply with correct status codes) for functional/performance tests. 
  
## How to use

```bash
docker run -d -p 1026:1026 fiware/service.mock:orion --workers 2
curl -XGET http://localhost:1026/version
```
```json
{
    "orion": {
        "version": "1.8.0",
        "uptime": "",
        "git_hash": "",
        "compile_time": "",
        "compiled_by": "",
        "compiled_in": "",
        "release_date": "",
        "doc": ""
    }
}   
```
