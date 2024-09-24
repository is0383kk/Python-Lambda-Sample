# How to  
## Build and Deploy  
```
$ sam build
$ sam deploy --config-file samconfig.toml
```

## How to call API  
＜Use in Windows PowerShell＞  
```
Invoke-WebRequest -Uri "https://XXXXXXXXXXXXXXXX/dev/data/00000" -Method Post -Headers @{"Content-Type"="application/json";"x-api-key"="XXXXXXXXXXXXXXXX"} -Body '{"name": "is0383kk"}'
```
＜Use in curl＞  
```
curl -X POST "https://XXXXXXXXXXXXXXXX/dev/data/00000" -H "Content-Type: application/json" -H "x-api-key: XXXXXXXXXXXXXXXX" -d "{\"name\": \"is0383kk\"}"
```
