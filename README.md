# Programming Languages Statistics

Ushbu loyiha GitHub repository’laridan olingan ma’lumotlarni saqlash, tahlil qilish va API orqali taqdim etish uchun mo‘ljallangan.

---

## 📦 O‘rnatish

```bash
git clone https://github.com/raximov/programming-languages-statistics.git
cd programming-languages-statistics
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

---

## ⚙️ Ma’lumotlarni import qilish

Loyiha `reportapp` ichida maxsus Django management command bilan keladi. JSON fayldan ma’lumotlarni import qilish uchun:

```bash
python manage.py import_data path/to/file.json
```

### Misol:

```bash
python manage.py import_data data/github_repos.json
```

✅ Ushbu buyruq:
- `GithubReport` jadvalini to‘ldiradi  
- Har bir repositoriyaning `languages` massivini **`GithubLanguage`** jadvaliga yozadi  

Import tugagandan so‘ng terminalda quyidagiga o‘xshash xabar chiqadi:

```
Barcha  1250 qatorlar import qilindi
```

---

## 🗄️ Model tuzilmasi

**GithubReport** — asosiy repository ma’lumotlari:  
- owner, name, stars, forks, watchers  
- languages (JSON)  
- topics (JSON)  
- created_at, pushed_at va boshqa statistikalar  

**GithubLanguage** — har bir repository bo‘yicha dasturlash tillari:  
- repo (ForeignKey → GithubReport)  
- name (til nomi)  
- size (baytlarda hajm)  
- year (repo yaratilgan yili)  

---

## 🚀 API

### 1. Top 5 tillar bo‘yicha statistikasi
**Endpoint:**  
```
GET /api/report-orm/
```

**Namuna natija:**
```json
[
  {
    "year": 2020,
    "lang_name": "Python",
    "total_size": 1234567
  },
  {
    "year": 2020,
    "lang_name": "JavaScript",
    "total_size": 987654
  }
]
```

Bu API har bir yil bo‘yicha **eng ko‘p ishlatilgan TOP-5 dasturlash tillarini** qaytaradi.

---

## 🖥️ Serverni ishga tushirish

```bash
python manage.py migrate
python manage.py runserver
```

Brauzer orqali oching:  
👉 `http://127.0.0.1:8000/`

---

## 🔧 Foydali buyruqlar

Testlarni ishga tushirish:
```bash
python manage.py test
```

Superuser yaratish:
```bash
python manage.py createsuperuser
```

---

## 📑 .gitignore haqida

Loyihada `.gitignore` faylida quyidagilar yozilgan:

```
venv/
__pycache__/
*.pyc
*.sqlite3
.env
```

Shuning uchun `venv/` yoki `.env` fayllari **GitHub’ga push qilinmaydi**.

---

## 👨‍💻 Muallif

- GitHub: [raximov](https://github.com/raximov)  
- Joylashuv: Buxoro  
