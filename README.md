# Backend APP
# RatioAPI

Bu proje, kullanici verilerini goruntuleme ve ekleme islemini yapmak için kullanılan bir Flask ve SQLAlchemy tabanlı bir API içermektedir. SQLite ile olusturulmus veritabanına CSV dosyalarını yazma ve bu verileri okuma yeteneklerini içermektedir.

## Başlangıç

Projeyi çalıştırmak için aşağıdaki adımları takip edebilirsiniz.

### Gereksinimler

- Docker
- Docker Compose

### Kurulum

1. Projenin kök dizininde, aşağıdaki komutu kullanarak Docker konteynerini oluşturun:

    ```bash
    python -m venv env
    .\env\Scripts\activate
    docker login
    docker build -t ratioapi:latest .
    ```

    Bu komut, projeyi ayağa kaldıracak ve API'yi `localhost:5000` adresinde çalıştıracaktır.

2. API'yi kullanmaya başlamak için [Swagger arayüzüne](http://localhost:5000/) göz atabilirsiniz.

## Kullanım

Proje başarıyla çalıştığında, aşağıdaki adımları takip edebilirsiniz:

### Müşteri Verilerini Ekleme

Yeni müşteri verilerini eklemek için aşağıdaki adımları izleyebilirsiniz:

```bash
curl -X POST -H "Content-Type: multipart/form-data" -F "csv=@your_file.csv" http://localhost:5000/write-objects
