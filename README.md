# blog

## init
```bash
docker compose up -d --build
```
mount\app\container-init.shの改行コードはLFにすること


## createsuperuser
```bash
docker compose exec app bash
python manage.py createsuperuser
```

## 実装の改修の反映
```bash
docker compose restart app
```
