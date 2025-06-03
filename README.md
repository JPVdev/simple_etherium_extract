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

## Assumptions and stuff

- Infura probably has some form of rate limiting
    - Might be a good idea to implement some form of back-off
    - Might be a good idea to cache results
- Basic error handling
    - Might be good idee to implement more robust error handling, ties in with above

- Was not technically assumed but discovered that the value from Infura is hexadecimal string that needed to be converted to int. Large numbers can cause overflow issues. So ended up converting to str.

## Scale up considerations:

- parallelism using a python module of some sort. ie "concurrent.futures"
- using asynchronous requests
- using batched requests, afaik Infura supports it
- Not familiar with parquet, but some form of data partioning might help query performance maybe? (more on the ingestion side of things)
- Some form of retry logic and jitter(might be overkill) to deal with api limitations
    - Multiple api keys if its not costly or free
- Have a message queue where multiple instances can scale up and process a block
    - keeping in mind api restrictions
