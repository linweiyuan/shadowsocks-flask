# shadowsocks-flask
## 基于Flask + Jinja2模板
### 构建
```bash
docker build -t shadowsocks-flask .
```
### 运行
```yaml
shadowsocks-flask:
  container_name: shadowsocks-flask
  image: shadowsocks-flask
  links:
    - mysql
  restart: unless-stopped
```
---
爬虫收集数据5000+条已全部失效故不放出
