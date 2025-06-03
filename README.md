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
docker build -t ethereum-transaction-processor
```

### Run container
```bash
docker run -e INFURA_API_KEY="<INFURA_API_KEY>" ethereum-transaction-processor <block_number>
```