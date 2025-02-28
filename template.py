'''
Bir proje başlarken, her seferinde elle klasör ve dosya oluşturmak yerine, 
bunu otomatik hale getiren bir script kodu.
'''

import os  # İşletim sistemi ile ilgili işlemleri yapmak için kullanılır (dosya ve klasör yönetimi).
from pathlib import Path  # Dosya yollarını sistem bağımsız bir şekilde yönetmek için kullanılır.
import logging  # Programın çalışma sırasında bilgi ve hata mesajlarını kaydetmek için kullanılır.

# Loglama ayarları: Çalışma sırasında hangi işlemlerin yapıldığını görmek için log formatı belirleniyor.
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


# Oluşturulacak dosyaların listesini belirtiyoruz.
list_of_files = [
    "src/__init__.py",  # src klasörünün içinde __init__.py dosyası (boş olabilir, genellikle modül oluşturmak için kullanılır)
    "src/helper.py",  # src klasöründe yardımcı fonksiyonları içeren helper.py dosyası
    "src/prompt.py",  # src klasöründe prompt ile ilgili işlemleri içeren bir Python dosyası
    ".env",  # Çevresel değişkenleri tutmak için .env dosyası
    "setup.py",  # Proje için başlangıç ayarlarını içeren setup.py dosyası
    "app.py",  # Ana uygulama dosyası (projeyi çalıştıracak dosya olabilir)
    "research/trials.ipynb",  # research klasöründe Jupyter Notebook dosyası
    "test.py"  # Testler için kullanılan test.py dosyası
]

# Listedeki her dosya için işlem yapıyoruz.
for filepath in list_of_files:
    filepath = Path(filepath) # Dosya yolunu sistem bağımsız hale getiriyoruz.

    # Dosyanın bulunduğu klasörü ve dosya adını ayırıyoruz.
    filedir, filename = os.path.split(filepath)

    # Eğer dosyanın içinde bulunduğu klasör belirtilmişse (boş değilse), bu klasörü oluşturuyoruz.
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Eğer klasör zaten varsa hata vermemesi için exist_ok=True kullanıyoruz.
        logging.info(f"Creating directory: {filedir} for the file: {filename}")  # Klasörün oluşturulduğunu logluyoruz.

    # Eğer dosya yoksa veya dosyanın boyutu 0 bayt ise, yeni bir dosya oluşturuyoruz.
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) ==0):
         with open(filepath, "w") as f:  # Dosyayı "w" (write) modunda açıyoruz, boş bir dosya oluşturuyoruz.
            pass  # Dosyaya içerik eklemiyoruz, sadece oluşturuyoruz.
         logging.info(f"Creating empty file: {filepath}")  # Dosyanın oluşturulduğunu logluyoruz.

    else:
        logging.info(f"{filename} already exists")  # Eğer dosya zaten varsa, bunu logluyoruz.