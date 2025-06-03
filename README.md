# simple_etherium_extract

## setup local

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

```bash
pip install -r requirements.txt
```

```bash
cp .env_copy .env
```

```
paste in the missing environment variables values
```

```bash
export $(cat .env)
```

## Run local

```bash
python src/main.py "Block number here"
```

## Docker instructions

### Build the image
```bash
docker build -t ethereum-transaction-processor .
```

### Run container
```bash
docker run -e INFURA_API_KEY="<INFURA_API_KEY>" ethereum-transaction-processor <block_number>
```

### ssh into container if still running
```bash
docker exec -it ethereum-transaction-processor /bin/bash
```

### output the output files of the container
```bash
docker run -v $(pwd):/app -e INFURA_API_KEY="YOUR_INFURA_KEY" ethereum-transaction-processor "The block num"
    
```